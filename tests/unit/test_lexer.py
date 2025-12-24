"""
Test script for the HyperCode lexer.

This script provides a simple way to test the lexer with various inputs
and see the resulting tokens.
"""

from hypercode.core.lexer import Lexer
from hypercode.core.tokens import TokenType


def test_lexer(source: str, description: str):
    """Test the lexer with the given source code and print the results.

    Args:
        source: The source code to tokenize
        description: A description of what this test is checking
    """
    print(f"\n{'='*80}")
    print(f"TEST: {description}")
    print(f"{'='*80}")
    print(f"Source code:\n{source}")
    print("\nTokens:")

    try:
        lexer = Lexer(source)
        tokens = lexer.tokenize()

        # Print tokens in a formatted table
        print(f"{'Type':<16} {'Lexeme':<20} {'Literal':<20} Line:Column")
        print("-" * 60)
        for token in tokens:
            literal = repr(str(token.literal)) if token.literal is not None else "None"
            print(
                f"{token.type.name:<16} {token.lexeme!r:<20} {literal:<20} {token.line}:{token.column}"
            )

    except Exception as e:
        print(f"ERROR: {str(e)}")


def run_tests():
    """Run a series of test cases for the lexer."""
    # Test 1: Basic arithmetic
    test_lexer("1 + 2 * 3", "Basic arithmetic operations")

    # Test 2: Variables and assignment
    test_lexer(
        """
        let x = 42
        let name = "HyperCode"
        let is_valid = true
        """,
        "Variable declarations and assignments",
    )

    # Test 3: String with escape sequences
    test_lexer(
        r'let message = "Hello,\nWorld!\tThis is a test\""',
        "String with escape sequences",
    )

    # Test 4: Different number formats
    test_lexer(
        """
        let decimal = 42
        let hex = 0x2A
        let binary = 0b101010
        let octal = 0o52
        let float = 3.14
        let scientific = 6.022e23
        """,
        "Different number formats",
    )

    # Test 5: Control structures
    test_lexer(
        """
        if x > 0 {
            print("Positive")
        } else if x < 0 {
            print("Negative")
        } else {
            print("Zero")
        }
        """,
        "Control structures",
    )

    # Test 6: Function definition and call
    test_lexer(
        """
        fun greet(name) {
            return "Hello, " + name + "!"
        }
        
        let greeting = greet("World")
        """,
        "Function definition and call",
    )

    # Test 7: Docstrings
    test_lexer(
        """
        /**
         * This is a docstring
         * that spans multiple lines
         */
        fun example() {
            # This is a single-line comment
            return 42
        }
        """,
        "Docstrings and comments",
    )

    # Test 8: Edge cases
    test_lexer(
        """
        let empty = ""
        let quotes = "He said \"Hello!\""
        let special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>/?"
        """,
        "Edge cases and special characters",
    )


if __name__ == "__main__":
    print("HyperCode Lexer Test Runner")
    print("=" * 80)
    run_tests()
    print("\nAll tests completed!")
