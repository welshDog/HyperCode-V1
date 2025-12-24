import os
import sys

import pytest

# Add the src directory to the Python path
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "src"))
)


def test_example():
    """Example test that should always pass."""
    assert 1 + 1 == 2


class TestLexer:
    def test_lexer_import(self):
        """Test that the lexer can be imported."""
        try:
            from hypercode.core.lexer import Lexer

            assert Lexer is not None
        except ImportError as e:
            pytest.fail(f"Could not import Lexer: {str(e)}")
