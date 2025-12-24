# hypercode_manager_enhanced.py
import json
import logging
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum, auto
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional, TypedDict, Union

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class VersionChangeType(Enum):
    """Type of version change for semantic versioning."""

    PATCH = auto()
    MINOR = auto()
    MAJOR = auto()


class FieldMetadata(TypedDict):
    """Metadata for tracking field changes."""

    added_in: str
    last_updated: str
    deprecated: bool
    deprecated_in: Optional[str]
    description: Optional[str]


class HyperCodeDataManager:
    """
    Manages HyperCode project data with semantic versioning and validation.

    Features:
    - Semantic versioning (MAJOR.MINOR.PATCH)
    - Schema validation
    - Change tracking
    - Data integrity checks
    - Automatic backups
    """

    def __init__(
        self,
        data_file: Optional[Union[str, Path]] = None,
        schema_file: Optional[Union[str, Path]] = None,
        auto_save: bool = False,
        create_backups: bool = True,
    ):
        """
        Initialize the HyperCodeDataManager.

        Args:
            data_file: Path to the JSON data file
            schema_file: Path to the JSON schema file
            auto_save: Automatically save changes
            create_backups: Create backup files before saving
        """
        self.data_file = Path(data_file) if data_file else None
        self.schema_file = Path(schema_file) if schema_file else None
        self.auto_save = auto_save
        self.create_backups = create_backups
        self._metadata: Dict[str, FieldMetadata] = {}

        # Initialize with default structure
        self.data = {
            "schema_version": "0.1.0",
            "last_updated": self._get_iso_timestamp(),
            "metadata": {
                "created": self._get_iso_timestamp(),
                "modified": self._get_iso_timestamp(),
            },
        }

        # Load existing data if file exists
        if self.data_file and self.data_file.exists():
            self.load()
        elif self.auto_save and self.data_file:
            self.save()

    def _get_iso_timestamp(self) -> str:
        """Get current timestamp in ISO 8601 format."""
        return datetime.now(timezone.utc).isoformat()

    def _create_backup(self) -> Optional[Path]:
        """Create a backup of the current data file."""
        if not self.data_file or not self.data_file.exists():
            return None

        backup_file = self.data_file.with_suffix(
            f".{int(datetime.now().timestamp())}.bak"
        )
        try:
            import shutil

            shutil.copy2(self.data_file, backup_file)
            return backup_file
        except Exception as e:
            logger.warning(f"Failed to create backup: {e}")
            return None

    def save(self, path: Optional[Union[str, Path]] = None) -> bool:
        """Save data to file with optional backup."""
        save_path = Path(path) if path else self.data_file
        if not save_path:
            raise ValueError("No save path specified")

        try:
            # Create directory if it doesn't exist
            save_path.parent.mkdir(parents=True, exist_ok=True)

            # Create backup if enabled
            if self.create_backups and save_path.exists():
                self._create_backup()

            # Save data
            with open(save_path, "w", encoding="utf-8") as f:
                json.dump(self.data, f, indent=2, ensure_ascii=False)

            logger.info(f"Data saved to {save_path}")
            return True

        except Exception as e:
            logger.error(f"Error saving to {save_path}: {e}")
            raise

    def load(self, path: Optional[Union[str, Path]] = None) -> bool:
        """Load data from file with validation."""
        load_path = Path(path) if path else self.data_file
        if not load_path or not load_path.exists():
            raise FileNotFoundError(f"Data file not found: {load_path}")

        try:
            with open(load_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Basic validation
            if not isinstance(data, dict):
                raise ValueError("Invalid data format: expected dictionary")

            if "schema_version" not in data:
                logger.warning("No schema_version found in data")

            self.data = data
            self.data_file = load_path
            logger.info(f"Data loaded from {load_path}")
            return True

        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in {load_path}: {e}")
            raise
        except Exception as e:
            logger.error(f"Error loading from {load_path}: {e}")
            raise

    def validate(self) -> bool:
        """Validate data against schema if schema_file is set."""
        if not self.schema_file:
            logger.warning("No schema file specified for validation")
            return False

        try:
            import jsonschema
            from jsonschema import validate as js_validate

            if not self.schema_file.exists():
                logger.error(f"Schema file not found: {self.schema_file}")
                return False

            with open(self.schema_file, "r", encoding="utf-8") as f:
                schema = json.load(f)

            js_validate(instance=self.data, schema=schema)
            logger.info("Data validation successful")
            return True

        except ImportError:
            logger.error(
                "jsonschema package not installed. Install with: pip install jsonschema"
            )
            return False
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in schema file: {e}")
            return False
        except jsonschema.ValidationError as e:
            logger.error(f"Validation error: {e}")
            return False
        except Exception as e:
            logger.error(f"Error during validation: {e}")
            return False

    def update_field(
        self,
        path: str,
        value: Any,
        change_type: Union[VersionChangeType, str] = VersionChangeType.PATCH,
        description: Optional[str] = None,
    ) -> bool:
        """Update a field with version tracking."""
        if not path:
            raise ValueError("Path cannot be empty")

        # Handle string change_type
        if isinstance(change_type, str):
            try:
                change_type = VersionChangeType[change_type.upper()]
            except KeyError:
                raise ValueError(f"Invalid change_type: {change_type}")

        # Update the data structure
        keys = path.split(".")
        current = self.data

        for key in keys[:-1]:
            if key not in current or not isinstance(current[key], dict):
                current[key] = {}
            current = current[key]

        # Track changes
        old_value = current.get(keys[-1])
        current[keys[-1]] = value

        # Update metadata
        field_path = path
        if field_path not in self._metadata:
            self._metadata[field_path] = {
                "added_in": self.data["schema_version"],
                "last_updated": self._get_iso_timestamp(),
                "deprecated": False,
                "deprecated_in": None,
                "description": description,
            }
        else:
            self._metadata[field_path]["last_updated"] = self._get_iso_timestamp()
            if description:
                self._metadata[field_path]["description"] = description

        # Update version
        self._increment_version(change_type)

        logger.info(f"Updated field '{path}': {old_value} -> {value}")
        return True

    def _increment_version(self, change_type: VersionChangeType) -> str:
        """Increment the version based on change type."""
        if not isinstance(change_type, VersionChangeType):
            raise ValueError("Invalid change type")

        major, minor, patch = map(int, self.data["schema_version"].split("."))

        if change_type == VersionChangeType.MAJOR:
            major += 1
            minor = 0
            patch = 0
        elif change_type == VersionChangeType.MINOR:
            minor += 1
            patch = 0
        else:  # PATCH
            patch += 1

        new_version = f"{major}.{minor}.{patch}"
        self.data["schema_version"] = new_version
        self.data["last_updated"] = self._get_iso_timestamp()

        logger.info(
            f"Version updated to {new_version} ({change_type.name.lower()} change)"
        )
        return new_version

    def get_field_metadata(self, path: str) -> Optional[FieldMetadata]:
        """Get metadata for a field."""
        return self._metadata.get(path)

    def deprecate_field(self, path: str, message: str = "") -> bool:
        """Mark a field as deprecated."""
        if path not in self._metadata:
            self._metadata[path] = {
                "added_in": self.data["schema_version"],
                "last_updated": self._get_iso_timestamp(),
                "deprecated": True,
                "deprecated_in": self.data["schema_version"],
                "description": message
                or f"Deprecated in {self.data['schema_version']}",
            }
        else:
            self._metadata[path].update(
                {
                    "deprecated": True,
                    "deprecated_in": self.data["schema_version"],
                    "description": message
                    or self._metadata[path].get("description", ""),
                }
            )

        logger.warning(f"Deprecated field '{path}': {message}")
        return True

    def get_changelog(self) -> Dict[str, List[Dict[str, Any]]]:
        """Generate a changelog of all changes."""
        changes = {"added": [], "modified": [], "deprecated": []}

        for path, meta in self._metadata.items():
            change = {
                "field": path,
                "added_in": meta["added_in"],
                "last_updated": meta["last_updated"],
                "description": meta.get("description", ""),
            }

            if meta.get("deprecated", False):
                change["deprecated_in"] = meta["deprecated_in"]
                changes["deprecated"].append(change)
            elif meta["added_in"] == self.data["schema_version"]:
                changes["added"].append(change)
            else:
                changes["modified"].append(change)

        return changes

    def export_schema(self) -> Dict[str, Any]:
        """Export current data structure as a JSON Schema."""
        return {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "title": "HyperCode Data Schema",
            "description": "Auto-generated schema from HyperCode data",
            "type": "object",
            "properties": {
                "schema_version": {
                    "type": "string",
                    "description": "Schema version in semver format",
                },
                "last_updated": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Last update timestamp",
                },
                "metadata": {
                    "type": "object",
                    "properties": {
                        "created": {"type": "string", "format": "date-time"},
                        "modified": {"type": "string", "format": "date-time"},
                    },
                },
            },
            "required": ["schema_version", "last_updated", "metadata"],
        }
