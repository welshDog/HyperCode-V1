from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Dict, List, Optional, Union


class TokenType(Enum):
    # Keywords
    IF = auto()
    ELSE = auto()
    FOR = auto()
    WHILE = auto()
    FUNCTION = auto()
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

    # HyperCode specific
    THEN = auto()
    IN = auto()
    MATCH = auto()
    WITH = auto()
    IMPORT = auto()
    EXPORT = auto()
    AS = auto()
    TYPE = auto()
    INTERFACE = auto()

    # Literals
    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()
    FLOAT = auto()
    BOOLEAN = auto()

    # Complex literals
    LIST = auto()
    DICT = auto()
    TUPLE = auto()

    # Operators
    # Arithmetic
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    FLOOR_DIV = auto()
    MODULO = auto()
    POWER = auto()

    # Comparison
    EQUAL = auto()
    EQUAL_EQUAL = auto()
    BANG = auto()
    BANG_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()

    # Logical
    AND = auto()
    OR = auto()
    NOT = auto()

    # Bitwise
    BIT_AND = auto()
    BIT_OR = auto()
    BIT_XOR = auto()
    BIT_NOT = auto()
    SHIFT_LEFT = auto()
    SHIFT_RIGHT = auto()

    # Assignment
    PLUS_EQUAL = auto()
    MINUS_EQUAL = auto()
    STAR_EQUAL = auto()
    SLASH_EQUAL = auto()

    # Type operators
    IS = auto()
    IS_NOT = auto()
    IN = auto()
    NOT_IN = auto()

    # Punctuation
    LPAREN = auto()
    RPAREN = auto()
    LBRACE = auto()
    RBRACE = auto()
    LBRACKET = auto()
    RBRACKET = auto()
    COMMA = auto()
    COLON = auto()
    SEMICOLON = auto()
    DOT = auto()
    RANGE = auto()
    ARROW = auto()
    ELLIPSIS = auto()

    # Special
    INDENT = auto()
    DEDENT = auto()
    NEWLINE = auto()
    EOF = auto()
    SEMICOLON = auto()
    COLON = auto()
    DOT = auto()

    # Other
    UNKNOWN = auto()
    EOF = auto()


@dataclass
class Token:
    """Represents a token in the HyperCode language."""

    type: TokenType
    lexeme: str
    literal: Optional[Any] = None
    line: int = 0
    column: int = 0
    end_line: Optional[int] = None
    end_column: Optional[int] = None

    def __post_init__(self):
        if self.end_line is None:
            self.end_line = self.line
        if self.end_column is None:
            self.end_column = self.column + len(self.lexeme)

    def __str__(self) -> str:
        literal = f" '{self.literal}'" if self.literal is not None else ""
        return f"{self.type.name}({self.line}:{self.column}-{self.end_line}:{self.end_column}): '{self.lexeme}'{literal}"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> Dict[str, Any]:
        """Convert token to a dictionary for serialization."""
        return {
            "type": self.type.name,
            "lexeme": self.lexeme,
            "literal": self.literal,
            "line": self.line,
            "column": self.column,
            "end_line": self.end_line,
            "end_column": self.end_column,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Token":
        """Create a token from a dictionary."""
        return cls(
            type=TokenType[data["type"]],
            lexeme=data["lexeme"],
            literal=data.get("literal"),
            line=data["line"],
            column=data["column"],
            end_line=data.get("end_line"),
            end_column=data.get("end_column"),
        )
