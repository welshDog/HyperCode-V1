#!/usr/bin/env python3
"""
HyperCode Database Manager

A tool to manage and evolve the HyperCode research database with validation,
version control, and synchronization capabilities.
"""

import hashlib
import json
import logging
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Optional

import jsonschema

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("database_manager.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


class DatabaseManager:
    def __init__(
        self, db_path: Optional[str] = None, schema_path: Optional[str] = None
    ) -> None:
        """Initialize the database manager with paths to the database and schema."""
        self.base_dir = Path(__file__).parent.parent
        self.db_path = (
            Path(db_path)
            if db_path
            else self.base_dir / "HyperCore-DB" / "hypercode_db.json"
        )
        self.schema_path = (
            Path(schema_path)
            if schema_path
            else self.base_dir / "HyperCore-DB" / "hypercode_schema.json"
        )
        self.backup_dir = self.base_dir / "HyperCore-DB" / "backups"
        self.backup_dir.mkdir(exist_ok=True)

        # Load schema and database
        self.schema = self._load_json_file(self.schema_path, "schema")
        self.db = self._load_json_file(self.db_path, "database")

        # Initialize metrics
        self.metrics = {
            "start_time": datetime.now(timezone.utc).isoformat(),
            "operations": 0,
            "validation_errors": [],
            "backup_created": False,
            "git_commit": self._get_git_commit_hash(),
        }

    def _load_json_file(self, file_path: Path, file_type: str) -> Dict[str, Any]:
        """Load a JSON file with error handling."""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"{file_type.capitalize()} file not found: {file_path}")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in {file_type} file: {e}")
            return {}

    def _get_git_commit_hash(self) -> str:
        """Get the current git commit hash if available."""
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--short", "HEAD"],
                cwd=self.base_dir,
                capture_output=True,
                text=True,
            )
            return result.stdout.strip()
        except Exception:
            return "unknown"

    def validate_database(self) -> bool:
        """Validate the database against the schema."""
        try:
            jsonschema.validate(instance=self.db, schema=self.schema)
            logger.info("✅ Database validation successful")
            return True
        except jsonschema.exceptions.ValidationError as e:
            error_msg = str(e)
            self.metrics["validation_errors"].append(error_msg)
            logger.error(f"❌ Database validation failed: {error_msg}")
            return False

    def create_backup(self) -> Path:
        """Create a timestamped backup of the database."""
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        backup_path = self.backup_dir / f"hypercode_db_{timestamp}.json"

        try:
            with open(backup_path, "w", encoding="utf-8") as f:
                json.dump(self.db, f, indent=2, ensure_ascii=False)

            self.metrics["backup_created"] = True
            logger.info(f"✅ Created backup at: {backup_path}")
            return backup_path
        except Exception as e:
            logger.error(f"❌ Failed to create backup: {e}")
            raise

    def update_database(  # type: ignore
        self, updates: Dict[str, Any], section: Optional[str] = None
    ) -> bool:
        """Update the database with the provided changes."""
        try:
            # Create backup before making changes
            self.create_backup()

            # Update the specified section or merge at root
            target = self.db[section] if section else self.db
            if isinstance(target, dict):
                target.update(updates)
            elif (
                section
            ):  # Only log error if a specific section was intended to be updated
                logger.error(f"Cannot update section {section}: not a dictionary")
                return False

            # Update metadata
            self.db["last_updated"] = datetime.now(timezone.utc).isoformat()
            self.db["version"] = self._bump_version()

            logger.info(f"✅ Updated database (v{self.db['version']})")
            return True
        except Exception as e:
            logger.error(f"❌ Failed to update database: {e}")
            return False

    def _bump_version(self) -> str:
        """Increment the version number following semantic versioning."""
        try:
            version = self.db.get("version", "0.0.0")
            major, minor, patch = map(int, version.split("."))
            return f"{major}.{minor}.{patch + 1}"
        except (ValueError, KeyError):
            return "1.0.0"  # Fallback version

    def save_database(self) -> bool:
        """Save the database to disk."""
        try:
            with open(self.db_path, "w", encoding="utf-8") as f:
                json.dump(self.db, f, indent=2, ensure_ascii=False)
            logger.info(f"💾 Database saved to {self.db_path}")
            return True
        except Exception as e:
            logger.error(f"❌ Failed to save database: {e}")
            return False

    def add_research_entry(
        self, section: str, entry: Dict[str, Any], entry_id: Optional[str] = None
    ) -> bool:
        """Add a new entry to a research section."""
        try:
            if section not in self.db.get("research_data", {}):
                logger.error(f"❌ Invalid section: {section}")
                return False

            # Generate ID if not provided
            if not entry_id:
                entry_id = hashlib.sha256(
                    json.dumps(entry, sort_keys=True).encode()
                ).hexdigest()[:8]

            # Initialize section if it's a dictionary
            if not isinstance(self.db["research_data"][section], dict):
                self.db["research_data"][section] = {}

            # Add entry with timestamp
            entry_metadata = {
                "added": datetime.now(timezone.utc).isoformat(),
                "updated": datetime.now(timezone.utc).isoformat(),
                "source": "database_manager",
                "version": self.db.get("version", "1.0.0"),
            }

            self.db["research_data"][section][entry_id] = {
                **entry,
                "_metadata": entry_metadata,
            }
            logger.info(f"✅ Added entry to '{section}' with ID: {entry_id}")
            return True
        except Exception as e:
            logger.error(f"❌ Failed to add research entry: {e}")
            return False

    def generate_report(self) -> Dict[str, Any]:
        """Generate a report of database metrics and status."""
        return {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "database_version": self.db.get("version", "unknown"),
            "schema_version": self.db.get("schema_version", "unknown"),
            "last_updated": self.db.get("last_updated", "unknown"),
            "record_count": self._count_records(),
            "validation_passed": not bool(self.metrics["validation_errors"]),
            "validation_errors": self.metrics["validation_errors"],
            "backup_created": self.metrics["backup_created"],
            "git_commit": self.metrics["git_commit"],
            "operations": self.metrics["operations"],
        }

    def _count_records(self) -> Dict[str, int]:
        """Count records in each section of the database."""
        counts: Dict[str, int] = {}
        for section, data in self.db.get("research_data", {}).items():
            if isinstance(data, dict):
                counts[section] = len(data)
            elif isinstance(data, list):
                counts[section] = len(data)
            else:
                counts[section] = 1  # Single value
        return counts


def main() -> int:
    """Command-line interface for the Database Manager."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Manage the HyperCode research database"
    )
    subparsers = parser.add_subparsers(dest="command", help="Command to execute")

    # Validate command
    subparsers.add_parser("validate", help="Validate the database against the schema")

    # Update command
    update_parser = subparsers.add_parser(
        "update", help="Update a section of the database"
    )
    update_parser.add_argument(
        "section", help="Section to update (e.g., research_data.core_concept)"
    )
    update_parser.add_argument(
        "--file", required=True, help="JSON file containing updates"
    )

    # Add entry command
    add_parser = subparsers.add_parser("add", help="Add a new research entry")
    add_parser.add_argument(
        "section",
        help="Section to add to (e.g., neurodivergent_features.design_principles)",
    )
    add_parser.add_argument("--id", help="Optional ID for the entry")
    add_parser.add_argument(
        "--file", required=True, help="JSON file containing the entry data"
    )

    # Report command
    _ = subparsers.add_parser("report", help="Generate a database report")

    args = parser.parse_args()

    # Initialize database manager
    try:
        manager = DatabaseManager()
    except Exception as e:
        logger.error(f"Failed to initialize database manager: {e}")
        return 1

    # Execute command
    if args.command == "validate":
        if not manager.validate_database():
            return 1

    elif args.command == "update":
        if not args.file:
            logger.error("Please provide a JSON file with --file")
            return 1

        try:
            with open(args.file, "r", encoding="utf-8") as f:
                updates = json.load(f)

            if manager.update_database(updates, getattr(args, "section", None)):
                if not manager.validate_database():
                    logger.warning(
                        "⚠️  Database updated but validation failed. Rolling back..."
                    )
                    # Rollback would go here
                    return 1
                manager.save_database()
        except Exception as e:
            logger.error(f"Update failed: {e}")
            return 1

    elif args.command == "add":
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                entry = json.load(f)

            if manager.add_research_entry(
                args.section, entry, getattr(args, "id", None)
            ):
                if not manager.validate_database():
                    logger.warning(
                        "⚠️  Entry added but validation failed. Rolling back..."
                    )
                    # Rollback would go here
                    return 1
                manager.save_database()
        except Exception as e:
            logger.error(f"Failed to add entry: {e}")
            return 1

    elif args.command == "report":
        report = manager.generate_report()
        print(json.dumps(report, indent=2))

    else:
        parser.print_help()
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
