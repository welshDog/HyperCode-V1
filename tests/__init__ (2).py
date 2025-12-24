"""Test package for HyperCode."""
from pathlib import Path

TEST_DIR = Path(__file__).parent
TEST_DATA_DIR = TEST_DIR / "test_data"


def read_test_file(filename: str) -> str:
    """Read a test file from the test_data directory."""
    path = TEST_DATA_DIR / filename
    return path.read_text(encoding="utf-8")
