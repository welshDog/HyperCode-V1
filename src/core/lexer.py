from dataclasses import dataclass
from typing import Any, Dict, List

from .tokens import Token, TokenType


@dataclass
class LexerError:
    message: str
    line: int
    column: int
    length: int = 1


class Lexer:
    """
    Lexical analyzer for the HyperCode programming language.

    Converts source code into a sequence of tokens that can be parsed.
    Handles syntax highlighting, error reporting, and source mapping.

    Attributes:
        source: The source code to tokenize
        tokens: List of tokens generated from the source
        errors: List of lexing errors encountered
        start: Starting position of the current lexeme
        current: Current position in the source
        line: Current line number (1-based)
        column: Current column number (1-based)
    """

    def __init__(self, source: str):
        self.source = source
        self.tokens: List[Token] = []
        self.errors: List[LexerError] = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.column = 1

        # Keywords map to their corresponding token types
        self.KEYWORDS: Dict[str, TokenType] = {
            # Control flow
            "if": TokenType.IF,
            "else": TokenType.ELSE,
            "for": TokenType.FOR,
            "while": TokenType.WHILE,
            "match": TokenType.MATCH,
            "case": TokenType.CASE,
            "default": TokenType.DEFAULT,
            # Functions
            "fun": TokenType.FUN,
            "return": TokenType.RETURN,
            "yield": TokenType.YIELD,
            "await": TokenType.AWAIT,
            # Variables
            "let": TokenType.LET,
            "const": TokenType.CONST,
            "var": TokenType.VAR,
            # I/O
            "print": TokenType.PRINT,
            "input": TokenType.INPUT,
            # Literals
            "true": TokenType.TRUE,
            "false": TokenType.FALSE,
            "nil": TokenType.NIL,
            # OOP
            "class": TokenType.CLASS,
            "interface": TokenType.INTERFACE,
            "extends": TokenType.EXTENDS,
            "implements": TokenType.IMPLEMENTS,
            "this": TokenType.THIS,
            "super": TokenType.SUPER,
            "new": TokenType.NEW,
            # Modules
            "import": TokenType.IMPORT,
            "export": TokenType.EXPORT,
            "from": TokenType.FROM,
            "as": TokenType.AS,
            # Error handling
            "try": TokenType.TRY,
            "catch": TokenType.CATCH,
            "finally": TokenType.FINALLY,
            "throw": TokenType.THROW,
        }

    def tokenize(self) -> List[Token]:
        """
        Convert the source code into a list of tokens.

        Returns:
            List of tokens representing the source code.

        Example:
            >>> lexer = Lexer("let x = 42")
            >>> tokens = lexer.tokenize()
            >>> [t.type for t in tokens]
            [TokenType.LET, TokenType.IDENTIFIER, TokenType.EQUAL, TokenType.NUMBER, TokenType.EOF]
        """
        while not self.is_at_end():
            self.start = self.current
            try:
                self.scan_token()
            except Exception as e:
                self.error(f"Unexpected character: {e}")
                self.synchronize()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line, self.column))
        return self.tokens

    def is_at_end(self) -> bool:
        return self.current >= len(self.source)

    def scan_token(self) -> None:
        """
        Scan the next token from the source code.

        This method processes a single token and adds it to the tokens list.
        It handles all token types including keywords, identifiers, literals,
        and operators.

        Raises:
            ValueError: If an unexpected character is encountered
        """
        char = self.advance()

        # Skip whitespace
        if char in " \r\t":
            return

        # Handle newlines
        if char == "\n":
            self.line += 1
            self.column = 1
            return

        # Handle line continuation
        if char == "\\" and self.peek() == "\n":
            self.advance()  # Consume the newline
            self.line += 1
            self.column = 1
            return

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
        elif char == ":":
            self.add_token(TokenType.COLON)
        elif char == "*":
            self.add_token(TokenType.STAR)

        # Two-character tokens
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

        # Comments
        elif char == "/":
            if self.match("/"):
                while self.peek() != "\n" and not self.is_at_end():
                    self.advance()
            else:
                self.add_token(TokenType.SLASH)

        # Literals
        elif char == '"':
            self.string()
        elif self.is_digit(char):
            self.number()
        elif self.is_alpha(char):
            self.identifier()

        else:
            self.add_token(TokenType.UNKNOWN)

    def advance(self) -> str:
        self.current += 1
        self.column += 1
        return self.source[self.current - 1]

    def add_token(self, type: TokenType, literal: Any = None) -> None:
        """
        Add a new token to the tokens list.

        Args:
            type: The token type
            literal: The literal value (for numbers, strings, etc.)
        """
        text = self.source[self.start : self.current]
        self.tokens.append(
            Token(type, text, literal, self.line, self.column - len(text))
        )

    def error(self, message: str) -> None:
        """
        Record a lexing error.

        Args:
            message: Error message
        """
        self.errors.append(
            LexerError(
                message=message,
                line=self.line,
                column=self.column - (self.current - self.start),
                length=self.current - self.start,
            )
        )

    def synchronize(self) -> None:
        """
        Synchronize after an error by skipping tokens until we find a statement boundary.
        """
        while not self.is_at_end():
            if self.previous() in ";\n}":
                return
            if self.peek() in ";\n}":
                self.advance()
                return
            self.advance()

    def previous(self) -> str:
        """Return the previous character."""
        if self.current == 0:
            return "\0"
        return self.source[self.current - 1]

    def peek_next(self) -> str:
        """Look ahead two characters."""
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def match(self, expected: str) -> bool:
        if self.is_at_end():
            return False
        if self.source[self.current] != expected:
            return False
        self.current += 1
        self.column += 1
        return True

    def peek(self) -> str:
        if self.is_at_end():
            return "\0"
        return self.source[self.current]

    def peek_next(self) -> str:
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def string(self) -> None:
        """Parse a string literal."""
        delimiter = self.previous()  # Should be '"'
        value = []

        while True:
            if self.is_at_end():
                self.error("Unterminated string")
                return

            char = self.advance()

            if char == "\\":
                # Handle escape sequences
                if self.is_at_end():
                    self.error("Unterminated escape sequence")
                    return

                # Process escape sequence
                esc = self.advance()
                if esc == "n":
                    value.append("\n")
                elif esc == "t":
                    value.append("\t")
                elif esc == "r":
                    value.append("\r")
                elif esc == "b":
                    value.append("\b")
                elif esc == "f":
                    value.append("\f")
                elif esc in "\"'\\":
                    value.append(esc)
                elif esc == "x":
                    # Hex escape: \xHH
                    if not (
                        self.is_hex_digit(self.peek())
                        and self.is_hex_digit(self.peek_next())
                    ):
                        self.error("Invalid hex escape sequence")
                        return
                    hex_str = self.advance() + self.advance()
                    value.append(chr(int(hex_str, 16)))
                else:
                    self.error(f"Invalid escape sequence: \\{esc}")
                    value.append(esc)

            elif char == delimiter:
                break

            elif char == "\n":
                if delimiter == '"':
                    self.error("Unterminated string")
                    return
                self.line += 1
                self.column = 1
                value.append("\n")

            else:
                value.append(char)

        self.add_token(TokenType.STRING, "".join(value))

    def is_digit(self, char: str) -> bool:
        """Check if a character is a digit (0-9)."""
        return char.isdigit()

    def number(self) -> None:
        """Parse a number literal (integer or float)."""
        # Handle hexadecimal numbers (0x...)
        if self.peek() == "0" and self.peek_next().lower() == "x":
            self.advance()  # Consume 'x'
            self.advance()  # Consume first digit after 'x'
            while self.is_hex_digit(self.peek()):
                self.advance()
            hex_str = self.source[self.start + 2 : self.current]
            self.add_token(TokenType.NUMBER, int(hex_str, 16))
            return

        # Handle binary numbers (0b...)
        if self.peek() == "0" and self.peek_next().lower() == "b":
            self.advance()  # Consume 'b'
            self.advance()  # Consume first digit after 'b'
            while self.peek() in "01_":
                if self.peek() != "_":
                    self.advance()
            bin_str = self.source[self.start + 2 : self.current].replace("_", "")
            self.add_token(TokenType.NUMBER, int(bin_str, 2))
            return

        # Handle decimal numbers
        while self.peek().isdigit() or self.peek() == "_":
            self.advance()

        # Look for a fractional part
        if self.peek() == "." and self.is_digit(self.peek_next()):
            # Consume the "."
            self.advance()

            while self.peek().isdigit() or self.peek() == "_":
                if self.peek() != "_":
                    self.advance()

        # Handle scientific notation
        if self.peek().lower() == "e":
            self.advance()
            if self.peek() in "+-":
                self.advance()
            while self.peek().isdigit():
                self.advance()

        # Parse the number, ignoring underscores
        num_str = self.source[self.start : self.current].replace("_", "")
        self.add_token(
            TokenType.NUMBER,
            (
                float(num_str)
                if "." in num_str or "e" in num_str.lower()
                else int(num_str)
            ),
        )

    def is_alpha(self, char: str) -> bool:
        """Check if a character is alphabetic or underscore."""
        return char.isalpha() or char == "_" or char == "$"

    def is_alphanumeric(self, char: str) -> bool:
        """Check if a character is alphanumeric or underscore."""
        return self.is_alpha(char) or self.is_digit(char)

    def is_hex_digit(self, char: str) -> bool:
        """Check if a character is a valid hexadecimal digit."""
        return char.isdigit() or char.lower() in "abcdef"

    def identifier(self) -> None:
        """Parse an identifier or keyword."""
        while self.is_alphanumeric(self.peek()):
            self.advance()

        text = self.source[self.start : self.current]

        # Check for contextual keywords (not reserved in all contexts)
        if text in self.KEYWORDS:
            token_type = self.KEYWORDS[text]
        else:
            token_type = TokenType.IDENTIFIER

        self.add_token(token_type)

        # Handle special cases like 'not in', 'is not'
        if (
            text == "is"
            and self.peek() == " "
            and self.source.startswith("not", self.current + 1)
        ):
            # Handle 'is not' operator
            lookahead = self.current + 1
            while lookahead < len(self.source) and self.source[lookahead].isspace():
                lookahead += 1

            if self.source.startswith("not", lookahead):
                # Replace 'is' with 'is not' token
                self.tokens.pop()  # Remove the 'is' token
                self.current = lookahead + 3  # Skip 'not'
                self.add_token(TokenType.IS_NOT)
