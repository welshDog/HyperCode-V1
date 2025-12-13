# Database Configuration & Initialization
# SQLAlchemy engine, session management, and connection pooling

from sqlalchemy import create_engine, event, pool
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool
from contextlib import contextmanager
import os
from pathlib import Path
from typing import Generator
import logging

from database_utils.models import Base

logger = logging.getLogger(__name__)

# ============================================================================
# Database Configuration
# ============================================================================

class DatabaseConfig:
    """Centralized database configuration."""
    
    # SQLite for development (easy, portable)
    # For production: use PostgreSQL, MySQL, etc.
    DB_TYPE = os.getenv('DB_TYPE', 'sqlite')
    DB_PATH = Path(os.getenv('DB_PATH', 'data/research.db'))
    
    if DB_TYPE == 'sqlite':
        DATABASE_URL = f'sqlite:///{DB_PATH}'
    elif DB_TYPE == 'postgresql':
        DB_USER = os.getenv('DB_USER', 'postgres')
        DB_PASSWORD = os.getenv('DB_PASSWORD', '')
        DB_HOST = os.getenv('DB_HOST', 'localhost')
        DB_PORT = os.getenv('DB_PORT', '5432')
        DB_NAME = os.getenv('DB_NAME', 'hypercode')
        DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    elif DB_TYPE == 'mysql':
        DB_USER = os.getenv('DB_USER', 'root')
        DB_PASSWORD = os.getenv('DB_PASSWORD', '')
        DB_HOST = os.getenv('DB_HOST', 'localhost')
        DB_PORT = os.getenv('DB_PORT', '3306')
        DB_NAME = os.getenv('DB_NAME', 'hypercode')
        DATABASE_URL = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    else:
        raise ValueError(f"Unsupported database type: {DB_TYPE}")
    
    # Connection pooling
    POOL_SIZE = int(os.getenv('DB_POOL_SIZE', '10'))
    MAX_OVERFLOW = int(os.getenv('DB_MAX_OVERFLOW', '20'))
    POOL_RECYCLE = int(os.getenv('DB_POOL_RECYCLE', '3600'))
    ECHO_SQL = os.getenv('DB_ECHO_SQL', 'False').lower() == 'true'


# ============================================================================
# Engine and Session Factory
# ============================================================================

def create_db_engine():
    """Create SQLAlchemy engine with appropriate configuration."""
    
    engine_kwargs = {
        'echo': DatabaseConfig.ECHO_SQL,
    }
    
    if DatabaseConfig.DB_TYPE == 'sqlite':
        # Use StaticPool for SQLite to avoid threading issues
        engine_kwargs['connect_args'] = {'check_same_thread': False}
        engine_kwargs['poolclass'] = StaticPool
    else:
        # Connection pooling for production databases
        engine_kwargs.update({
            'pool_size': DatabaseConfig.POOL_SIZE,
            'max_overflow': DatabaseConfig.MAX_OVERFLOW,
            'pool_recycle': DatabaseConfig.POOL_RECYCLE,
        })
    
    engine = create_engine(DatabaseConfig.DATABASE_URL, **engine_kwargs)
    
    # Enable Foreign Key support for SQLite
    if DatabaseConfig.DB_TYPE == 'sqlite':
        @event.listens_for(engine, 'connect')
        def set_sqlite_pragma(dbapi_conn, connection_record):
            cursor = dbapi_conn.cursor()
            cursor.execute('PRAGMA foreign_keys=ON')
            cursor.close()
    
    logger.info(f"Database engine created: {DatabaseConfig.DB_TYPE}")
    return engine


# Global engine instance
engine = create_db_engine()

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False
)


# ============================================================================
# Database Initialization & Management
# ============================================================================

def init_db(drop_all: bool = False):
    """
    Initialize database schema.
    
    Args:
        drop_all: If True, drops all tables before creating (DANGEROUS!)
    """
    if drop_all:
        logger.warning("Dropping all tables...")
        Base.metadata.drop_all(bind=engine)
    
    logger.info("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    logger.info("Database initialization complete")


def get_db() -> Session:
    """Get a database session."""
    return SessionLocal()


@contextmanager
def get_db_context() -> Generator[Session, None, None]:
    """
    Context manager for database sessions.
    Automatically commits on success and rolls back on error.
    
    Usage:
        with get_db_context() as session:
            papers = session.query(ResearchPaper).all()
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception as e:
        db.rollback()
        logger.error(f"Database error: {e}")
        raise
    finally:
        db.close()


def close_db():
    """Close database connections."""
    engine.dispose()
    logger.info("Database connections closed")


# ============================================================================
# Database Health Check & Utilities
# ============================================================================

def check_db_connection() -> bool:
    """Test database connection."""
    try:
        with engine.connect() as conn:
            conn.execute("SELECT 1")
        logger.info("Database connection successful")
        return True
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        return False


def get_db_stats():
    """Get database statistics."""
    try:
        with get_db_context() as session:
            from database_utils.models import (
                ResearchPaper, ResearchAgent, ResearchTask, 
                KnowledgeNode, KnowledgeRelationship
            )
            
            stats = {
                'papers': session.query(ResearchPaper).count(),
                'agents': session.query(ResearchAgent).count(),
                'tasks': session.query(ResearchTask).count(),
                'knowledge_nodes': session.query(KnowledgeNode).count(),
                'relationships': session.query(KnowledgeRelationship).count(),
            }
            return stats
    except Exception as e:
        logger.error(f"Failed to get DB stats: {e}")
        return {}


# ============================================================================
# CLI Database Commands
# ============================================================================

import click

@click.group()
def db_cli():
    """Database management commands."""
    pass


@db_cli.command()
def init():
    """Initialize database."""
    if click.confirm('This will create all database tables. Continue?'):
        init_db()
        click.echo("✓ Database initialized")


@db_cli.command()
def reset():
    """Reset database (DANGEROUS)."""
    if click.confirm('This will DELETE ALL DATA. Are you absolutely sure?'):
        if click.confirm('Type "yes" to confirm deletion', default=False):
            init_db(drop_all=True)
            click.echo("✓ Database reset")


@db_cli.command()
def stats():
    """Show database statistics."""
    stats = get_db_stats()
    click.echo("\nDatabase Statistics:")
    click.echo("=" * 40)
    for key, value in stats.items():
        click.echo(f"{key:.<30} {value}")


@db_cli.command()
def migrate():
    """Run Alembic migrations."""
    import subprocess
    result = subprocess.run(['alembic', 'upgrade', 'head'])
    if result.returncode == 0:
        click.echo("✓ Migrations completed")
    else:
        click.echo("✗ Migration failed")


if __name__ == '__main__':
    db_cli()
