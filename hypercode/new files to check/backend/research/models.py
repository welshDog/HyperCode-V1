"""
ORM models for the HyperCode research database.

This module defines the core entities needed to store research
projects, source materials, language versions, tasks, participants,
sessions, low‑level event logs and qualitative feedback.  The
schema is designed to be extensible and normalised so that
different types of analysis can be performed without rewriting
queries each time.

If you add or modify models in this file you will need to create
and run a new Alembic migration to reflect the changes in your
database.  See the repository documentation for instructions on
initialising and running migrations.
"""

from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    Text,
    DateTime,
    ForeignKey,
    JSON,
)
from sqlalchemy.dialects.postgresql import ARRAY

from .db import Base


class Study(Base):
    """Top‑level research study.

    Each research endeavour (for example, "ADHD editing patterns in
    HyperCode v0.3") is represented by a Study.  Studies have
    optional tags for categorisation and can be linked to multiple
    sources, tasks and sessions.
    """

    __tablename__ = "studies"

    id = Column(Integer, primary_key=True)
    slug = Column(Text, unique=True, nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text)
    status = Column(Text, nullable=False, default="planned")
    started_at = Column(DateTime(timezone=True))
    completed_at = Column(DateTime(timezone=True))
    tags = Column(ARRAY(Text), default=list)

    def __repr__(self) -> str:
        return f"<Study slug={self.slug!r} title={self.title!r}>"


class Source(Base):
    """External or internal resource used in a study.

    Examples include published papers, blog posts, videos, design
    documents or spec notes.  The ``storage_path`` points to the
    persisted location of the source material if it exists on disk or
    in object storage.  The optional ``summary`` can store a human or
    machine generated abstract of the resource.
    """

    __tablename__ = "sources"

    id = Column(Integer, primary_key=True)
    study_id = Column(Integer, ForeignKey("studies.id", ondelete="SET NULL"))
    title = Column(Text, nullable=False)
    kind = Column(Text, nullable=False)
    url = Column(Text)
    storage_path = Column(Text)
    summary = Column(Text)
    imported_at = Column(DateTime(timezone=True), default=datetime.utcnow)

    # embedding column can be added later if using pgvector
    # from sqlalchemy.dialects.postgresql import VECTOR
    # embedding = Column(VECTOR(1536))

    def __repr__(self) -> str:
        return f"<Source title={self.title!r} kind={self.kind!r}>"


class LanguageVersion(Base):
    """Version of the HyperCode language.

    Tracks semantic changes and meta information about a particular
    version of HyperCode.  The optional ``spec_source_id`` can be
    linked to a Source row representing the language specification.
    """

    __tablename__ = "language_versions"

    id = Column(Integer, primary_key=True)
    version = Column(Text, unique=True, nullable=False)
    codename = Column(Text)
    released_at = Column(DateTime(timezone=True))
    changelog = Column(Text)
    spec_source_id = Column(Integer, ForeignKey("sources.id"))

    def __repr__(self) -> str:
        return f"<LanguageVersion version={self.version!r}>"


class Task(Base):
    """A coding task or challenge used in experiments.

    Tasks describe the problem statement and any relevant metadata so
    that results can be compared across participants and language
    versions.
    """

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    slug = Column(Text, unique=True, nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    difficulty = Column(Text)
    cognitive_focus = Column(Text)
    tags = Column(ARRAY(Text), default=list)

    def __repr__(self) -> str:
        return f"<Task slug={self.slug!r} title={self.title!r}>"


class Participant(Base):
    """An anonymised participant in the study.

    Participants are keyed by a code rather than a real identity to
    preserve privacy.  Additional demographic information could be
    stored here if needed (for example, ND profile flags).
    """

    __tablename__ = "participants"

    id = Column(Integer, primary_key=True)
    anon_code = Column(Text, unique=True, nullable=False)
    profile_notes = Column(Text)
    nd_profile = Column(ARRAY(Text), default=list)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Participant anon_code={self.anon_code!r}>"


class Session(Base):
    """A single coding session of a participant performing a task.

    A session links together a study, participant, task and language
    version.  It captures metadata about the environment and an
    optional free form note field for the researcher.
    """

    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True)
    study_id = Column(Integer, ForeignKey("studies.id"))
    participant_id = Column(Integer, ForeignKey("participants.id"))
    task_id = Column(Integer, ForeignKey("tasks.id"))
    language_version_id = Column(Integer, ForeignKey("language_versions.id"))

    started_at = Column(DateTime(timezone=True), nullable=False)
    ended_at = Column(DateTime(timezone=True))
    environment = Column(JSON, default=dict)
    notes = Column(Text)

    def __repr__(self) -> str:
        return (
            f"<Session id={self.id} participant_id={self.participant_id}"
            f" task_id={self.task_id} language_version_id={self.language_version_id}>"
        )


class Event(Base):
    """Low‑level interaction within a session.

    Events capture keystrokes, runs, errors, completions or any
    arbitrary interaction that occurs during a coding session.  The
    ``data`` column stores a flexible payload to accommodate
    different kinds of events.
    """

    __tablename__ = "events"

    id = Column(BigInteger, primary_key=True)
    session_id = Column(Integer, ForeignKey("sessions.id", ondelete="CASCADE"))
    ts = Column(DateTime(timezone=True), nullable=False)
    event_type = Column(Text, nullable=False)
    data = Column(JSON, default=dict)

    def __repr__(self) -> str:
        return (
            f"<Event id={self.id} session_id={self.session_id} type={self.event_type}>"
        )


class Feedback(Base):
    """Qualitative and quantitative feedback for a session.

    Stores ratings for flow, clarity and frustration along with
    free‑form comments.  Additional embedding support can be added
    later for semantic searches.
    """

    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("sessions.id", ondelete="CASCADE"))
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    rating_flow = Column(Integer)
    rating_clarity = Column(Integer)
    rating_frustration = Column(Integer)
    free_text = Column(Text)

    # embedding column can be added later
    # from sqlalchemy.dialects.postgresql import VECTOR
    # embedding = Column(VECTOR(1536))

    def __repr__(self) -> str:
        return f"<Feedback id={self.id} session_id={self.session_id}>"
