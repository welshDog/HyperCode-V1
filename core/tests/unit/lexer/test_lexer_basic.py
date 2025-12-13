"""
Unit tests for the HyperCode lexer's basic functionality.
"""

from hypercode.core.lexer import Lexer
from hypercode.core.tokens import TokenType


class TestLexerBasic:
    """Test basic lexer functionality."""

    def test_empty_source(self):
        """Test that an empty source returns only EOF token."""
        lexer = Lexer("")
        tokens = lexer.scan_tokens()
        assert len(tokens) == 1
        assert tokens[0].type == TokenType.EOF

    def test_whitespace_handling(self):
        """Test that whitespace is properly handled and ignored."""
        lexer = Lexer("  \t\n\r  ")
        tokens = lexer.scan_tokens()
        # Should only have EOF token
        assert len(tokens) == 1
        assert tokens[0].type == TokenType.EOF

    def test_single_character_tokens(self):
        """Test recognition of single-character tokens."""
        source = "( ) { } , . - + ; / *"
        expected_types = [
            TokenType.LEFT_PAREN,
            TokenType.RIGHT_PAREN,
            TokenType.LEFT_BRACE,
            TokenType.RIGHT_BRACE,
            TokenType.COMMA,
            TokenType.DOT,
            TokenType.MINUS,
            TokenType.PLUS,
            TokenType.SEMICOLON,
            TokenType.SLASH,
            TokenType.STAR,
            TokenType.EOF,
        ]

        lexer = Lexer(source)
        tokens = lexer.scan_tokens()
        assert len(tokens) == len(expected_types)

        for token, expected_type in zip(tokens, expected_types):
            assert token.type == expected_type

    def test_comments_are_ignored(self):
        """Test that comments are properly ignored."""
        source = """
        // This is a comment
        x = 5 // Another comment
        /* Multi-line
           comment */
        y = 10
        """
        lexer = Lexer(source)
        tokens = lexer.scan_tokens()
        # Should have: x, =, 5, y, =, 10, EOF
        assert len(tokens) == 7
        assert tokens[0].type == TokenType.IDENTIFIER and tokens[0].lexeme == "x"
        assert tokens[1].type == TokenType.EQUAL
        assert tokens[2].type == TokenType.NUMBER and tokens[2].literal == 5
        assert tokens[3].type == TokenType.IDENTIFIER and tokens[3].lexeme == "y"
        assert tokens[4].type == TokenType.EQUAL
        assert tokens[5].type == TokenType.NUMBER and tokens[5].literal == 10

    def test_string_literals(self):
        """Test string literal tokenization."""
        source = '"hello" "world" "escaped "quote""'
        lexer = Lexer(source)
        tokens = lexer.scan_tokens()

        # Should have 3 string literals + EOF
        assert len(tokens) == 4
        assert tokens[0].type == TokenType.STRING and tokens[0].literal == "hello"
        assert tokens[1].type == TokenType.STRING and tokens[1].literal == "world"
        assert (
            tokens[2].type == TokenType.STRING
            and tokens[2].literal == 'escaped "quote"'
        )

    def test_number_literals(self):
        """Test number literal tokenization."""
        source = "123 45.67 .5 123. 1e10 1e-5 2.5e+3"
        lexer = Lexer(source)
        tokens = lexer.scan_tokens()

        # Should have 7 number literals + EOF
        assert len(tokens) == 8
        assert tokens[0].type == TokenType.NUMBER and tokens[0].literal == 123
        assert tokens[1].type == TokenType.NUMBER and tokens[1].literal == 45.67
        assert tokens[2].type == TokenType.NUMBER and tokens[2].literal == 0.5
        assert tokens[3].type == TokenType.NUMBER and tokens[3].literal == 123.0
        assert tokens[4].type == TokenType.NUMBER and tokens[4].literal == 1e10
        assert tokens[5].type == TokenType.NUMBER and tokens[5].literal == 1e-5
        assert tokens[6].type == TokenType.NUMBER and tokens[6].literal == 2.5e3

    def test_identifiers_and_keywords(self):
        """Test identifier and keyword recognition."""
        source = "var x = 5; if x > 3 { print(x); } else { return x; }"
        lexer = Lexer(source)
        tokens = lexer.scan_tokens()

        expected_types = [
            TokenType.VAR,
            TokenType.IDENTIFIER,
            TokenType.EQUAL,
            TokenType.NUMBER,
            TokenType.SEMICOLON,
            TokenType.IF,
            TokenType.IDENTIFIER,
            TokenType.GREATER,
            TokenType.NUMBER,
            TokenType.LEFT_BRACE,
            TokenType.PRINT,
            TokenType.LEFT_PAREN,
            TokenType.IDENTIFIER,
            TokenType.RIGHT_PAREN,
            TokenType.SEMICOLON,
            TokenType.RIGHT_BRACE,
            TokenType.ELSE,
            TokenType.LEFT_BRACE,
            TokenType.RETURN,
            TokenType.IDENTIFIER,
            TokenType.SEMICOLON,
            TokenType.RIGHT_BRACE,
            TokenType.EOF,
        ]

        assert len(tokens) == len(expected_types)
        for token, expected_type in zip(tokens, expected_types):
            assert token.type == expected_type

    def test_error_handling(self):
        """Test error handling for invalid tokens."""
        source = "@ # $"
        lexer = Lexer(source)
        tokens = lexer.scan_tokens()

        # Should have errors for @ and #, but still tokenize $ and EOF
        assert len(lexer.errors) == 2
        assert tokens[0].type == TokenType.UNKNOWN
        assert tokens[1].type == TokenType.UNKNOWN
        assert tokens[2].type == TokenType.EOF

        # Check error messages
        assert "Unexpected character" in lexer.errors[0].message
        assert lexer.errors[0].line == 1 and lexer.errors[0].column == 1
        assert "Unexpected character" in lexer.errors[1].message
        assert lexer.errors[1].line == 1 and lexer.errors[1].column == 3
