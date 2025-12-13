import pytest
import sys
from pathlib import Path

# Add project root and src directory to Python path
project_root = str(Path(__file__).parent.parent)
src_dir = str(Path(project_root) / "src")

# Add to sys.path if not already there
for path in [project_root, src_dir]:
    if path not in sys.path:
        sys.path.insert(0, path)


@pytest.fixture
def sample_hypercode():
    return """
    // Sample HyperCode program
    fun greet(name) {
        return "Hello, " + name + "!";
    }
    print(greet("World"));
    """


@pytest.fixture
def sample_lexer_tokens():
    return [
        {"type": "FUN", "lexeme": "fun", "line": 1},
        {"type": "IDENTIFIER", "lexeme": "greet", "line": 1},
        {"type": "LEFT_PAREN", "lexeme": "(", "line": 1},
        {"type": "IDENTIFIER", "lexeme": "name", "line": 1},
        {"type": "RIGHT_PAREN", "lexeme": ")", "line": 1},
        {"type": "LEFT_BRACE", "lexeme": "{", "line": 2},
        {"type": "RETURN", "lexeme": "return", "line": 3},
        {"type": "STRING", "lexeme": "Hello, ", "literal": "Hello, ", "line": 3},
        {"type": "PLUS", "lexeme": "+", "line": 3},
        {"type": "IDENTIFIER", "lexeme": "name", "line": 3},
        {"type": "PLUS", "lexeme": "+", "line": 3},
        {"type": "STRING", "lexeme": "!", "literal": "!", "line": 3},
        {"type": "SEMICOLON", "lexeme": ";", "line": 3},
        {"type": "RIGHT_BRACE", "lexeme": "}", "line": 4},
        {"type": "PRINT", "lexeme": "print", "line": 5},
        {"type": "LEFT_PAREN", "lexeme": "(", "line": 5},
        {"type": "IDENTIFIER", "lexeme": "greet", "line": 5},
        {"type": "LEFT_PAREN", "lexeme": "(", "line": 5},
        {"type": "STRING", "lexeme": "World", "literal": "World", "line": 5},
        {"type": "RIGHT_PAREN", "lexeme": ")", "line": 5},
        {"type": "RIGHT_PAREN", "lexeme": ")", "line": 5},
        {"type": "SEMICOLON", "lexeme": ";", "line": 5},
        {"type": "EOF", "lexeme": "", "line": 6},
    ]
