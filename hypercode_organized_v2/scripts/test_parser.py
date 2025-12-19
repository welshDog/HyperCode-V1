# test_parser.py
import sys
import os

# Add the src directory to the Python path
src_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from hypercode.core.lexer import Lexer
from hypercode.core.parser import Parser

def test_parser():
    # Test case 1: Simple variable declaration
    source1 = "var x = 42;"
    print("\nTest 1 - Variable Declaration:")
    try:
        tokens1 = Lexer(source1).scan_tokens()
        parser1 = Parser(tokens1)
        program1 = parser1.parse()
        print(f"Number of statements: {len(program1.statements)}")
        if program1.statements:
            stmt = program1.statements[0]
            print(f"Statement type: {type(stmt).__name__}")
            if hasattr(stmt, 'name') and hasattr(stmt, 'initializer'):
                print(f"Variable: {stmt.name}")
                if stmt.initializer:
                    print(f"Initializer value: {stmt.initializer.value}")
    except Exception as e:
        print(f"Error in test 1: {e}")

    # Test case 2: Expression statement
    source2 = "42;"
    print("\nTest 2 - Expression Statement:")
    try:
        tokens2 = Lexer(source2).scan_tokens()
        parser2 = Parser(tokens2)
        program2 = parser2.parse()
        print(f"Number of statements: {len(program2.statements)}")
        if program2.statements:
            stmt = program2.statements[0]
            print(f"Statement type: {type(stmt).__name__}")
            if hasattr(stmt, 'expression'):
                print(f"Expression type: {type(stmt.expression).__name__}")
                if hasattr(stmt.expression, 'value'):
                    print(f"Value: {stmt.expression.value}")
    except Exception as e:
        print(f"Error in test 2: {e}")

    # Test case 3: Binary expression
    source3 = "x + 10;"
    print("\nTest 3 - Binary Expression:")
    try:
        tokens3 = Lexer(source3).scan_tokens()
        parser3 = Parser(tokens3)
        program3 = parser3.parse()
        print(f"Number of statements: {len(program3.statements)}")
        if program3.statements:
            stmt = program3.statements[0]
            print(f"Statement type: {type(stmt).__name__}")
            if hasattr(stmt, 'expression') and hasattr(stmt.expression, 'left'):
                bin_expr = stmt.expression
                left = bin_expr.left
                right = bin_expr.right
                print(f"Left: {type(left).__name__}({getattr(left, 'name', '')})")
                print(f"Operator: {bin_expr.operator.lexeme}")
                print(f"Right: {type(right).__name__}({getattr(right, 'value', '')})")
    except Exception as e:
        print(f"Error in test 3: {e}")

if __name__ == "__main__":
    test_parser()
