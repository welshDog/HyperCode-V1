import os
import sys
import time
from pathlib import Path

import pytest

# Add the project root to Python path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Now import the module
from hypercode_db import HypercodeDB

# Get the path to the database file
DB_PATH = Path(__file__).parent.parent.parent / "hypercode-database.json"


@pytest.mark.skipif(not DB_PATH.exists(), reason=f"Database file not found: {DB_PATH}")
def test_database_loading():
    print(f"Testing Hypercode Database with file: {DB_PATH}")
    start_time = time.time()
    try:
        db = HypercodeDB(str(DB_PATH))
        load_time = time.time() - start_time
        print(f"[OK] Database loaded successfully in {load_time:.2f} seconds")

        # Test basic queries
        research_entities = db.get_entities_by_type("research")
        assert len(research_entities) > 0, "Expected to find research entities"

        print("[OK] Basic queries successful")

    except Exception as e:
        print(f"[ERROR] Error loading database: {str(e)}")
        import traceback

        traceback.print_exc()
        assert False, f"Test failed with exception: {str(e)}"


if __name__ == "__main__":
    test_database_loading()
