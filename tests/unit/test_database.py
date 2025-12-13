"""
Test script for Hypercode database operations.
"""

import time

from hypercode_db import HypercodeDB


def test_database_loading():
    """Test loading the database and basic queries."""
    print("Testing Hypercode Database...")

    # Time the database loading
    start_time = time.time()
    try:
        db = HypercodeDB("HYPER_DATABASE.json")
        load_time = time.time() - start_time
        print(f"[OK] Database loaded successfully in {load_time:.2f} seconds")

        # Get entity counts by type
        print("\nEntity counts by type:")
        entity_types = db.by_type.keys()
        for etype in sorted(entity_types):
            count = len(db.by_type[etype])
            print(f"- {etype}: {count}")

        # Get some sample entities
        if db.entities:
            print("\nSample entities:")
            for i, entity in enumerate(db.entities[:3], 1):
                print(
                    f"{i}. {entity.type} '{entity.name}' in {entity.file}:{entity.lineno}"
                )

        # Test specific queries
        print("\nTesting specific queries:")

        # Get all functions
        functions = db.get_entities_by_type("function")
        if functions:
            print(f"Found {len(functions)} functions")
            if len(functions) > 0:
                print(f"  First function: {functions[0].name} in {functions[0].file}")

        # Get all classes
        classes = db.get_entities_by_type("class")
        if classes:
            print(f"Found {len(classes)} classes")
            if len(classes) > 0:
                print(f"  First class: {classes[0].name} in {classes[0].file}")
                if hasattr(classes[0], "methods") and classes[0].methods:
                    print(
                        f"    Methods: {', '.join(classes[0].methods[:3])}{'...' if len(classes[0].methods) > 3 else ''}"
                    )

        return True

    except Exception as e:
        print(f"[ERROR] Error loading database: {str(e)}")
        import traceback

        traceback.print_exc()
        return False


if __name__ == "__main__":
    test_database_loading()
