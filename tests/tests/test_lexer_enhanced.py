# tests/test_lexer_enhanced.py
from hypercode.core.lexer import Lexer
from hypercode.core.tokens import TokenType


def test_lexer_edge_cases():
    # Test empty input
    lexer = Lexer("")
    tokens = lexer.scan_tokens()
    assert len(tokens) == 1  # Just EOF
    assert tokens[0].type == TokenType.EOF

    # Test only whitespace
    lexer = Lexer("  \n\t  \n")
    tokens = lexer.scan_tokens()
    assert len(tokens) == 1  # Just EOF

    # Test very long identifier
    long_ident = "a" * 1000
    lexer = Lexer(long_ident)
    tokens = lexer.scan_tokens()
    assert tokens[0].type == TokenType.IDENTIFIER
    assert tokens[0].lexeme == long_ident
    assert len(tokens[0].lexeme) == 1000


def test_lexer_error_handling():
    # Test unterminated string
    lexer = Lexer('"unterminated string')
    tokens = lexer.scan_tokens()
    assert len(lexer.errors) == 1
    assert "Unterminated string" in lexer.errors[0].message

    # Test invalid character
    lexer = Lexer("var x = @")
    tokens = lexer.scan_tokens()
    assert len(lexer.errors) == 1
    assert "Unexpected character" in lexer.errors[0].message
    assert "@" in lexer.errors[0].message


def test_lexer_number_literals():
    # Test various number formats
    source = """
    42
    3.14159
    1e5
    0xFF
    0b1010
    1_000_000
    """
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()

    # Should have 7 tokens (6 numbers + EOF)
    assert len(tokens) == 7
    assert tokens[0].type == TokenType.NUMBER
    assert tokens[0].literal == 42
    assert tokens[1].type == TokenType.NUMBER
    assert tokens[1].literal == 3.14159
    # ... more assertions for other number formats


def test_lexer_string_interpolation():
    source = 'f"Hello, {name}!"'
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()

    # Should tokenize as: f, ", Hello, , {, name, }, !
    assert len(tokens) == 8  # 7 tokens + EOF
    assert tokens[0].type == TokenType.IDENTIFIER
    assert tokens[0].lexeme == "f"
    assert tokens[1].type == TokenType.STRING
    assert tokens[1].literal == "Hello, "
    # ... more assertions for string interpolation


def test_lexer_docstrings():
    source = """
    /** This is a docstring */
    fun example() {
        // Regular comment
        return 42;
    }
    """
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()

    # Should properly identify docstring as a special token
    assert tokens[0].type == TokenType.DOCSTRING
    assert "This is a docstring" in tokens[0].literal
    # ... more assertions for docstring handling
