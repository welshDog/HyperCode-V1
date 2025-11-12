import pytest
from hypercode.core.lexer import Lexer, Token, TokenType

def test_lexer_basic_tokens():
    source = "let x = 42"
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    expected = [
        (TokenType.LET, "let"),
        (TokenType.IDENTIFIER, "x"),
        (TokenType.EQUAL, "="),
        (TokenType.NUMBER, "42"),
        (TokenType.EOF, ""),
    ]
    
    for (exp_type, exp_value), token in zip(expected, tokens):
        assert token.type == exp_type
        assert token.value == exp_value

def test_lexer_strings():
    source = '"hello"'
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    assert tokens[0].type == TokenType.STRING
    assert tokens[0].value == '"hello"'

@pytest.mark.parametrize("source,expected_type", [
    ("+", TokenType.PLUS),
    ("-", TokenType.MINUS),
    ("*", TokenType.STAR),
    ("/", TokenType.SLASH),
    ("=", TokenType.EQUAL),
    ("==", TokenType.EQUAL_EQUAL),
    ("!=", TokenType.BANG_EQUAL),
    (">", TokenType.GREATER),
    (">=", TokenType.GREATER_EQUAL),
    ("<", TokenType.LESS),
    ("<=", TokenType.LESS_EQUAL),
])
def test_lexer_operators(source, expected_type):
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    assert tokens[0].type == expected_type