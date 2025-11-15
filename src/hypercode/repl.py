import sys

from .core.lexer import Lexer
from .core.parser import Parser


def run_repl():
    print("HyperCode REPL (type 'exit' to quit)")
    while True:
        try:
            source = input("> ")
            if source.lower() in ("exit", "quit"):
                break
            run(source)
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")


def run(source: str):
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    # For now, just print the tokens
    for token in tokens:
        print(token)

    parser = Parser(tokens)
    statements = parser.parse()

    # In the future, we'll execute these statements
    for stmt in statements:
        print(stmt)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Run a file
        with open(sys.argv[1], "r") as f:
            run(f.read())
    else:
        # Start REPL
        run_repl()
