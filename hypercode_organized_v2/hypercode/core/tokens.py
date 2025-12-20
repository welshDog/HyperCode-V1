"""
HyperCode Token Definitions

This module defines the TokenType enum and Token class used by the HyperCode lexer.
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Any, Optional, Dict, List, Union


class TokenType(Enum):
    """Enumeration of all token types in the HyperCode language."""
    
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
    END = auto()  # Added for 'end' keyword
    
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

    # Operators
    BANG = auto()  # ! operator
    
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
    MULTIPLY = auto()
    DIVIDE = auto()
    MODULO = auto()
    EXPONENT = auto()
    STAR = auto()  # Alias for MULTIPLY for compatibility
    
    # Comparison
    EQUAL = auto()
    NOT_EQUAL = auto()
    LESS = auto()
    LESS_EQUAL = auto()
    GREATER = auto()
    GREATER_EQUAL = auto()
    
    # Logical
    AND = auto()
    OR = auto()
    NOT = auto()
    
    # Bitwise
    BITWISE_AND = auto()
    BITWISE_OR = auto()
    BITWISE_XOR = auto()
    BITWISE_NOT = auto()
    LEFT_SHIFT = auto()
    RIGHT_SHIFT = auto()
    
    # Assignment
    ASSIGN = auto()
    PLUS_ASSIGN = auto()
    MINUS_ASSIGN = auto()
    MULTIPLY_ASSIGN = auto()
    DIVIDE_ASSIGN = auto()
    MODULO_ASSIGN = auto()
    EXPONENT_ASSIGN = auto()
    
    # Delimiters
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    COMMA = auto()
    DOT = auto()
    COLON = auto()
    SEMICOLON = auto()
    ARROW = auto()
    RANGE = auto()
    
    # Special
    NEWLINE = auto()
    INDENT = auto()
    DEDENT = auto()
    EOF = auto()
    
    # Error
    ERROR = auto()


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
        """Initialize end_line and end_column if not provided."""
        if self.end_line is None:
            self.end_line = self.line
        if self.end_column is None:
            self.end_column = self.column + len(self.lexeme)
    
    def __str__(self) -> str:
        """Return a string representation of the token."""
        return f"{self.type.name} {self.lexeme} {self.literal}"
    
    def __repr__(self) -> str:
        """Return a detailed string representation of the token."""
        return (f"Token(type={self.type.name}, lexeme='{self.lexeme}', "
                f"literal={self.literal}, line={self.line}, column={self.column}, "
                f"end_line={self.end_line}, end_column={self.end_column})")
    
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
    def from_dict(cls, data: Dict[str, Any]) -> 'Token':
        """Create a token from a dictionary."""
        return cls(
            type=TokenType[data["type"]],
            lexeme=data["lexeme"],
            literal=data.get("literal"),
            line=data.get("line", 0),
            column=data.get("column", 0),
            end_line=data.get("end_line"),
            end_column=data.get("end_column"),
        )
