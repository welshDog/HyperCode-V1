# src/core/tokens.py
"""
HyperCode Token Types and Definitions

Defines all token types used in the HyperCode language.
"""

from enum import Enum
from typing import Any


class TokenType(Enum):
    # Single-character tokens
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"
    COMMA = ","
    DOT = "."
    MINUS = "-"
    PLUS = "+"
    SEMICOLON = ";"
    SLASH = "/"
    STAR = "*"
    PERCENT = "%"
    BANG = "!"
    EQUAL = "="
    LESS = "<"
    GREATER = ">"
    COLON = ":"
    QUESTION = "?"
    PIPE = "|"
    AT = "@"

    # One or two character tokens
    BANG_EQUAL = "!="
    EQUAL_EQUAL = "=="
    LESS_EQUAL = "<="
    GREATER_EQUAL = ">="
    ARROW = "->"

    # Literals
    IDENTIFIER = "IDENTIFIER"
    STRING = "STRING"
    NUMBER = "NUMBER"

    # Keywords
    AND = "and"
    BLOCK = "block"
    BREAK = "break"
    CLASS = "class"
    CONTINUE = "continue"
    ELSE = "else"
    FALSE = "false"
    FOR = "for"
    FUNC = "func"
    IF = "if"
    NIL = "nil"
    OR = "or"
    PRINT = "print"
    RETURN = "return"
    SUPER = "super"
    THIS = "this"
    TRUE = "true"
    LET = "let"
    WHILE = "while"
    DOCSTRING = "DOCSTRING"

    # Special tokens
    EOF = "EOF"
    ERROR = "ERROR"


class Token:
    """
    Represents a token in the HyperCode language.

    Attributes:
        type: The type of the token (from TokenType)
        lexeme: The actual text that was matched
        literal: The literal value (for numbers, strings, etc.)
        line: The line number where the token appears (1-based)
        column: The column number where the token starts (1-based)
    """

    def __init__(
        self, type: TokenType, lexeme: str, literal: Any, line: int, column: int
    ):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
        self.column = column

    def __str__(self) -> str:
        return f"{self.type} {self.lexeme} {self.literal}"

    def __repr__(self) -> str:
        return f"<Token {self.type} '{self.lexeme}' at {self.line}:{self.column}>"


# Keywords mapping for quick lookup
KEYWORDS = {
    "and": TokenType.AND,
    "block": TokenType.BLOCK,
    "break": TokenType.BREAK,
    "class": TokenType.CLASS,
    "continue": TokenType.CONTINUE,
    "else": TokenType.ELSE,
    "false": TokenType.FALSE,
    "for": TokenType.FOR,
    "func": TokenType.FUNC,
    "if": TokenType.IF,
    "nil": TokenType.NIL,
    "or": TokenType.OR,
    "print": TokenType.PRINT,
    "return": TokenType.RETURN,
    "super": TokenType.SUPER,
    "this": TokenType.THIS,
    "true": TokenType.TRUE,
    "let": TokenType.LET,
    "while": TokenType.WHILE,
}
