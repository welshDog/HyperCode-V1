"""
Enhanced test suite for the HyperCode lexer.

This module contains comprehensive tests for the HyperCode lexer,
covering edge cases, Unicode support, and error handling.
"""

import os
import sys

import pytest

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from hypercode.core.lexer import Lexer
from hypercode.core.tokens import TokenType

# Test cases for basic token recognition
BASIC_TOKENS = [
    ("+", TokenType.PLUS),
    ("-", TokenType.MINUS),
    ("*", TokenType.STAR),
    ("/", TokenType.SLASH),
    ("(", TokenType.LEFT_PAREN),
    (")", TokenType.RIGHT_PAREN),
    ("{", TokenType.LEFT_BRACE),
    ("}", TokenType.RIGHT_BRACE),
    (",", TokenType.COMMA),
    (".", TokenType.DOT),
    (";", TokenType.SEMICOLON),
    ("%", TokenType.PERCENT),
    ("!", TokenType.BANG),
    ("=", TokenType.EQUAL),
    (">", TokenType.GREATER),
    ("<", TokenType.LESS),
    (":", TokenType.COLON),
    ("?", TokenType.QUESTION),
    ("==", TokenType.EQUAL_EQUAL),
    ("!=", TokenType.BANG_EQUAL),
    (">=", TokenType.GREATER_EQUAL),
    ("<=", TokenType.LESS_EQUAL),
    ("=>", TokenType.ARROW),
]

# Test cases for keywords
KEYWORD_TOKENS = [
    ("and", TokenType.AND),
    ("break", TokenType.BREAK),
    ("class", TokenType.CLASS),
    ("continue", TokenType.CONTINUE),
    ("else", TokenType.ELSE),
    ("false", TokenType.FALSE),
    ("for", TokenType.FOR),
    ("fun", TokenType.FUN),
    ("if", TokenType.IF),
    ("nil", TokenType.NIL),
    ("or", TokenType.OR),
    ("print", TokenType.PRINT),
    ("return", TokenType.RETURN),
    ("super", TokenType.SUPER),
    ("this", TokenType.THIS),
    ("true", TokenType.TRUE),
    ("var", TokenType.VAR),
    ("while", TokenType.WHILE),
]

# Test cases for numbers
NUMBER_TOKENS = [
    ("0", 0.0),
    ("123", 123.0),
    ("3.14", 3.14),
    ("0.5", 0.5),
    ("123e5", 123e5),
    ("123e-5", 123e-5),
    ("123.456e7", 123.456e7),
]

# Test cases for strings and escape sequences
STRING_TOKENS = [
    ('"hello"', "hello"),
    ('""', ""),
    ('"\\""', '"'),
    ('"\\n"', "\n"),
    ('"\\t"', "\t"),
    ('"\\""', '"'),
    ('"\\\\"', "\\"),
]

# Unicode test cases
UNICODE_TOKENS = [
    ('"ã“ã‚“ã«ã¡ã¯"', "ã“ã‚“ã«ã¡ã¯"),  # Japanese
    ('"ì•ˆë…•í•˜ì„¸ìš”"', "ì•ˆë…•í•˜ì„¸ìš”"),  # Korean
    ('"ÐŸÑ€Ð¸Ð²ÐµÑ‚"', "ÐŸÑ€Ð¸Ð²ÐµÑ‚"),  # Russian
    ('"Ù…Ø±Ø­Ø¨Ø§"', "Ù…Ø±Ø­Ø¨Ø§"),  # Arabic
    ('"ðŸ˜Š"', "ðŸ˜Š"),  # Emoji
]

# Edge cases for identifiers
IDENTIFIER_TOKENS = [
    ("x", "x"),
    ("_x", "_x"),
    ("x1", "x1"),
    ("x_1", "x_1"),
    ("x_", "x_"),
    ("x_y_z", "x_y_z"),
    ("x1y2z3", "x1y2z3"),
]

# Test cases for error handling
ERROR_CASES = [
    ('"unterminated string', "Unterminated string"),
    ('"invalid escape \\x"', "Invalid escape sequence"),
    ("123abc", "Unexpected character"),
    ("@", "Unexpected character"),
]


@pytest.mark.parametrize("source,expected_type", BASIC_TOKENS)
def test_basic_tokens(source, expected_type):
    """Test that basic tokens are correctly recognized."""
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()
    assert len(tokens) == 2  # Token + EOF
    assert tokens[0].type == expected_type
    assert tokens[1].type == TokenType.EOF


@pytest.mark.parametrize("source,expected_type", KEYWORD_TOKENS)
def test_keywords(source, expected_type):
    """Test that all keywords are correctly recognized."""
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()
    assert len(tokens) == 2  # Keyword + EOF
    assert tokens[0].type == expected_type
    assert tokens[0].lexeme == source
    assert tokens[1].type == TokenType.EOF


@pytest.mark.parametrize("source,expected_value", NUMBER_TOKENS)
def test_numbers(source, expected_value):
    """Test that number literals are correctly parsed."""
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()
    assert len(tokens) == 2  # Number + EOF
    assert tokens[0].type == TokenType.NUMBER
    assert tokens[0].literal == expected_value
    assert tokens[1].type == TokenType.EOF


@pytest.mark.parametrize("source,expected_value", STRING_TOKENS)
def test_strings(source, expected_value):
    """Test that string literals are correctly parsed."""
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()
    assert len(tokens) == 2  # String + EOF
    assert tokens[0].type == TokenType.STRING
    assert tokens[0].literal == expected_value
    assert tokens[1].type == TokenType.EOF


@pytest.mark.parametrize("source,expected_value", UNICODE_TOKENS)
def test_unicode_strings(source, expected_value):
    """Test that Unicode strings are correctly handled."""
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()
    assert len(tokens) == 2  # String + EOF
    assert tokens[0].type == TokenType.STRING
    assert tokens[0].literal == expected_value
    assert tokens[1].type == TokenType.EOF


@pytest.mark.parametrize("source,expected_lexeme", IDENTIFIER_TOKENS)
def test_identifiers(source, expected_lexeme):
    """Test that identifiers are correctly recognized."""
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()
    assert len(tokens) == 2  # Identifier + EOF
    assert tokens[0].type == TokenType.IDENTIFIER
    assert tokens[0].lexeme == expected_lexeme
    assert tokens[1].type == TokenType.EOF


@pytest.mark.parametrize("source,expected_error", ERROR_CASES)
def test_lexer_errors(source, expected_error):
    """Test that lexer reports appropriate errors."""
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()
    assert len(lexer.errors) > 0
    assert any(expected_error in str(e) for e in lexer.errors)


def test_comments():
    """Test that comments are properly ignored."""
    source = """
    # This is a comment
    x = 42  # This is another comment
    """
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()
    # Should only have IDENTIFIER, EQUAL, NUMBER, and EOF tokens
    assert len(tokens) == 4
    assert tokens[0].type == TokenType.IDENTIFIER
    assert tokens[1].type == TokenType.EQUAL
    assert tokens[2].type == TokenType.NUMBER
    assert tokens[3].type == TokenType.EOF


def test_whitespace():
    """Test that whitespace is properly handled."""
    source = "  \t\n  x  \t =  \t 42  \n  "
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()
    # Should only have IDENTIFIER, EQUAL, NUMBER, and EOF tokens
    assert len(tokens) == 4
    assert tokens[0].type == TokenType.IDENTIFIER
    assert tokens[1].type == TokenType.EQUAL
    assert tokens[2].type == TokenType.NUMBER
    assert tokens[3].type == TokenType.EOF


def test_empty_file():
    """Test that an empty file produces only an EOF token."""
    lexer = Lexer("")
    tokens = lexer.scan_tokens()
    assert len(tokens) == 1
    assert tokens[0].type == TokenType.EOF


def test_line_numbers():
    """Test that line numbers are correctly tracked."""
    source = """
    x = 1
    y = 2
    if x < y:
        print(x)
    """
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()

    # Check line numbers for tokens
    assert tokens[0].line == 2  # x
    assert tokens[3].line == 2  # 1
    assert tokens[4].line == 3  # y
    assert tokens[7].line == 3  # 2
    assert tokens[8].line == 4  # if
    assert tokens[12].line == 4  # :
    assert tokens[13].line == 5  # print


if __name__ == "__main__":
    pytest.main([__file__])
