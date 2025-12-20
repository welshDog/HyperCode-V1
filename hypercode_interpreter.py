#!/usr/bin/env python3
import sys
import os
import io
from contextlib import redirect_stdout

# Add the organized directory to sys.path to allow imports
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "hypercode_organized_v2"))

try:
    from hypercode.core.lexer import Lexer
    from hypercode.core.parser import Parser
    from hypercode.core.interpreter import Interpreter
except ImportError as e:
    print(f"Error importing HyperCode core: {e}")
    print(f"sys.path: {sys.path}")
    sys.exit(1)


def main():
    if len(sys.argv) < 2:
        print("Usage: python hypercode_interpreter.py <file>")
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        # Check if it's an example name like "hello_world"
        if not filename.endswith(".hc"):
            # Try to resolve example
            pass
        print(f"File not found: {filename}")
        sys.exit(1)

    with open(filename, "r") as f:
        source = f.read()

    run(source)


def run(source):
    try:
        lexer = Lexer(source)
        tokens = lexer.scan_tokens()

        parser = Parser(tokens)
        program = parser.parse()

        interpreter = Interpreter()
        interpreter.interpret(program)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
