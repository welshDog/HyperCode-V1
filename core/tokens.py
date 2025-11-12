
# core/tokens.py

from dataclasses import dataclass
from enum import Enum

class TokenType(Enum):
    # Data types
    NUMBER = "NUMBER"
    STRING = "STRING"
    IDENTIFIER = "IDENTIFIER"
    
    # Keywords
    KEYWORD = "KEYWORD"

    # Operators
    PLUS = "PLUS"
    MINUS = "MINUS"
    MULTIPLY = "MULTIPLY"
    DIVIDE = "DIVIDE"
    ASSIGN = "ASSIGN"
    
    # Punctuation
    LPAREN = "LPAREN"
    RPAREN = "RPAREN"
    LBRACE = "LBRACE"
    RBRACE = "RBRACE"
    SEMICOLON = "SEMICOLON"
    COMMA = "COMMA"

    # Special
    EOF = "EOF" # End of File
    ILLEGAL = "ILLEGAL" # Illegal character

@dataclass
class Token:
    type: TokenType
    value: any = None
    line: int = 1
    column: int = 1

    def __repr__(self):
        return f"Token({self.type.name}, {repr(self.value)}, line={self.line}, col={self.column})"

# --- Keyword Map ---
KEYWORDS = {
    "let",
    "const",
    "fun",
    "return",
    "if",
    "else",
    "true",
    "false",
    "null",
    "print", # For simple output
}
