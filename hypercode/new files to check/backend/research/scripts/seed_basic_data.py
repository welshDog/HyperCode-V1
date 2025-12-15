"""
Seed the research database with initial data.

This script is intended to be run from the command line during
development to populate the database with a minimal set of entries.
It creates a default study and a language version so that the
schema can be inspected and tested without requiring manual
interaction through the API.

Usage::

    python hypercode/backend/research/scripts/seed_basic_data.py

Before running this script ensure that the environment variable
``RESEARCH_DATABASE_URL`` points to a writable database.  If the
variable isn't set then the script will fall back to using a
local SQLite file ``hypercode_research.db`` in the working directory.
"""

from datetime import datetime
from hypercode.backend.research import Base, SessionLocal
from hypercode.backend.research.models import Study, LanguageVersion


def main() -> None:
    # Create the database tables.  In a real deployment you'll
    # typically use Alembic migrations instead of calling
    # ``create_all`` directly, but this is convenient for local
    # development.
    from hypercode.backend.research.db import engine

    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        # Add a sample study if none exist
        if not db.query(Study).first():
            study = Study(
                slug="nd-devs-hypercode-v0-1",
                title="Neurodivergent Developers & Early HyperCode",
                description="Initial research on ADHD/dyslexic devs using early HyperCode syntax.",
                status="running",
                tags=["adhd", "dyslexia", "language-design"],
                started_at=datetime.utcnow(),
            )
            db.add(study)
        # Add a sample language version if none exist
        if not db.query(LanguageVersion).first():
            lv = LanguageVersion(
                version="0.1.0",
                codename="Proto-Emoji",
                changelog="First prototype with emoji-native BNF.",
                released_at=datetime.utcnow(),
            )
            db.add(lv)

        db.commit()
        print("Seed complete.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
