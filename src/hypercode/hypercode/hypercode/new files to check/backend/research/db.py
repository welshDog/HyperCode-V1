"""
Database configuration for the HyperCode research module.

This module defines a SQLAlchemy engine and session factory
used throughout the research layer.  The database URL is read
from the ``RESEARCH_DATABASE_URL`` environment variable.  If
unset, a local SQLite database will be used as a sensible
default so that the schema can be inspected without additional
configuration.

Example usage:

    from hypercode.backend.research import Base, SessionLocal
    from hypercode.backend.research.models import Study

    # create all tables
    Base.metadata.create_all(bind=engine)

    # open a session and use the ORM
    db = SessionLocal()
    try:
        study = Study(slug="example", title="Example Study")
        db.add(study)
        db.commit()
    finally:
        db.close()

"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


def _get_database_url() -> str:
    """Return the database URL to connect to.

    Checks the ``RESEARCH_DATABASE_URL`` environment variable first.  If
    it isn't defined then falls back to a local SQLite file so that
    development and testing can proceed without a PostgreSQL server.
    """

    url = os.getenv("RESEARCH_DATABASE_URL")
    if url:
        return url
    # fallback to a local SQLite database in the project root
    # note: relative paths in SQLite URLs are resolved relative to the
    # current working directory.  A persistent file makes it easier to
    # inspect the database from outside of the application.
    return "sqlite:///hypercode_research.db"


# Create the SQLAlchemy engine.  ``future=True`` enables SQLAlchemy 2.0
# style usage (optional, but recommended).  We disable
# ``check_same_thread`` on SQLite to allow connections to be shared
# across threads when using the fallback database.
DATABASE_URL = _get_database_url()
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}, future=True
    )
else:
    engine = create_engine(DATABASE_URL, future=True)


# sessionmaker returns a factory which will produce new Session objects
# configured with our engine.  These sessions are not automatically
# committed or flushed; callers must commit when appropriate.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


# Base class for declarative models.
Base = declarative_base()
