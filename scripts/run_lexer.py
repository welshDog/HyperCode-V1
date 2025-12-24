"""
Test suite for HyperCode lexer.

This module contains comprehensive tests for the HyperCode lexer,
verifying tokenization of various language constructs and edge cases.
"""

import os
import sys
import unittest
from typing import List, TypeVar

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    from hypercode.core.lexer import Lexer
    from hypercode.core.tokens import Token, TokenType
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Current sys.path:", sys.path)
    raise

# Type variable for test methods
T = TypeVar("T")


class TestLexer(unittest.TestCase):
    """Test suite for the HyperCode lexer."""

    def setUp(self) -> None:
        """Create a fresh lexer instance for each test."""
        self.lexer = Lexer()

    def test_empty_source(self) -> None:
        """Test that an empty source returns only an EOF token."""
        tokens = self.lexer.tokenize("")
        self.assertEqual(len(tokens), 1)
        self.assertEqual(tokens[0].type, TokenType.EOF)
     
        # Identifiers and keywords (handled specially)
        (re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*"), None),
    ]

    def test_basic_tokens(self) -> None:
        """Test basic token types are correctly identified."""
        source = "var x = 10;"
        expected_types = [
            TokenType.VAR,
            TokenType.IDENTIFIER,
            TokenType.EQUAL,
            TokenType.NUMBER,
            TokenType.SEMICOLON,
        ]
        tokens = self.lexer.tokenize(source)
        self._assert_token_types(tokens, expected_types, "Basic token test failed: ")

    def test_string_literals(self):
        """Test string literals with various contents."""
        test_cases = [
            ('"simple"', "simple"),
            ('"escaped \\n newline"', "escaped \\n newline"),
            ('"unicode "', "unicode "),
        ]

        for source, expected_content in test_cases:
            with self.subTest(source=source):
                tokens = self.lexer.tokenize(f"var s = {source};")
                self.assertEqual(tokens[3].type, TokenType.STRING)
                self.assertEqual(tokens[3].lexeme.strip('"'), expected_content)

    def test_numbers(self) -> None:
        """Test different number formats."""
        test_cases = [
            ("42", 42, 42.0),
            ("3.14", 3.14, 3.14),
            ("1e3", 1000.0, 1000.0),
            ("0x2A", 42, 42.0),  # Hex to int
            ("0b1010", 10, 10.0),  # Binary to int
        ]

        for source, expected_int, expected_float in test_cases:
            with self.subTest(source=source):
                tokens = self.lexer.tokenize(f"n = {source};")
                self.assertEqual(tokens[2].type, TokenType.NUMBER)

                # Check the literal value
                self.assertIsNotNone(tokens[2].literal)
                self.assertEqual(tokens[2].literal, expected_int)

                # For float comparison, handle potential floating point precision
                if isinstance(tokens[2].literal, float):
                    self.assertAlmostEqual(tokens[2].literal, expected_float, places=5)
                else:
                    self.assertEqual(float(tokens[2].literal), expected_float)

    def test_arithmetic_expressions(self) -> None:
        """Test complex arithmetic expressions."""
        source = "result = (x + y * 2) / (3 - 1);"
        expected_types = [
            TokenType.IDENTIFIER,  # result
            TokenType.EQUAL,  # =
            TokenType.LPAREN,  # (
            TokenType.IDENTIFIER,  # x
            TokenType.PLUS,  # +
            TokenType.IDENTIFIER,  # y
            TokenType.STAR,  # *
            TokenType.NUMBER,  # 2
            TokenType.RPAREN,  # )
            TokenType.SLASH,  # /
            TokenType.LPAREN,  # (
            TokenType.NUMBER,  # 3
            TokenType.MINUS,  # -
            TokenType.NUMBER,  # 1
            TokenType.RPAREN,  # )
            TokenType.SEMICOLON,  # ;
        ]
        tokens = self.lexer.tokenize(source)
        self._assert_token_types(tokens, expected_types)

    def test_comments(self):
        """Test different types of comments are properly ignored."""
        source = """
        // Single line comment
        var x = 10;  # Another comment style
        /* Multi-line
           comment */
        """
        tokens = self.lexer.tokenize(source)
        # Should only find the variable declaration tokens and EOF
        self.assertEqual(len(tokens), 6)  # var, x, =, 10, ;, EOF
        self.assertEqual(tokens[0].type, TokenType.VAR)
        self.assertEqual(tokens[-1].type, TokenType.EOF)

    def test_error_handling(self) -> None:
        """Test that the lexer properly handles and reports errors."""
        test_cases = [
            ("var x = @invalid;", "@", "Invalid character"),
            ('var str = "unclosed string', '"', "Invalid character"),
            ("var num = 123abc;", "a", "Invalid character"),
            ("var $invalid = 1;", "$", "Invalid character"),
        ]

        for source, error_char, error_msg in test_cases:
            with self.subTest(source=source):
                # Reset lexer state
                self.setUp()
                tokens = self.lexer.tokenize(source)

                # Should have at least one error
                self.assertTrue(self.lexer.has_errors())
                self.assertGreater(len(self.lexer.errors), 0)

                # Check error details
                error = self.lexer.errors[0]
                self.assertIn(error_msg, str(error))
                self.assertIn(error_char, str(error))

                # Should still return tokens including the error token
                error_tokens = [t for t in tokens if t.type == TokenType.UNKNOWN]
                self.assertGreater(len(error_tokens), 0)
                self.assertIn(error_char, error_tokens[0].lexeme)

                # Should continue parsing after the error
                self.assertEqual(tokens[-1].type, TokenType.EOF)

    def test_error_recovery(self):
        """Test that the lexer can recover from invalid tokens and continue parsing."""
        source = """
        var x = @invalid;
        var y = 42;  // This should still be parsed
        print(y);    // This too
        """
        tokens = self.lexer.tokenize(source)

        # Should have errors
        self.assertTrue(self.lexer.has_errors())

        # Should still parse valid tokens after the error
        var_y = next((t for t in tokens if t.lexeme == "y"), None)
        print_token = next((t for t in tokens if t.lexeme == "print"), None)

        self.assertIsNotNone(var_y)
        self.assertIsNotNone(print_token)

        # Should have proper token types
        self.assertEqual(var_y.type, TokenType.IDENTIFIER)
        self.assertEqual(print_token.type, TokenType.PRINT)

        # Should have EOF at the end
        self.assertEqual(tokens[-1].type, TokenType.EOF)

    def _assert_token_types(
        self, tokens: List[Token], expected_types: List[TokenType], msg: str = ""
    ) -> None:
        """Helper to assert token types match expected types.

        Args:
            tokens: List of tokens to check
            expected_types: List of expected token types
            msg: Optional message to include in assertion errors
        """
        self.assertEqual(
            len(tokens),
            len(expected_types) + 1,  # +1 for EOF
            f"{msg}Expected {len(expected_types) + 1} tokens (including EOF), got {len(tokens)}",
        )
        for i, (token, expected_type) in enumerate(zip(tokens, expected_types)):
            self.assertEqual(
                token.type,
                expected_type,
                f"{msg}Token {i} type mismatch: expected {expected_type}, got {token.type}",
            )

    def test_lexer_error_class(self):
        """Test that LexerError is properly defined and can be instantiated."""
        from hypercode.core.lexer import LexerError

        error = LexerError("Test error", 1, 5)
        self.assertEqual(error.message, "Test error")
        self.assertEqual(error.line, 1)
        self.assertEqual(error.column, 5)
        self.assertIn("Test error", str(error))
        self.assertIn("line 1, column 5", str(error))


if __name__ == "__main__":
    unittest.main()
