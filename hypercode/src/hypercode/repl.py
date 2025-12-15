import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from hypercode.core.interpreter import Interpreter
from hypercode.core.lexer import Lexer
from hypercode.core.parser import Parser


def run_repl():
    print("🚀 HyperCode REPL v1.0")
    print("Type 'exit' to quit, 'help' for examples")
    print("-" * 40)
    while True:
        try:
            source = input("> ")
            if source.lower() in ("exit", "quit"):
                print("👋 Goodbye!")
                break
            if source.lower() == "help":
                show_help()
                continue
            run(source)
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


def run(source: str):
    # Lexical analysis
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()

    if lexer.errors:
        for error in lexer.errors:
            print(
                f"❌ Lexer Error at line {error.line}:{error.column}: {error.message}"
            )
        return

    # Parsing
    parser = Parser(tokens)
    statements = parser.parse()

    # Execution
    interpreter = Interpreter()
    interpreter.interpret(statements)


def show_help():
    print(
        """
📚 HyperCode Quick Examples:

1. Print a message:
   print("Hello, HyperCode!");

2. Variables:
   var x = 42;
   print(x);

3. Math:
   var result = (10 + 2) * 3;
   print(result);

4. Strings:
   var name = "BROski";
   print("Hello, " + name);
"""
    )


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Run a file
        with open(sys.argv[1], "r") as f:
            run(f.read())
    else:
        # Start REPL
        run_repl()
