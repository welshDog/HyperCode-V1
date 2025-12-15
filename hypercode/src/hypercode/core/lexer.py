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

import re
from typing import List, Optional, Pattern, Tuple

from .tokens import Token as BaseToken
from .tokens import TokenType

# The Token class is now imported from tokens.py, but we'll keep the same interface
Token = BaseToken


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

    # Define keywords mapping
    KEYWORDS = {
        "if": TokenType.IF,
        "else": TokenType.ELSE,
        "for": TokenType.FOR,
        "while": TokenType.WHILE,
        "function": TokenType.FUN,  # Changed from FUNCTION to FUN to match tokens.py
        "return": TokenType.RETURN,
        "let": TokenType.LET,
        "const": TokenType.CONST,
        "var": TokenType.VAR,
        "true": TokenType.TRUE,
        "false": TokenType.FALSE,
        "null": TokenType.NIL,  # Changed from NULL to NIL to match tokens.py
        "print": TokenType.PRINT,
        "intent": TokenType.INTENT,
    }

    # Token specifications - ordered by priority (longer patterns first)
    TOKENS = [
        # Skip whitespace and comments (they won't be included in the token stream)
        (None, r"\s+"),  # Whitespace
        (None, r"#[^\r\n]*|//[^\r\n]*|/\*[\s\S]*?\*/"),  # Comments
        # Multi-character operators (must come before single-character ones)
        (TokenType.EQUAL_EQUAL, r"=="),
        (TokenType.BANG_EQUAL, r"!="),
        (TokenType.LESS_EQUAL, r"<="),
        (TokenType.GREATER_EQUAL, r">="),
        # Single-character operators
        (TokenType.PLUS, r"\+"),
        (TokenType.MINUS, r"-"),
        (TokenType.STAR, r"\*"),  # Handles both * and ** (handled in parser)
        (TokenType.SLASH, r"/"),
        (TokenType.EQUAL, r"="),
        (TokenType.BANG, r"!"),
        (TokenType.LESS, r"<"),
        (TokenType.GREATER, r">"),
        # String literals (handle both single and double quoted strings with escaped quotes)
        (TokenType.STRING, r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\''),
        # Numbers (handle integers, decimals, and scientific notation)
        (
            TokenType.NUMBER,
            r"\d+(?:_?\d+)*\.\d+([eE][+-]?\d+)?|\d+(?:_?\d+)*[eE][+-]?\d+|\.\d+([eE][+-]?\d+)?|0[xX][0-9a-fA-F_]+|0[bB][01_]+|0[oO]?[0-7_]+|\d+(?:_?\d+)*",
        ),
        # Punctuation
        (TokenType.LPAREN, r"\("),
        (TokenType.RPAREN, r"\)"),
        (TokenType.LBRACE, r"\{"),
        (TokenType.RBRACE, r"\}"),
        (TokenType.LBRACKET, r"\["),
        (TokenType.RBRACKET, r"\]"),
        (TokenType.COMMA, r","),
        (TokenType.SEMICOLON, r";"),
        (TokenType.COLON, r":"),
        (TokenType.DOT, r"\."),
        # Keywords and identifiers (must come after operators to avoid conflicts)
        (TokenType.IDENTIFIER, r"[a-zA-Z_]\w*"),
    ]

    def __init__(self, source: str = ""):
        """Initialize the lexer with source code.

        Args:
            source: The source code to tokenize
        """
        self.tokens: List[Token] = []
        self.pos = 0
        self.line = 1
        self.column = 1
        self.source = source

        # Compile regex patterns
        self.token_patterns: List[Tuple[TokenType, Pattern]] = []
        for token_type, pattern in self.TOKENS:
            self.token_patterns.append((token_type, re.compile(pattern)))

    def tokenize(self, source: Optional[str] = None) -> List[Token]:
        """
        Convert source code into a list of tokens.

        Args:
            source: Optional source code to tokenize. If not provided, uses the source
                   passed to the constructor.

        Returns:
            List of Token objects

        Raises:
            ValueError: If no source code is provided
        """
        if source is not None:
            self.source = source

        if not self.source:
            raise ValueError("No source code provided to tokenize")

        # Reset state
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens = []

        while self.pos < len(self.source):
            if not self._match_patterns():
                # Handle unknown characters
                self._handle_unknown()

        # Add EOF token
        self._add_token(TokenType.EOF, "")
        return self.tokens

    def _match_patterns(self) -> bool:
        """Try to match the current position against all token patterns."""
        for token_type, pattern in self.token_patterns:
            match = pattern.match(self.source, self.pos)
            if match:
                value = match.group(0)

                # Update position first for accurate line/column tracking
                self._update_position(value)

                # Skip tokens with None type (whitespace and comments)
                if token_type is None:
                    self.pos = match.end()
                    return True

                # Special handling for identifiers that might be keywords
                if token_type == TokenType.IDENTIFIER and value in self.KEYWORDS:
                    token_type = self.KEYWORDS[value]

                # Add the token
                self._add_token(token_type, value)
                self.pos = match.end()
                return True

        return False

    def _update_position(self, text: str) -> None:
        """Update line and column numbers based on the given text."""
        lines = text.splitlines(keepends=True)
        if not lines:
            return

        # Update line and column based on the last line
        last_line = lines[-1]
        if "\n" in last_line or "\r" in last_line:
            # If the last character is a newline, move to the start of the next line
            self.line += len(lines)
            self.column = 1
        else:
            # Otherwise, just update the column
            self.column += len(last_line)

        # Add any additional newlines from the text
        self.line += text.count("\n")

    def _add_token(self, token_type: TokenType, lexeme: str):
        """Add a token to the token list.

        Args:
            token_type: The type of the token.
            lexeme: The lexeme of the token (the actual text from the source).
        """
        if token_type is not None:
            # For literals, we need to set the appropriate value
            literal = None
            if token_type == TokenType.NUMBER:
                try:
                    if lexeme.lower().startswith("0x"):
                        # Parse as hexadecimal
                        literal = int(lexeme, 16)
                    elif lexeme.lower().startswith("0b"):
                        # Parse as binary
                        literal = int(lexeme[2:], 2)
                    elif lexeme.lower().startswith("0o"):
                        # Parse as octal
                        literal = int(lexeme[2:], 8)
                    else:
                        # Try to parse as int first, then as float
                        try:
                            # Handle underscores in numbers (e.g., 1_000_000)
                            clean_lexeme = lexeme.replace("_", "")
                            literal = int(clean_lexeme)
                        except ValueError:
                            try:
                                literal = float(clean_lexeme)
                            except ValueError:
                                # If we can't parse it as a number, keep literal as None
                                pass
                except Exception:
                    # If there's any error in parsing, keep literal as None
                    pass
            elif token_type == TokenType.STRING:
                # Remove the quotes from the string literal
                literal = lexeme[1:-1]
                # Handle escape sequences
                try:
                    # Use a simple approach to handle common escape sequences
                    literal = literal.encode().decode("unicode_escape")
                except:
                    # If there's an error in unescaping, keep the original
                    pass
            elif token_type in (TokenType.TRUE, TokenType.FALSE):
                literal = token_type == TokenType.TRUE
            elif token_type == TokenType.NIL:
                literal = None

            self.tokens.append(
                Token(
                    type=token_type,
                    lexeme=lexeme,
                    literal=literal,
                    line=self.line,
                    column=self.column - len(lexeme),
                )
            )

            # For debugging
            # print(f"Added token: {self.tokens[-1]}")

    def _handle_unknown(self):
        """Handle unknown characters in the source."""
        char = self.source[self.pos]
        if char.strip():  # Only raise for non-whitespace characters
            raise SyntaxError(
                f"Invalid character '{char}' at line {self.line}, column {self.column}"
            )
        # Skip the unknown character
        self.pos += 1
        self.column += 1
