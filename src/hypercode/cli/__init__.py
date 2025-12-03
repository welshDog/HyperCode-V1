"""
HyperCode Command Line Interface

This module provides the command-line interface for the HyperCode language.
"""

import argparse
import sys
from pathlib import Path
from typing import Optional, Sequence
from hypercode.core.lexer import Lexer


def main(args: Optional[Sequence[str]] = None) -> int:
    """Run the HyperCode lexer from the command line.

    Args:
        args: Command line arguments (defaults to sys.argv[1:])

    Returns:
        int: Exit code (0 for success, non-zero for errors)
    """
    parser = argparse.ArgumentParser(description="HyperCode language lexer")
    parser.add_argument(
        "source_file",
        type=str,
        help="Path to the source file to tokenize",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Enable verbose output"
    )

    parsed_args = parser.parse_args(args)

    try:
        # Read the source file
        source_path = Path(parsed_args.source_file)
        if not source_path.exists():
            print(f"Error: File '{source_path}' not found.", file=sys.stderr)
            return 1

        source = source_path.read_text(encoding="utf-8")

        # Tokenize the source
        lexer = Lexer()
        tokens = lexer.tokenize(source)

        # Print tokens
        if parsed_args.verbose:
            print(f"Tokens from {source_path}:")
            print("-" * 80)

        for token in tokens:
            print(
                f"{token.line:4d}:{token.column:<3d} {token.type.name:<15} {token.lexeme!r}"
            )

        print(f"\nSuccessfully tokenized {source_path}")
        if parsed_args.verbose:
            print(f"Total tokens: {len(tokens)}")

        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if parsed_args.verbose:
            import traceback

            traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
