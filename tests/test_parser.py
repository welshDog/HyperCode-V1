from hypercode.core.ast import Assign, Binary, Grouping, Literal, Program, Unary, Var, VarDecl
from hypercode.core.lexer import Lexer
from hypercode.core.parser import Parser
from hypercode.core.tokens import Token, TokenType


def test_parser_expression():
    """Test parsing a simple arithmetic expression."""
    source = "3 + 4 * 2 / (1 - 5) + -2"
    lexer = Lexer(source)
    parser = Parser(lexer.scan_tokens())
    expr = parser.expression()

    # Basic check that we got an expression back
    assert expr is not None


def test_parser_variable_declaration():
    """Test parsing a variable declaration."""
    source = "let x = 42"
    lexer = Lexer(source)
    parser = Parser(lexer.scan_tokens())
    program = parser.parse()

    assert program is not None
    assert isinstance(program, Program)
    assert len(program.statements) > 0
    stmt = program.statements[0]
    assert isinstance(stmt, VarDecl)
    assert stmt.name == "x"  # Directly compare with the variable name as a string
    assert hasattr(stmt, "initializer")
    assert isinstance(stmt.initializer, Literal)
    assert stmt.initializer.value == 42
