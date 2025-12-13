"""Database utilities for HyperFocus."""

from contextlib import contextmanager
from pathlib import Path
from typing import Generator, Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import Session as SessionType
from sqlalchemy.orm import scoped_session, sessionmaker

from .config import load_config
from .database import Base, Task, db


def init_database() -> None:
    """Initialize the database with configuration from settings."""
    config = load_config()
    db_url = config.database.url

    # Create the database directory if it doesn't exist
    if db_url.startswith("sqlite"):
        db_path = db_url.replace("sqlite:///", "")
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    # Create engine and session
    db.engine = create_engine(db_url, echo=config.database.echo)
    db.SessionLocal = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=db.engine)
    )

    # Create tables
    Base.metadata.create_all(bind=db.engine)


@contextmanager
def get_db() -> Generator[SessionType, None, None]:
    """
    Dependency to get DB session.

    Example:
        with get_db() as session:
            # Use the session
            result = session.query(Task).all()
    """
    if not hasattr(db, "SessionLocal") or db.SessionLocal is None:
        init_database()

    session = db.SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def get_task(session: SessionType, task_id: int) -> Optional[Task]:
    """Get a task by ID.

    Args:
        session: Database session
        task_id: ID of the task to retrieve

    Returns:
        Optional[Task]: The task if found, None otherwise
    """
    return session.query(Task).filter(Task.id == task_id).first()


def create_task(
    session: SessionType,
    title: str,
    description: str = "",
    priority: int = 2,
    status: str = "pending",
) -> Task:
    """Create a new task."""
    task = Task(title=title, description=description, priority=priority, status=status)
    session.add(task)
    session.commit()
    return task
