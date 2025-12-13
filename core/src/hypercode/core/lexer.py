# Copyright 2025 welshDog (Lyndz Williams)
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Core HyperCode language implementation - Lexer

This module implements the lexical analyzer for the HyperCode language.
It converts source code into a sequence of tokens for further processing.
"""

from typing import List, Optional, Any, Dict
from dataclasses import dataclass
from .tokens import Token, TokenType


@dataclass
class LexerError(Exception):
    """Exception raised for errors in the lexer."""

    message: str
    line: int
    column: int

    def __init__(self, message: str, line: int, column: int):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(f"{message} at line {line}, column {column}")


class Lexer:
    """Lexical analyzer for the HyperCode language."""

    def __init__(self, source: str = ""):
        """Initialize the lexer with source code.

        Args:
            source: The source code to tokenize
        """
        self.source = source
        self.tokens: List[Token] = []
        self.errors: List[LexerError] = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.column = 1

    def tokenize(self, source: Optional[str] = None) -> List[Token]:
        """Convert source code into a list of tokens.

        Args:
            source: Optional source code to tokenize. If not provided,
                   uses the source passed to the constructor.

        Returns:
            List of Token objects, always ending with an EOF token
        """
        if source is not None:
            self.source = source

        self.tokens = []
        self.errors = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.column = 1

        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        # Add EOF token
        self.add_token(TokenType.EOF, "")
        return self.tokens

    # Add other Lexer methods here (scan_token, add_token, etc.)

    def is_at_end(self) -> bool:
        """Check if we've consumed all characters."""
        return self.current >= len(self.source)


if __name__ == "__main__":
    # Test code
    lexer = Lexer("main { }")
    tokens = lexer.tokenize()
    for token in tokens:
        print(token)


class LexerError(Exception):
    """Exception raised for errors in the lexer."""

    def __init__(self, message: str, line: int, column: int):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(f"{message} at line {line}, column {column}")


class Lexer:
    """
    Lexical analyzer for the HyperCode language.

    Converts source code into a sequence of tokens that can be processed
    by the parser.
    """

    # We'll handle tokens directly in scan_token() instead of using a TOKENS list

    def __init__(self, source: str = ""):
        """Initialize the lexer with source code.

        Args:
            source: The source code to tokenize
        """
        self.source = source
        self.tokens: List[Token] = []
        self.errors: List[LexerError] = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.column = 1

    def tokenize(self, source: Optional[str] = None) -> List[Token]:
        """Convert source code into a list of tokens.

        Args:
            source: Optional source code to tokenize. If not provided,
                   uses the source passed to the constructor.

        Returns:
            List of Token objects, always ending with an EOF token
        """
        if source is not None:
            self.source = source

        self.tokens = []
        self.errors = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.column = 1

        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        # Add EOF token
        self.add_token(TokenType.EOF, "")
        return self.tokens

    def scan_token(self) -> None:
        """Scan the next token from the source."""
        # Skip whitespace
        while not self.is_at_end() and self.peek() in " \t\r":
            self.advance()

        if self.is_at_end():
            return

        char = self.advance()
        self.start = self.current - 1  # Set start to the beginning of the token

        # Single-character tokens
        if char == "(":
            self.add_token(TokenType.LPAREN)
        elif char == ")":
            self.add_token(TokenType.RPAREN)
        elif char == "{":
            self.add_token(TokenType.LBRACE)
        elif char == "}":
            self.add_token(TokenType.RBRACE)
        elif char == "[":
            # Check for [ow:label] syntax
            if (
                self.peek() == "o"
                and self.peek_next() == "w"
                and self.source[self.current] == ":"
            ):
                # Skip 'ow:' part
                while self.peek() != "]" and not self.is_at_end():
                    self.advance()
                if not self.is_at_end() and self.peek() == "]":
                    self.advance()  # Consume ']'
                    self.add_token(
                        TokenType.IDENTIFIER,
                        self.source[self.start + 1 : self.current - 1],
                    )
            else:
                self.add_token(TokenType.LBRACKET)
        elif char == "]":
            self.add_token(TokenType.RBRACKET)
        elif char == ",":
            self.add_token(TokenType.COMMA)
        elif char == ".":
            self.add_token(TokenType.DOT)
        elif char == "-":
            self.add_token(TokenType.MINUS)
        elif char == "+":
            self.add_token(TokenType.PLUS)
        elif char == ";":
            self.add_token(TokenType.SEMICOLON)
        elif char == "*":
            self.add_token(TokenType.STAR)
        elif char == ":":
            self.add_token(TokenType.COLON)
        elif char == "!":
            self.add_token(TokenType.BANG_EQUAL if self.match("=") else TokenType.BANG)
        elif char == "=":
            self.add_token(
                TokenType.EQUAL_EQUAL if self.match("=") else TokenType.EQUAL
            )
        elif char == "<":
            self.add_token(TokenType.LESS_EQUAL if self.match("=") else TokenType.LESS)
        elif char == ">":
            self.add_token(
                TokenType.GREATER_EQUAL if self.match("=") else TokenType.GREATER
            )
        elif char == '"' or char == "'":
            self.string(char)
        elif char.isdigit():
            self.number()
        elif char.isalpha() or char == "_":
            self.identifier()
        elif char == "/":
            if self.match("/"):
                # Skip comments
                while self.peek() != "\n" and not self.is_at_end():
                    self.advance()
            else:
                self.add_token(TokenType.SLASH)
        elif char == "\n":
            self.line += 1
            self.column = 1
        else:
            # Skip unknown characters for now
            pass

    def string(self, quote: str) -> None:
        """Scan a string literal."""
        start_line = self.line
        start_col = self.column
        value = ""

        while self.peek() != quote and not self.is_at_end():
            if self.peek() == "\n":
                self.line += 1
                self.column = 0
            value += self.advance()

        if self.is_at_end():
            self.error("Unterminated string", start_line, start_col)
            return

        # The closing quote
        self.advance()

        # Add the string token without the surrounding quotes
        self.add_token(TokenType.STRING, value[1:-1])

    def number(self) -> None:
        """Scan a number literal."""
        while self.peek().isdigit():
            self.advance()

        # Look for a fractional part
        if self.peek() == "." and self.peek_next().isdigit():
            # Consume the "."
            self.advance()

            while self.peek().isdigit():
                self.advance()

        # Look for exponent
        if self.peek().lower() == "e":
            self.advance()  # Consume 'e' or 'E'
            if self.peek() in "+-":
                self.advance()  # Consume sign

            if not self.peek().isdigit():
                self.error("Expected digit after exponent")
                return

            while self.peek().isdigit():
                self.advance()

        # Convert to int or float
        num_str = self.source[self.start : self.current]
        if "." in num_str or "e" in num_str.lower():
            self.add_token(TokenType.NUMBER, float(num_str))
        else:
            self.add_token(TokenType.NUMBER, int(num_str))

    def identifier(self) -> None:
        """Scan an identifier or keyword."""
        while not self.is_at_end() and (self.peek().isalnum() or self.peek() == "_"):
            self.advance()

        # Check if the identifier is a reserved keyword
        text = self.source[self.start : self.current]
        token_type = self.KEYWORDS.get(text.lower(), TokenType.IDENTIFIER)
        self.add_token(token_type)

    def match(self, expected: str) -> bool:
        """Match the next character if it matches the expected character."""
        if self.is_at_end():
            return False
        if self.source[self.current] != expected:
            return False

        self.current += 1
        self.column += 1
        return True

    def peek(self) -> str:
        """Look at the next character without consuming it."""
        if self.is_at_end():
            return "\0"
        return self.source[self.current]

    def peek_next(self) -> str:
        """Look at the character after the next one without consuming it."""
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def advance(self) -> str:
        """Consume and return the next character."""
        if self.is_at_end():
            return "\0"

        char = self.source[self.current]
        self.current += 1
        self.column += 1
        return char

    def add_token(self, token_type: TokenType, literal: Any = None) -> None:
        """Add a new token to the tokens list."""
        text = self.source[self.start : self.current]
        if literal is None:
            literal = text.strip()
        self.tokens.append(Token(token_type, text, literal, self.line, self.column))
        self.column += len(text)

    def error(
        self, message: str, line: Optional[int] = None, column: Optional[int] = None
    ) -> None:
        """Record a lexer error.

        Args:
            message: The error message
            line: The line number where the error occurred (defaults to current line)
            column: The column number where the error occurred (defaults to current column)
        """
        error_line = line if line is not None else self.line
        error_col = column if column is not None else self.column
        self.errors.append(LexerError(message, error_line, error_col))

    def is_at_end(self) -> bool:
        """Check if we've consumed all characters."""
        return self.current >= len(self.source)

    KEYWORDS = {
        # Standard keywords
        "if": TokenType.IF,
        "else": TokenType.ELSE,
        "for": TokenType.FOR,
        "while": TokenType.WHILE,
        "fun": TokenType.FUN,
        "function": TokenType.FUNCTION,
        "return": TokenType.RETURN,
        "let": TokenType.LET,
        "const": TokenType.CONST,
        "var": TokenType.VAR,
        "print": TokenType.PRINT,
        "true": TokenType.TRUE,
        "false": TokenType.FALSE,
        "nil": TokenType.NIL,
        "class": TokenType.CLASS,
        # HyperCode specific keywords
        "main": TokenType.MAIN,
        "emit": TokenType.EMIT,
        "output": TokenType.OUTPUT,
        "input": TokenType.INPUT,
        "store": TokenType.STORE,
        "goto": TokenType.GOTO,
        "label": TokenType.LABEL,
        "repeat": TokenType.REPEAT,
        "times": TokenType.TIMES,
    }
