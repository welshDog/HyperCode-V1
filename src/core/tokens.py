# src/core/tokens.py
"""
Token types and definitions for the HyperCode language.

This module defines all token types and the Token class used in the HyperCode language.
"""

from enum import Enum
from typing import Any, Dict, Optional


class TokenType(Enum):
    """Enumeration of all token types in the HyperCode language."""
    
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

    # One or two character tokens
    BANG_EQUAL = "!="
    EQUAL_EQUAL = "=="
    LESS_EQUAL = "<="
    GREATER_EQUAL = ">="
    ARROW = "=>"

    # Literals
    IDENTIFIER = "IDENTIFIER"
    STRING = "STRING"
    NUMBER = "NUMBER"
    DOCSTRING = "DOCSTRING"
    
    # Keywords
    AND = "and"
    BREAK = "break"
    CLASS = "class"
    CONTINUE = "continue"
    ELSE = "else"
    FALSE = "false"
    FOR = "for"
    FUN = "fun"
    FUNC = "func"
    IF = "if"
    NIL = "nil"
    OR = "or"
    PRINT = "print"
    RETURN = "return"
    SUPER = "super"
    THIS = "this"
    TRUE = "true"
    VAR = "var"
    WHILE = "while"

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
        self,
        type: TokenType,
        lexeme: str,
        literal: Any,
        line: int,
        column: int
    ) -> None:
        """Initialize a new token with the given properties."""
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
        self.column = column
    
    def __str__(self) -> str:
        """Return a string representation of the token."""
        return f"{self.type} {self.lexeme} {self.literal}"
    
    def __repr__(self) -> str:
        """Return a detailed string representation of the token for debugging."""
        return f"<Token {self.type} '{self.lexeme}' at {self.line}:{self.column}>"


# Keywords mapping for quick lookup
KEYWORDS: Dict[str, TokenType] = {
    'and': TokenType.AND,
    'break': TokenType.BREAK,
    'class': TokenType.CLASS,
    'continue': TokenType.CONTINUE,
    'else': TokenType.ELSE,
    'false': TokenType.FALSE,
    'for': TokenType.FOR,
    'fun': TokenType.FUN,
    'func': TokenType.FUNC,
    'if': TokenType.IF,
    'nil': TokenType.NIL,
    'or': TokenType.OR,
    'print': TokenType.PRINT,
    'return': TokenType.RETURN,
    'super': TokenType.SUPER,
    'this': TokenType.THIS,
    'true': TokenType.TRUE,
    'var': TokenType.VAR,
    'while': TokenType.WHILE,
}
