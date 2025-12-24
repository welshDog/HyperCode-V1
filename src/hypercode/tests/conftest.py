"""pytest configuration and fixtures for testing."""

import json
import os
from pathlib import Path

import pytest

# Add the project root to the Python path
PROJECT_ROOT = Path(__file__).parent.parent
os.environ["PYTHONPATH"] = str(PROJECT_ROOT)

# Create test data directory if it doesn't exist
TEST_DATA_DIR = PROJECT_ROOT / "tests" / "test_data"
TEST_DATA_DIR.mkdir(exist_ok=True)


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Set up the test environment."""
    # Create a test database file if it doesn't exist
    test_db_path = TEST_DATA_DIR / "test_db.json"
    if not test_db_path.exists():
        test_data = {
            "entities": [
                {
                    "id": "1",
                    "type": "research",
                    "name": "Test Research",
                    "file": "test_file.py",
                    "lineno": 10,
                    "docstring": "Test docstring",
                    "methods": ["method1", "method2"],
                    "content": {"key": "value"},
                },
                {
                    "id": "2",
                    "type": "code",
                    "name": "test_function",
                    "file": "test_file.py",
                    "lineno": 20,
                    "docstring": "Test function",
                    "methods": [],
                    "content": {},
                },
            ]
        }
        with open(test_db_path, "w") as f:
            json.dump(test_data, f)

    yield  # Test runs here

    # Cleanup (if needed)
    # test_db_path.unlink(missing_ok=True)  # Uncomment to clean up after tests


@pytest.fixture
def test_db_path():
    """Return the path to the test database file."""
    return TEST_DATA_DIR / "test_db.json"


@pytest.fixture
def test_entities():
    """Return a list of test entities."""
    return [
        {
            "id": "1",
            "type": "research",
            "name": "Test Research",
            "file": "test_file.py",
            "lineno": 10,
            "docstring": "Test docstring",
            "methods": ["method1", "method2"],
            "content": {"key": "value"},
        },
        {
            "id": "2",
            "type": "code",
            "name": "test_function",
            "file": "test_file.py",
            "lineno": 20,
            "docstring": "Test function",
            "methods": [],
            "content": {},
        },
    ]
