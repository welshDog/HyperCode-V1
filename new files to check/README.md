# HyperCode Research Module

This repository contains a lightweight implementation of the
``research`` module described in previous conversations.  It is
intended to serve as a foundation for logging and analysing
experiments conducted with the HyperCode language.

## Structure

The key files are under `backend/research`:

- `db.py` – sets up a SQLAlchemy engine and session factory.  The
  database URL is read from the `RESEARCH_DATABASE_URL` environment
  variable.  If unset, a local SQLite file `hypercode_research.db`
  in the project root will be used instead.  This makes it
  straightforward to run the module without any external
  dependencies.
- `models.py` – defines ORM models for Studies, Sources, Language
  Versions, Tasks, Participants, Sessions, Events and Feedback.  It
  follows the schema discussed earlier, including flexible JSON
  payloads for event data and array fields for tags and ND profiles.
- `scripts/seed_basic_data.py` – a small script to create the
  database tables and populate them with a starter study and
  language version.  Run this at least once to verify that your
  environment is configured correctly.
- `scripts/import_sources_from_folder.py` – a utility for bulk
  loading files (PDFs, markdown, HTML) into the `sources` table.
  The script infers the ``kind`` based on file extension and
  preserves the original filename in the database.

## Getting started

1. **Install dependencies** (for example in a virtualenv):

   ```bash
   pip install sqlalchemy psycopg2-binary  # for PostgreSQL support
   ```

2. **Set up a database**:

   Define the `RESEARCH_DATABASE_URL` environment variable.  For
   PostgreSQL:

   ```bash
   export RESEARCH_DATABASE_URL=postgresql+psycopg2://user:password@host:port/dbname
   ```

   If the variable is not set then the module will use an in–file
   SQLite database (`sqlite:///hypercode_research.db`).  This is
   useful for local experimentation.

3. **Create the tables and seed some data**:

   Run the seed script:

   ```bash
   python hypercode/backend/research/scripts/seed_basic_data.py
   ```

   This will create all tables (if they do not already exist) and
   insert a starter Study and LanguageVersion.  You can inspect
   these by opening the database with your favourite SQL tool.

4. **Import your sources**:

   Put some PDFs or markdown files into a folder (for example
   `data/research_sources`) and run:

   ```bash
   python hypercode/backend/research/scripts/import_sources_from_folder.py data/research_sources
   ```

   Each file will be registered as a ``Source`` in the database.

5. **Integrate into your application**:

   Import the models and session factory from `hypercode.backend.research`
   to create new studies, sessions, events and feedback records from
   your HyperCode playground or other services.  See the docstrings
   in `models.py` for more details.

## Next steps

This module can be extended in several directions:

- Integrate [pgvector](https://github.com/pgvector/pgvector) by
  adding embedding columns to the `sources` and `feedback` tables
  (see commented lines in `models.py`).  Use a background job to
  compute embeddings.
- Wrap the ORM with a small API (for example with FastAPI) to
  decouple research logging from the core HyperCode runtime.
- Add more sophisticated data importers (for example to parse
  transcripts or logs) and exporters (for example to produce reports
  or dashboards).

Feel free to adapt and evolve this structure to suit the needs of
your research.  The goal is to capture structured data about
HyperCode experiments in a way that supports rigorous analysis and
continuous improvement.