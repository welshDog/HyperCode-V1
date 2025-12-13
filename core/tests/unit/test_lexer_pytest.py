"""
Pytest tests for the HyperCode lexer.
"""

from hypercode.core.lexer import Lexer
from hypercode.core.tokens import TokenType


def test_basic_arithmetic():
    """Test basic arithmetic expressions."""
    source = "1 + 2 * 3"
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    token_types = [t.type for t in tokens]
    assert token_types == [
        TokenType.NUMBER,
        TokenType.PLUS,
        TokenType.NUMBER,
        TokenType.STAR,
        TokenType.NUMBER,
        TokenType.EOF,
    ]


def test_variable_declaration():
    """Test variable declarations."""
    source = "let x = 42"
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    token_types = [t.type for t in tokens]
    assert token_types == [
        TokenType.LET,
        TokenType.IDENTIFIER,
        TokenType.EQUAL,
        TokenType.NUMBER,
        TokenType.EOF,
    ]


def test_string_literals():
    """Test string literals."""
    source = 'let message = "Hello, World!"'
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    assert tokens[0].type == TokenType.LET
    assert tokens[1].type == TokenType.IDENTIFIER
    assert tokens[1].lexeme == "message"
    assert tokens[3].type == TokenType.STRING
    assert tokens[3].literal == "Hello, World!"
