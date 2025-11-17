from hypercode.core.ast import (
    Binary,
    Expression,
    Literal,
    Var,
)
from hypercode.core.lexer import Lexer
from hypercode.core.parser import Parser
from hypercode.core.tokens import TokenType


def test_parse_literal():
    source = "42;"
    tokens = Lexer(source).tokenize()
    parser = Parser(tokens)
    statements = parser.parse()

    assert len(statements) == 1
    assert isinstance(statements[0], Expression)
    assert isinstance(statements[0].expression, Literal)
    assert statements[0].expression.value == 42


def test_parse_variable_declaration():
    source = "var x = 42;"
    tokens = Lexer(source).tokenize()
    parser = Parser(tokens)
    statements = parser.parse()

    assert len(statements) == 1
    assert isinstance(statements[0], Var)
    assert statements[0].name.lexeme == "x"
    assert isinstance(statements[0].initializer, Literal)
    assert statements[0].initializer.value == 42


def test_parse_binary_expression():
    source = "1 + 2 * 3;"
    tokens = Lexer(source).tokenize()
    parser = Parser(tokens)
    statements = parser.parse()

    assert len(statements) == 1
    expr = statements[0].expression
    assert isinstance(expr, Binary)
    assert expr.operator.type == TokenType.PLUS
    assert isinstance(expr.right, Binary)
    assert expr.right.operator.type == TokenType.STAR
