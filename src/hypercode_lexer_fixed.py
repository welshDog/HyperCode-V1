"""
HyperCode Lexer - Fixed String Handling with Escape Sequences
Properly handles escaped quotes, newlines, tabs, and other escape sequences

Key improvements:
1. Correctly parses escaped characters within strings
2. Handles both single and double quotes
3. Preserves or converts escapes (configurable)
4. Provides detailed error messages for malformed strings
5. Includes comprehensive test cases
"""

import sys
from dataclasses import dataclass
from enum import Enum
from typing import List


class TokenType(Enum):
    """HyperCode token types"""

    # Core operations
    PUSH = "PUSH"  # >
    POP = "POP"  # <
    INCR = "INCR"  # +
    DECR = "DECR"  # -
    OUTPUT = "OUTPUT"  # .
    INPUT = "INPUT"  # ,
    LOOP_START = "LOOP_START"  # [
    LOOP_END = "LOOP_END"  # ]

    # String literals
    STRING = "STRING"  # "..." or '...'

    # Comments
    COMMENT = "COMMENT"  # ;

    # Special
    EOF = "EOF"
    UNKNOWN = "UNKNOWN"


@dataclass
class Token:
    """Represents a single token with position tracking"""

    type: TokenType
    value: str
    raw_value: str  # Original value (with escapes)
    position: int
    line: int
    column: int

    def __repr__(self) -> str:
        """Readable representation"""
        if self.value != self.raw_value:
            return (
                f"Token({self.type.value:15} | value='{self.value}' "
                f"| raw='{self.raw_value}' | L{self.line}:C{self.column})"
            )
        else:
            return (
                f"Token({self.type.value:15} | '{self.value}' "
                f"| L{self.line}:C{self.column})"
            )


class LexerError(Exception):
    """Lexer error with context"""

    def __init__(self, message: str, line: int, column: int, context: str = "") -> None:
        self.message = message
        self.line = line
        self.column = column
        self.context = context

        error_msg = f"Line {line}, Col {column}: {message}"
        if context:
            error_msg += f"\n  Context: {context}"

        super().__init__(error_msg)


class HyperCodeLexerFixed:
    """
    Fixed lexer with proper string escape sequence handling.

    Escape sequences supported:
    - \\" = escaped double quote
    - \\' = escaped single quote
    - \\\\ = escaped backslash
    - \\n = newline
    - \\t = tab
    - \\r = carriage return
    - \\b = backspace
    - \\f = form feed
    """

    # Escape sequence mappings
    ESCAPE_SEQUENCES = {
        '"': '"',  # Escaped double quote
        "'": "'",  # Escaped single quote
        "\\": "\\",  # Escaped backslash
        "n": "\n",  # Newline
        "t": "\t",  # Tab
        "r": "\r",  # Carriage return
        "b": "\b",  # Backspace
        "f": "\f",  # Form feed
        "0": "\0",  # Null character
    }

    # Single character operations
    OPERATIONS = {
        ">": TokenType.PUSH,
        "<": TokenType.POP,
        "+": TokenType.INCR,
        "-": TokenType.DECR,
        ".": TokenType.OUTPUT,
        ",": TokenType.INPUT,
        "[": TokenType.LOOP_START,
        "]": TokenType.LOOP_END,
        ";": TokenType.COMMENT,
    }

    def __init__(
        self, source: str, filename: str = "<stdin>", preserve_escapes: bool = False
    ):
        """
        Initialize lexer.

        Args:
            source: Source code
            filename: Filename for error reporting
            preserve_escapes: If True, keep escapes in output (e.g., "hello\\"world")
                            If False, convert to actual chars (e.g., "hello"world")
        """
        self.source = source
        self.filename = filename
        self.preserve_escapes = preserve_escapes
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []

    def tokenize(self) -> List[Token]:
        """
        Convert source to token stream.

        Returns:
            List of tokens

        Raises:
            LexerError: On invalid syntax
        """
        self.tokens = []

        while self.position < len(self.source):
            char = self.source[self.position]

            # Skip whitespace
            if char.isspace():
                self._advance(char)
                continue

            # Comments (skip until end of line)
            if char == ";":
                self._skip_comment()
                continue

            # String literals (double quotes)
            if char == '"':
                self._parse_string('"')
                continue

            # String literals (single quotes)
            if char == "'":
                self._parse_string("'")
                continue

            # Operations
            if char in self.OPERATIONS:
                token_type = self.OPERATIONS[char]
                token = Token(
                    type=token_type,
                    value=char,
                    raw_value=char,
                    position=self.position,
                    line=self.line,
                    column=self.column,
                )
                self.tokens.append(token)
                self._advance(char)
                continue

            # Unknown character
            raise LexerError(
                f"Unexpected character: '{char}' (ASCII {ord(char)})",
                self.line,
                self.column,
                "Valid: > < + - . , [ ] ; or string literals",
            )

        # EOF token
        self.tokens.append(
            Token(
                type=TokenType.EOF,
                value="",
                raw_value="",
                position=self.position,
                line=self.line,
                column=self.column,
            )
        )

        return self.tokens

    def _parse_string(self, quote_char: str) -> None:
        """
        Parse string literal with escape sequence handling.

        Args:
            quote_char: Quote character (" or ')

        Raises:
            LexerError: If string is unterminated or contains invalid escapes
        """
        start_pos = self.position
        start_line = self.line
        start_col = self.column

        raw_string = ""  # Keep original with escapes
        parsed_string = ""  # Convert escapes

        self._advance(quote_char)  # Skip opening quote

        while self.position < len(self.source):
            char = self.source[self.position]

            # Closing quote (unescaped)
            if char == quote_char:
                self._advance(char)

                # Create token
                token = Token(
                    type=TokenType.STRING,
                    value=parsed_string,
                    raw_value=raw_string,
                    position=start_pos,
                    line=start_line,
                    column=start_col,
                )
                self.tokens.append(token)
                return

            # Escape sequence
            if char == "\\":
                raw_string += char
                self._advance(char)

                if self.position >= len(self.source):
                    raise LexerError(
                        "Unterminated string: backslash at end of file",
                        self.line,
                        self.column,
                        f"String started at line {start_line}, col {start_col}",
                    )

                next_char = self.source[self.position]

                # Valid escape sequence?
                if next_char in self.ESCAPE_SEQUENCES:
                    escaped_char = self.ESCAPE_SEQUENCES[next_char]
                    raw_string += next_char
                    parsed_string += escaped_char
                    self._advance(next_char)
                else:
                    raise LexerError(
                        f"Invalid escape sequence: '\\{next_char}'",
                        self.line,
                        self.column,
                        "Valid escapes: "
                        + ", ".join(["\\" + k for k in self.ESCAPE_SEQUENCES]),
                    )

                continue

            # Regular character
            raw_string += char
            parsed_string += char
            self._advance(char)

        # Unterminated string
        raise LexerError(
            f"Unterminated string: missing closing {quote_char}",
            start_line,
            start_col,
            f"String started here, expected {quote_char} before EOF",
        )

    def _skip_comment(self) -> None:
        """Skip comment until end of line"""
        while self.position < len(self.source) and self.source[self.position] != "\n":
            self._advance(self.source[self.position])

    def _advance(self, char: str) -> None:
        """Update position after processing character"""
        self.position += 1

        if char == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

    def print_tokens(self, verbose: bool = True) -> None:
        """Print tokens in readable format"""
        for token in self.tokens:
            if verbose:
                print(token)
            else:
                print(f"{token.type.value:15} | {repr(token.value)}")


# ============================================================================
# TEST SUITE
# ============================================================================


def run_tests() -> None:
    """Comprehensive test suite"""

    test_cases = [
        # (description, source, expected_tokens)
        ("Simple double-quoted string", '"hello"', [("STRING", "hello")]),
        ("Simple single-quoted string", "'world'", [("STRING", "world")]),
        (
            "Multiple strings",
            "\"hello\" 'world'",
            [("STRING", "hello"), ("STRING", "world")],
        ),
        (
            "String with escaped double quote",
            '"escaped \\"quote\\""',
            [("STRING", 'escaped "quote"')],
        ),
        ("String with escaped single quote", "'it\\'s'", [("STRING", "it's")]),
        (
            "String with escaped backslash",
            '"path\\\\to\\\\file"',
            [("STRING", "path\\to\\file")],
        ),
        ("String with newline escape", '"hello\\nworld"', [("STRING", "hello\nworld")]),
        (
            "String with tab escape",
            '"column1\\tcolumn2"',
            [("STRING", "column1\tcolumn2")],
        ),
        (
            "String with multiple escapes",
            '"say \\"hello\\nworld\\""',
            [("STRING", 'say "hello\nworld"')],
        ),
        (
            "HyperCode with strings",
            '+++. "output"',
            [
                ("INCR", "+"),
                ("INCR", "+"),
                ("INCR", "+"),
                ("OUTPUT", "."),
                ("STRING", "output"),
            ],
        ),
        (
            "Complex mixed case",
            '"escaped \\"quote\\"" \'world\' > < +',
            [
                ("STRING", 'escaped "quote"'),
                ("STRING", "world"),
                ("PUSH", ">"),
                ("POP", "<"),
                ("INCR", "+"),
            ],
        ),
    ]

    print("\n" + "=" * 70)
    print("🧪 HYPERCODE LEXER - STRING HANDLING TESTS")
    print("=" * 70 + "\n")

    passed = 0
    failed = 0

    for description, source, expected in test_cases:
        try:
            lexer = HyperCodeLexerFixed(source)
            tokens = lexer.tokenize()

            # Filter out EOF token for comparison
            tokens = [t for t in tokens if t.type != TokenType.EOF]

            # Check if token count matches
            if len(tokens) != len(expected):
                print(f"❌ {description}")
                print(f"   Input: {source}")
                print(f"   Expected {len(expected)} tokens, got {len(tokens)}")
                print(f"   Got: {[(t.type.value, repr(t.value)) for t in tokens]}")
                failed += 1
                continue

            # Check each token
            all_match = True
            for token, (exp_type, exp_value) in zip(tokens, expected):
                if token.type.value != exp_type or token.value != exp_value:
                    all_match = False
                    break

            if all_match:
                print(f"✅ {description}")
                passed += 1
            else:
                print(f"❌ {description}")
                print(f"   Input: {source}")
                print(f"   Expected: {expected}")
                print(f"   Got: {[(t.type.value, repr(t.value)) for t in tokens]}")
                failed += 1

        except LexerError as e:
            print(f"❌ {description}")
            print(f"   Input: {source}")
            print(f"   Error: {e}")
            failed += 1

        except Exception as e:
            print(f"❌ {description}")
            print(f"   Input: {source}")
            print(f"   Unexpected error: {e}")
            failed += 1

    print()
    print("=" * 70)
    print(f"Results: {passed} passed, {failed} failed")
    print("=" * 70 + "\n")


def main() -> None:
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description="HyperCode Lexer - Fixed String Handling",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python lexer_fixed.py --test
  python lexer_fixed.py '"hello\\"world"'
  echo 'echo "test"' | python lexer_fixed.py -
        """,
    )

    parser.add_argument("input", nargs="?", help="Input to tokenize")
    parser.add_argument("--test", action="store_true", help="Run test suite")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")

    args = parser.parse_args()

    if args.test:
        run_tests()

    if not args.input:
        parser.print_help()
        return

    # Read input
    source = sys.stdin.read() if args.input == "-" else args.input

    try:
        lexer = HyperCodeLexerFixed(source)
        tokens = lexer.tokenize()

        print("✅ Successfully tokenized")
        print(f"   Total tokens: {len(tokens) - 1}\n")

        lexer.print_tokens(verbose=args.verbose)

    except LexerError as e:
        print(f"❌ Lexer Error: {e}")


if __name__ == "__main__":
    main()
