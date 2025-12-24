# scripts/test_hypercode.py
import os
import sys

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.hypercode.core.lexer import Lexer
from src.hypercode.core.parser import Parser


def test_lexer(source_code):
    print("=== Testing Lexer ===")
    print(f"Source code:\n{source_code}\n")

    lexer = Lexer(source_code)
    tokens = lexer.scan_tokens()

    print("Tokens:")
    for token in tokens:
        print(
            f"  {token.type.name}: {token.lexeme!r} (line {token.line}, col {token.column})"
        )
    print()

    return tokens


def test_parser(tokens):
    print("=== Testing Parser ===")
    parser = Parser(tokens)
    program = parser.parse()

    print("Parsed program structure:")
    print(program)
    print()

    return program


def main():
    # Test HyperCode source code
    source = """
    # This is a comment
    let x = 42
    let name = "HyperCode"

    if x > 10 then
        print("x is greater than 10")
    else
        print("x is 10 or less")

    function greet(name)
        return "Hello, " + name
    end

    let result = greet(name)
    print(result)
    """

    # Test the lexer
    tokens = test_lexer(source)

    # Test the parser
    program = test_parser(tokens)


if __name__ == "__main__":
    main()
