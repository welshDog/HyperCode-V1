"""
Import research sources from a folder into the database.

This script scans a directory for files and registers each file as a
``Source`` in the database.  It infers the ``kind`` based on file
extension and preserves the relative path so that the file can be
retrieved later.  Existing entries are not updated.

Usage::

    python hypercode/backend/research/scripts/import_sources_from_folder.py /path/to/data

The ``RESEARCH_DATABASE_URL`` environment variable should point to
your database; otherwise SQLite will be used.
"""

import sys
from pathlib import Path
from datetime import datetime

from hypercode.backend.research import SessionLocal
from hypercode.backend.research.models import Source


def infer_kind(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in {".pdf"}:
        return "paper"
    if ext in {".md", ".txt"}:
        return "note"
    if ext in {".html", ".htm"}:
        return "blog"
    return "other"


def main(data_dir: Path) -> None:
    if not data_dir.is_dir():
        raise SystemExit(f"{data_dir} is not a directory")

    db = SessionLocal()
    try:
        for path in data_dir.iterdir():
            if not path.is_file():
                continue
            title = path.stem.replace("_", " ")
            kind = infer_kind(path)
            storage_path = str(path)

            # skip if a source with the same storage_path already exists
            if db.query(Source).filter_by(storage_path=storage_path).first():
                continue

            src = Source(
                title=title,
                kind=kind,
                storage_path=storage_path,
                imported_at=datetime.utcnow(),
            )
            db.add(src)

        db.commit()
        print(f"Imported sources from {data_dir}")
    finally:
        db.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python import_sources_from_folder.py <directory>")
        raise SystemExit(1)
    main(Path(sys.argv[1]))
