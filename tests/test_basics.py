from hypercode.core.interpreter import Interpreter
from hypercode.core.lexer import Lexer
from hypercode.core.parser import Parser


def test_lexer_basic():
    source = "print 'Hello, World!'"
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()
    assert len(tokens) > 0  # Simple check that we got some tokens


def test_parser_basic():
    source = "print 'Hello, World!'"
    lexer = Lexer(source)
    parser = Parser(lexer.scan_tokens())
    statements = parser.parse()
    assert statements is not None
