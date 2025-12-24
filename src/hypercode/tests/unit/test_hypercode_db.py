"""Unit tests for hypercode_db.py"""

import json
import os
from pathlib import Path
from unittest.mock import mock_open, patch

import pytest
from hypercode_db import CodeEntity, HypercodeDB

# Test data paths
TEST_DATA_DIR = Path(__file__).parent.parent / "test_data"
TEST_DB_PATH = TEST_DATA_DIR / "test_db.json"
INVALID_JSON_PATH = TEST_DATA_DIR / "invalid.json"
MISSING_FILE_PATH = TEST_DATA_DIR / "nonexistent.json"

# Sample test data
TEST_ENTITIES = [
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


# Fixtures
@pytest.fixture
def sample_db():
    """Fixture that provides a pre-populated HypercodeDB instance."""
    # Create a temporary test database file
    test_data = {"entities": TEST_ENTITIES}

    with open(TEST_DB_PATH, "w") as f:
        json.dump(test_data, f)

    # Create and return the database instance
    db = HypercodeDB(str(TEST_DB_PATH))
    yield db

    # Cleanup
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)


# Test cases
class TestCodeEntity:
    """Tests for the CodeEntity class."""

    def test_code_entity_initialization(self):
        """Test that CodeEntity initializes with default values."""
        entity = CodeEntity(id="1", type="test")
        assert entity.id == "1"
        assert entity.type == "test"
        assert entity.name == ""
        assert entity.file == ""
        assert entity.lineno == 0
        assert entity.methods == []
        assert entity.docstring == ""
        assert entity.content == {}

    def test_code_entity_with_values(self):
        """Test CodeEntity initialization with all values provided."""
        entity = CodeEntity(
            id="1",
            type="test",
            name="test_entity",
            file="test.py",
            lineno=42,
            methods=["method1"],
            docstring="Test docstring",
            content={"key": "value"},
        )
        assert entity.id == "1"
        assert entity.type == "test"
        assert entity.name == "test_entity"
        assert entity.file == "test.py"
        assert entity.lineno == 42
        assert entity.methods == ["method1"]
        assert entity.docstring == "Test docstring"
        assert entity.content == {"key": "value"}


class TestHypercodeDB:
    """Tests for the HypercodeDB class."""

    def test_init_with_valid_file(self, sample_db):
        """Test initialization with a valid database file."""
        assert len(sample_db.entities) == 2
        assert len(sample_db.by_type["research"]) == 1
        assert len(sample_db.by_type["code"]) == 1
        assert len(sample_db.by_file["test_file.py"]) == 2

    def test_init_with_missing_file(self):
        """Test initialization with a non-existent file."""
        with pytest.raises(FileNotFoundError):
            HypercodeDB(str(MISSING_FILE_PATH))

    def test_init_with_invalid_json(self):
        """Test initialization with invalid JSON data."""
        # Create a file with invalid JSON
        with open(INVALID_JSON_PATH, "w") as f:
            f.write("not a valid json")

        try:
            with pytest.raises(json.JSONDecodeError):
                HypercodeDB(str(INVALID_JSON_PATH))
        finally:
            # Cleanup
            if os.path.exists(INVALID_JSON_PATH):
                os.remove(INVALID_JSON_PATH)

    def test_init_with_invalid_format(self, tmp_path):
        """Test initialization with a file that has invalid format."""
        # Create a file with valid JSON but invalid format
        invalid_data = {"not_entities": []}
        invalid_file = tmp_path / "invalid_format.json"
        with open(invalid_file, "w") as f:
            json.dump(invalid_data, f)

        with pytest.raises(ValueError) as excinfo:
            HypercodeDB(str(invalid_file))
        assert "Invalid database format" in str(excinfo.value)

    def test_get_entities_by_type(self, sample_db):
        """Test getting entities by type."""
        research_entities = sample_db.get_entities_by_type("research")
        assert len(research_entities) == 1
        assert research_entities[0].name == "Test Research"

        code_entities = sample_db.get_entities_by_type("code")
        assert len(code_entities) == 1
        assert code_entities[0].name == "test_function"

        # Test with non-existent type
        assert sample_db.get_entities_by_type("nonexistent") == []

    def test_get_entities_by_file(self, sample_db):
        """Test getting entities by file."""
        file_entities = sample_db.get_entities_by_file("test_file.py")
        assert len(file_entities) == 2
        assert {e.name for e in file_entities} == {"Test Research", "test_function"}

        # Test with non-existent file
        assert sample_db.get_entities_by_file("nonexistent.py") == []

    def test_search_entities(self, sample_db):
        """Test searching entities by name and type."""
        # Search by name
        results = sample_db.search_entities(name="Test Research")
        assert len(results) == 1
        assert results[0].name == "Test Research"

        # Search by type
        results = sample_db.search_entities(entity_type="code")
        assert len(results) == 1
        assert results[0].name == "test_function"

        # Search by both name and type
        results = sample_db.search_entities(name="test", entity_type="code")
        assert len(results) == 1
        assert results[0].name == "test_function"

        # Search with no matches
        assert sample_db.search_entities(name="nonexistent") == []


# Test error handling in _load_database
@patch(
    "builtins.open",
    new_callable=mock_open,
    read_data=json.dumps({"entities": [{"id": "1"}]}),
)
def test_load_database_missing_required_fields(mock_file):
    """Test loading database with entities missing required fields."""
    with pytest.raises(TypeError):
        HypercodeDB("dummy_path.json")


# Test the print_analysis function
@patch("builtins.print")
def test_print_analysis(mock_print, sample_db):
    """Test the print_analysis function."""
    from hypercode_db import print_analysis

    print_analysis(sample_db)

    # Verify that print was called with expected output
    assert mock_print.called
    output = "\n".join([str(call[0][0]) for call in mock_print.call_args_list])
    assert "Total entities: 2" in output
    assert "Entity types: research, code" in output
    assert "Files: test_file.py (2)" in output
