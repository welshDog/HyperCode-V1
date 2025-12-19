"""
Database Health Check and Fix Script

This script analyzes the Hypercode database for common issues and applies fixes.
It includes validation, documentation improvements, and data consistency checks.
"""

import datetime
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List

# Type aliases
EntityData = Dict[str, any]


@dataclass
class FixedCodeEntity:
    """Enhanced version of CodeEntity with validation and better documentation.

    Attributes:
        id: Unique identifier for the entity
        type: Type of entity (e.g., 'class', 'function')
        name: Name of the entity
        file: Source file path (relative to project root)
        lineno: Line number in the source file (1-based)
        methods: List of method names (for classes)
        docstring: Documentation string for the entity
        args: Function arguments (for functions)
        has_test: Whether the entity has associated tests
    """

    id: str
    type: str
    name: str
    file: str
    lineno: int
    methods: List[str] = field(default_factory=list)
    docstring: str = ""
    args: List[Dict[str, str]] = field(default_factory=list)
    has_test: bool = False
    # Allow additional fields that might be in the database
    extra_fields: Dict[str, any] = field(default_factory=dict)

    def __post_init__(self):
        """Validate entity data after initialization."""
        # Store any extra fields not in the class definition
        self.extra_fields = {}
        for key, value in self.__dict__.items():
            if not hasattr(self, key) and not key.startswith("_"):
                self.extra_fields[key] = value

        self._validate_required_fields()
        self._normalize_fields()
        self._validate_field_types()
        self._clean_docstring()

    def _validate_required_fields(self):
        """Ensure all required fields have values."""
        required_fields = ["id", "type", "name", "file", "lineno"]
        for field_name in required_fields:
            if not getattr(self, field_name, None):
                raise ValueError(f"Missing required field: {field_name}")

    def _validate_field_types(self):
        """Check that all fields have the correct types."""
        if not isinstance(self.methods, list):
            raise TypeError("'methods' must be a list")
        if not isinstance(self.docstring, str):
            raise TypeError("'docstring' must be a string")
        if not isinstance(self.lineno, int) or self.lineno < 1:
            raise ValueError("'lineno' must be a positive integer")
        if not isinstance(self.args, list):
            raise TypeError("'args' must be a list")
        if not isinstance(self.has_test, bool):
            raise TypeError("'has_test' must be a boolean")

    def _normalize_fields(self):
        """Normalize field values."""
        self.id = str(self.id).strip()
        self.type = str(self.type).strip().lower()
        self.name = str(self.name).strip()
        self.file = str(self.file).replace("\\", "/")  # Normalize path separators
        self.lineno = int(self.lineno)

        # Ensure methods is a list of strings
        if not hasattr(self, "methods") or not isinstance(self.methods, list):
            self.methods = []
        self.methods = [str(m).strip() for m in self.methods if m and str(m).strip()]

        # Ensure docstring is a string
        if not hasattr(self, "docstring") or not isinstance(self.docstring, str):
            self.docstring = ""

        # Ensure args is a list of dictionaries
        if not hasattr(self, "args") or not isinstance(self.args, list):
            self.args = []
        self.args = [dict(a) for a in self.args if a and isinstance(a, dict)]

        # Ensure has_test is a boolean
        if not hasattr(self, "has_test") or not isinstance(self.has_test, bool):
            self.has_test = False

    def _clean_docstring(self):
        """Clean and standardize the docstring."""
        if not self.docstring:
            return

        # Remove extra whitespace and normalize line endings
        self.docstring = "\n".join(
            line.strip() for line in self.docstring.splitlines()
        ).strip()

        # Ensure docstring ends with a period
        if self.docstring and not self.docstring.endswith("."):
            self.docstring += "."

    def to_dict(self) -> dict:
        """Convert entity to dictionary for JSON serialization."""
        result = {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "file": self.file,
            "lineno": self.lineno,
            "methods": self.methods,
            "docstring": self.docstring,
            "args": self.args,
            "has_test": self.has_test,
        }
        # Add any extra fields
        result.update(self.extra_fields)
        return result


class DatabaseFixer:
    """Handles fixing and validating the Hypercode database."""

    def __init__(self, db_path: str):
        """Initialize with path to the database file."""
        self.db_path = Path(db_path)
        self.entities: List[FixedCodeEntity] = []
        self.issues: List[dict] = []
        self.stats = {
            "total_entities": 0,
            "fixed_entities": 0,
            "invalid_entities": 0,
            "docstrings_added": 0,
            "methods_fixed": 0,
            "validation_errors": 0,
        }

    def load_database(self) -> bool:
        """Load and validate the database."""
        try:
            with open(self.db_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, dict) or "entities" not in data:
                raise ValueError("Invalid database format: missing 'entities' key")

            self.stats["total_entities"] = len(data["entities"])

            # Process each entity
            for idx, entity_data in enumerate(data["entities"], 1):
                try:
                    entity = FixedCodeEntity(**entity_data)
                    self.entities.append(entity)
                    self._check_for_issues(entity, idx)
                except Exception as e:
                    self.stats["validation_errors"] += 1
                    self.issues.append(
                        {
                            "type": "validation_error",
                            "entity": entity_data.get("name", f"entity_{idx}"),
                            "file": entity_data.get("file", "unknown"),
                            "error": str(e),
                            "data": entity_data,
                        }
                    )

            return True

        except Exception as e:
            self.issues.append(
                {"type": "load_error", "error": f"Failed to load database: {str(e)}"}
            )
            return False

    def _check_for_issues(self, entity: FixedCodeEntity, idx: int):
        """Check an entity for common issues."""
        # Check for missing docstring
        if not entity.docstring.strip():
            self.issues.append(
                {
                    "type": "missing_docstring",
                    "entity": entity.name,
                    "file": entity.file,
                    "lineno": entity.lineno,
                    "severity": "warning",
                }
            )

        # Check for potentially problematic method names
        for method in entity.methods:
            if not method.strip():
                self.issues.append(
                    {
                        "type": "empty_method_name",
                        "entity": entity.name,
                        "file": entity.file,
                        "lineno": entity.lineno,
                        "severity": "error",
                    }
                )

    def fix_issues(self):
        """Fix common issues in the database."""
        for entity in self.entities:
            try:
                # Add basic docstring if missing
                if not entity.docstring.strip():
                    entity.docstring = f"{entity.type} {entity.name}"
                    self.stats["docstrings_added"] += 1

                # Clean up methods list
                original_methods = len(entity.methods)
                entity.methods = [m for m in entity.methods if m.strip()]
                if len(entity.methods) != original_methods:
                    self.stats["methods_fixed"] += 1

                self.stats["fixed_entities"] += 1

            except Exception as e:
                self.stats["validation_errors"] += 1
                self.issues.append(
                    {
                        "type": "fix_error",
                        "entity": entity.name,
                        "file": entity.file,
                        "error": str(e),
                    }
                )

    def save_database(self, output_path: str = None) -> bool:
        """Save the fixed database to a file."""
        if not output_path:
            output_path = str(self.db_path).replace(".json", "_fixed.json")

        try:
            data = {
                "entities": [entity.to_dict() for entity in self.entities],
                "metadata": {
                    "fixed_by": "database_fixer.py",
                    "fix_timestamp": datetime.datetime.now().isoformat(),
                    "stats": self.stats,
                },
            }

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            return True

        except Exception as e:
            self.issues.append(
                {"type": "save_error", "error": f"Failed to save database: {str(e)}"}
            )
            return False

    def generate_report(self) -> str:
        """Generate a report of issues and fixes."""
        report = [
            "=" * 80,
            "HYPERCODE DATABASE HEALTH REPORT",
            "=" * 80,
            f"Database: {self.db_path}",
            f"Total entities: {self.stats['total_entities']}",
            f"Fixed entities: {self.stats['fixed_entities']}",
            f"Validation errors: {self.stats['validation_errors']}",
            f"Docstrings added: {self.stats['docstrings_added']}",
            f"Methods fixed: {self.stats['methods_fixed']}",
            "\nISSUES FOUND:",
            "-" * 40,
        ]

        # Group issues by type
        issues_by_type = {}
        for issue in self.issues:
            issue_type = issue.get("type", "unknown")
            if issue_type not in issues_by_type:
                issues_by_type[issue_type] = []
            issues_by_type[issue_type].append(issue)

        # Add issues to report
        for issue_type, items in issues_by_type.items():
            report.append(f"{issue_type.upper()} ({len(items)}):")
            for item in items[:10]:  # Show first 10 of each type
                if "entity" in item:
                    report.append(
                        f"  - {item['entity']} in {item.get('file', 'unknown')}"
                    )
                    if "error" in item:
                        report.append(f"    Error: {item['error']}")
            if len(items) > 10:
                report.append(f"  ... and {len(items) - 10} more")
            report.append("")

        return "\n".join(report)


def main():
    """Main function to run the database fixer."""
    import sys

    # Add current directory to path for imports
    sys.path.insert(0, str(Path(__file__).parent))

    # Set up paths
    db_path = Path("HYPER_DATABASE.json")
    if not db_path.exists():
        print(f"Error: Database file not found at {db_path}")
        return 1

    # Initialize fixer
    fixer = DatabaseFixer(db_path)

    # Load and validate database
    print("Loading database...")
    if not fixer.load_database():
        print("Failed to load database. Check the error messages above.")
        return 1

    # Print initial stats
    print(f"\nLoaded {len(fixer.entities)} entities")
    print(f"Found {len(fixer.issues)} potential issues")

    # Fix issues
    print("\nFixing issues...")
    fixer.fix_issues()

    # Save fixed database
    output_file = (
        f"HYPER_DATABASE_fixed_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )
    if fixer.save_database(output_file):
        print(f"\nSaved fixed database to: {output_file}")

    # Generate and save report
    report = fixer.generate_report()
    report_file = f"database_health_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write(report)

    print("\n" + "=" * 60)
    print(report)
    print("=" * 60)
    print(f"\nFull report saved to: {report_file}")

    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
