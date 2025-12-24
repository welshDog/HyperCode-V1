import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional


@dataclass
class CodeEntity:
    """Represents a code entity in the database.

    This can represent various types of entities including research content, code elements, etc.
    The content field is a flexible container for entity-specific data.
    """

    id: str
    type: str
    name: str = ""
    file: str = ""
    lineno: int = 0
    methods: List[str] = None
    docstring: str = ""
    content: dict = None

    def __post_init__(self):
        """Initialize default values for mutable fields."""
        if self.methods is None:
            self.methods = []
        if self.content is None:
            self.content = {}


class HypercodeDB:
    """In-memory database for Hypercode project analysis.

    This class provides efficient querying and analysis of code entities
    loaded from a JSON database file.
    """

    def __init__(self, db_path: str = "HYPER_DATABASE.json") -> None:
        """Initialize the database with the given JSON file.

        Args:
            db_path: Path to the JSON database file
        """
        self.entities: List[CodeEntity] = []
        self.by_type: Dict[str, List[CodeEntity]] = defaultdict(list)
        self.by_file: Dict[str, List[CodeEntity]] = defaultdict(list)
        self._load_database(db_path)

    def _load_database(self, db_path: str) -> None:
        """Load the database from a JSON file.

        Args:
            db_path: Path to the JSON database file
        """
        try:
            with open(db_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            if not isinstance(data, dict) or "entities" not in data:
                raise ValueError(
                    f"Invalid database format in '{db_path}'. "
                    "Expected a dictionary with 'entities' key."
                )

            for i, entity_data in enumerate(data.get("entities", []), 1):
                try:
                    entity = CodeEntity(
                        id=entity_data.get("id", ""),
                        type=entity_data.get("type", ""),
                        name=entity_data.get("name", ""),
                        file=entity_data.get("file", ""),
                        lineno=entity_data.get("lineno", 0),
                        docstring=entity_data.get("docstring", ""),
                        methods=entity_data.get("methods", []),
                        content=entity_data.get("content", {}),
                    )
                    self.entities.append(entity)
                    self.by_type[entity.type].append(entity)
                    self.by_file[entity.file].append(entity)
                except Exception as e:
                    print(
                        f"Warning: Failed to load entity #{i} from {db_path}: {str(e)}"
                    )
                    continue

        except FileNotFoundError as e:
            raise FileNotFoundError(f"Database file not found: {db_path}") from e
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f"Invalid JSON in database file '{db_path}': {str(e)}", e.doc, e.pos
            ) from e
        except Exception as e:
            raise RuntimeError(
                f"Failed to load database from {db_path}: {str(e)}"
            ) from e

    def get_entities_by_type(self, entity_type: str) -> List[CodeEntity]:
        """Get all entities of a specific type.

        Args:
            entity_type: The type of entities to retrieve (e.g., 'function', 'class')

        Returns:
            List of matching CodeEntity objects
        """
        return self.by_type.get(entity_type, []).copy()

    def get_entities_in_file(self, file_path: str) -> List[CodeEntity]:
        """Get all entities in a specific file.

        Args:
            file_path: Path to the file

        Returns:
            List of CodeEntity objects in the file
        """
        return self.by_file.get(file_path, []).copy()


def print_analysis(db: HypercodeDB) -> None:
    """Print a detailed analysis of the codebase.

    Args:
        db: Initialized HypercodeDB instance
    """
    if not isinstance(db, HypercodeDB):
        raise TypeError("Expected db to be an instance of HypercodeDB")
    print("\n" + "=" * 50)
    print("HYPERCODE CODEBASE ANALYSIS")
    print("=" * 50)


# Example usage
if __name__ == "__main__":
    # Initialize the database
    print("Loading database...")
    db = HypercodeDB("HYPER_DATABASE.json")

    # Run the analysis
    print_analysis(db)

    # Interactive search example
    print("\n[SEARCH] Try searching for entities (e.g., 'test', 'parse', 'handle'):")
    while True:
        search_term = input("\nSearch term (or 'quit' to exit): ").strip()
        if search_term.lower() in ("quit", "exit", "q"):
            break

        results = db.search_by_name(search_term)
        print(f"\nFound {len(results)} matching entities:")
        for i, entity in enumerate(results[:5], 1):
            doc_preview = f" - {entity.docstring[:50]}..." if entity.docstring else ""
            print(
                f"  {i}. {entity.type.title()}: {entity.name} (in {entity.file}:{entity.lineno}){doc_preview}"
            )

        if len(results) > 5:
            print(f"  ... and {len(results) - 5} more results")
        elif not results:
            print("  No results found. Try a different search term.")
