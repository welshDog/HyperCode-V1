# run_lexer.py
import sys
from pathlib import Path

# Add the project root to the Python path
project_root = str(Path(__file__).parent)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.core.lexer import Lexer


def run_lexer(source_file: str):
    """Run the lexer on a source file and print the tokens."""
    try:
        with open(source_file, "r") as f:
            source = f.read()
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
        return

    print(f"Lexing {source_file}...\n")
    lexer = Lexer(source)
    tokens = lexer.scan_tokens()

    # Print tokens
    print("Tokens:")
    print("-" * 80)
    for token in tokens:
        print(
            f"{token.line:4d}:{token.column:<3d} {token.type.name:<15} {token.lexeme!r}"
        )

    # Print any errors
    if lexer.errors:
        print("\nErrors:")
        print("-" * 80)
        for error in lexer.errors:
            print(f"Line {error.line}, Column {error.column}: {error.message}")

    print(f"\nTotal tokens: {len(tokens)}")
    if lexer.errors:
        print(f"Errors found: {len(lexer.errors)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_lexer.py <source_file>")
        sys.exit(1)

    run_lexer(sys.argv[1])
