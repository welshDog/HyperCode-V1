from core.lexer import Lexer
from core.parser import Parser
from core.interpreter import Interpreter
import sys
import os

# Ensure import path is correct
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

source = """
print(10 % 3);
print(20 % 5);
"""

print("--- Testing Modulo (%) ---")
try:
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()
    parser = Parser(tokens)
    statements = parser.parse()
    interpreter = Interpreter()
    interpreter.interpret(statements)
    print("--- Test Complete ---")
except Exception as e:
    print(f"FAILED: {e}")
