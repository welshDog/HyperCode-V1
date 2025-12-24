from hypercode.core.lexer import Lexer, TokenType


def test_lexer_basic():
    """Test basic lexer functionality."""
    source = "print 'Hello, World!'"
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()
    assert len(tokens) > 0  # Should have at least one token


def test_lexer_operators():
    """Test lexing of operators."""
    source = "+ - * / % = == != < > <= >="
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()

    # 12 operators + 1 EOF = 13 tokens
    assert len(tokens) == 13


def test_lexer_keywords():
    """Test lexing of keywords."""
    source = "if else while for function return let var print true false nil"
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()

    # 12 keywords + 1 EOF = 13 tokens
    assert len(tokens) == 13
