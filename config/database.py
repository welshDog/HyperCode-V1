# config/database.py
import os
from typing import AsyncGenerator

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

load_dotenv()


class DatabaseConfig:
    """Database configuration with environment variable support."""

    def __init__(self):
        # Get the DATABASE_URL from environment or use default SQLite
        db_url = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./hyperbase.db")
        # Ensure the URL uses aiosqlite
        if db_url.startswith("sqlite:///"):
            db_url = db_url.replace("sqlite:///", "sqlite+aiosqlite:///")
        self.DATABASE_URL = db_url

        self.POOL_SIZE = int(os.getenv("DB_POOL_SIZE", "10"))
        self.MAX_OVERFLOW = int(os.getenv("DB_MAX_OVERFLOW", "20"))
        self.ECHO = os.getenv("DB_ECHO", "true").lower() == "true"


# Initialize config
db_config = DatabaseConfig()

# SQLite-specific parameters
connect_args = {"check_same_thread": False} if "sqlite" in db_config.DATABASE_URL else {}

# Create async engine with SQLite-specific parameters
if "sqlite" in db_config.DATABASE_URL:
    engine = create_async_engine(
        db_config.DATABASE_URL,
        echo=db_config.ECHO,
        connect_args=connect_args,
        poolclass=None,  # Use default pool for SQLite
    )
else:
    engine = create_async_engine(
        db_config.DATABASE_URL,
        echo=db_config.ECHO,
        pool_size=db_config.POOL_SIZE,
        max_overflow=db_config.MAX_OVERFLOW,
        pool_pre_ping=True,
        pool_recycle=3600,
    )

# Session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

# Base class for models
Base = declarative_base()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Dependency to get DB session."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
