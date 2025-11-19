from dataclasses import dataclass
from enum import Enum, auto
from typing import Any


class TokenType(Enum):
    # Keywords
    IF = auto()
    ELSE = auto()
    FOR = auto()
    WHILE = auto()
    FUN = auto()
    RETURN = auto()
    LET = auto()
    CONST = auto()
    VAR = auto()
    PRINT = auto()
    TRUE = auto()
    FALSE = auto()
    NIL = auto()
    CLASS = auto()
    INTENT = auto()

    # Literals
    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()

    # Operators
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    EQUAL = auto()
    EQUAL_EQUAL = auto()
    BANG = auto()
    BANG_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()

    # Punctuation
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    COMMA = auto()
    SEMICOLON = auto()
    COLON = auto()
    DOT = auto()

    # Other
    UNKNOWN = auto()
    EOF = auto()


@dataclass
class Token:
    type: TokenType
    lexeme: str
    literal: Any
    line: int
    column: int

    def __str__(self):
        return f"Token({self.type.name}, {self.lexeme!r}, literal={self.literal!r}, line={self.line}, col={self.column})"
