"""Database configuration and models for HyperFocus."""

import uuid
from contextlib import contextmanager
from datetime import datetime
from enum import Enum as PyEnum
from pathlib import Path
from typing import Generator

from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Integer,
    String,
    Table,
    Text,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session as SessionType
from sqlalchemy.orm import relationship, scoped_session, sessionmaker
from sqlalchemy.sql import func

# Association tables
task_tags = Table(
    "task_tags",
    Base.metadata,
    Column("task_id", Integer, ForeignKey("tasks.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)


class UserRole(str, PyEnum):
    ADMIN = "admin"
    USER = "user"
    VIEWER = "viewer"


# Base class for all models
Base = declarative_base()


class User(Base):
    """User model for authentication and authorization."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(128), nullable=False)
    is_active = Column(Boolean, default=True)
    role = Column(Enum(UserRole), default=UserRole.USER)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_login = Column(DateTime, nullable=True)
    preferences = Column(JSON, default=dict)

    # Relationships
    tasks = relationship("Task", back_populates="owner")
    sessions = relationship("Session", back_populates="user")
    projects = relationship("Project", back_populates="owner")


class Project(Base):
    """Project model for grouping related tasks."""

    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    owner_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_archived = Column(Boolean, default=False)

    # Relationships
    owner = relationship("User", back_populates="projects")
    tasks = relationship("Task", back_populates="project")


class Tag(Base):
    """Tag model for categorizing tasks."""

    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    color = Column(String(20))

    # Relationships
    tasks = relationship("Task", secondary=task_tags, back_populates="tags")


class Task(Base):
    """Task model for tracking work sessions."""

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    public_id = Column(String(36), unique=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(200), nullable=False)
    description = Column(Text)
    status = Column(
        String(20), default="pending"
    )  # pending, in_progress, completed, blocked, archived
    priority = Column(Integer, default=2)  # 1=high, 2=medium, 3=low
    due_date = Column(DateTime, nullable=True)
    estimated_duration = Column(Integer, nullable=True)  # in minutes
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)

    # Foreign keys
    owner_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=True)

    # Relationships
    owner = relationship("User", back_populates="tasks")
    project = relationship("Project", back_populates="tasks")
    sessions = relationship(
        "Session", back_populates="task", cascade="all, delete-orphan"
    )
    tags = relationship("Tag", secondary=task_tags, back_populates="tasks")

    # Properties
    @property
    def total_time_spent(self):
        """Return total time spent on this task in seconds."""
        return sum((s.duration or 0 for s in self.sessions if s.duration), 0)

    @property
    def is_overdue(self):
        """Check if the task is overdue."""
        if not self.due_date:
            return False
        return datetime.utcnow() > self.due_date

    title = Column(String(200), nullable=False)
    description = Column(Text)
    status = Column(
        String(20), default="pending"
    )  # pending, in_progress, completed, blocked
    priority = Column(Integer, default=2)  # 1=high, 2=medium, 3=low
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)


class Session(Base):
    """Work session model for tracking focused work periods."""

    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    public_id = Column(String(36), unique=True, default=lambda: str(uuid.uuid4()))
    task_id = Column(
        Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False
    )
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    start_time = Column(DateTime(timezone=True), server_default=func.now())
    end_time = Column(DateTime(timezone=True), nullable=True)
    duration = Column(Integer, nullable=True)  # in seconds
    focus_score = Column(Integer, nullable=True)  # 1-10 scale
    notes = Column(Text, nullable=True)
    metadata_ = Column("metadata", JSON, default=dict)  # For additional tracking data

    # Performance metrics
    keystrokes = Column(Integer, default=0)
    distractions = Column(Integer, default=0)
    app_usage = Column(JSON, default=list)  # Track application usage during session

    # Relationships
    task = relationship("Task", back_populates="sessions")
    user = relationship("User", back_populates="sessions")

    @property
    def productivity_score(self):
        """Calculate a productivity score based on session metrics."""
        if not self.duration or self.duration == 0:
            return 0

        # Base score from focus
        score = (self.focus_score or 5) / 10.0

        # Adjust based on distractions
        if self.distractions > 0:
            score *= max(0, 1 - (self.distractions * 0.1))

        return round(score * 100, 2)


class Database:
    """Database connection and session management with enhanced features."""

    def __init__(self, db_url: str = None):
        self.db_url = db_url or f"sqlite:///{Path.home()}/.hyperfocus/hyperfocus.db"
        self.engine = create_engine(
            self.db_url,
            echo=False,
            connect_args={"check_same_thread": False}
            if "sqlite" in self.db_url
            else {},
        )
        self.SessionLocal = scoped_session(
            sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.engine,
                expire_on_commit=False,
            )
        )
        self.metadata = Base.metadata

    def init_db(self, create_admin: bool = False) -> None:
        """Initialize the database by creating all tables and optionally an admin user.

        Args:
            create_admin: If True, creates a default admin user
        """
        # Create the database directory if it doesn't exist
        if self.db_url.startswith("sqlite"):
            db_path = Path(self.db_url.replace("sqlite:///", ""))
            db_path.parent.mkdir(parents=True, exist_ok=True)

        # Create all tables
        Base.metadata.create_all(bind=self.engine)

        # Create default admin user if requested
        if create_admin:
            from passlib.context import CryptContext

            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

            with self.get_session() as session:
                admin = session.query(User).filter(User.username == "admin").first()
                if not admin:
                    admin = User(
                        username="admin",
                        email="admin@example.com",
                        hashed_password=pwd_context.hash("admin"),
                        role=UserRole.ADMIN,
                    )
                    session.add(admin)
                    session.commit()

    @contextmanager
    def get_session(self) -> Generator[SessionType, None, None]:
        """Provide a transactional scope around a series of operations."""
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def close(self) -> None:
        """Close the database connection."""
        self.SessionLocal.remove()
        if hasattr(self, "engine"):
            self.engine.dispose()


# Global database instance
db = Database()


def init_db() -> None:
    """Initialize the database."""
    db.init_db()
