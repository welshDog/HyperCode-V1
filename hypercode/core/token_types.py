from enum import Enum
from typing import Dict, List, Optional, Tuple, Union, Any

class TokenType(Enum):
    # Special tokens
    EOF = 'EOF'
    
    # Literals
    IDENTIFIER = 'IDENTIFIER'
    NUMBER = 'NUMBER'
    STRING = 'STRING'
    
    # Keywords
    LET = 'let'
    CONST = 'const'
    VAR = 'var'  # For variable declarations
    IF = 'if'
    ELSE = 'else'
    FOR = 'for'
    WHILE = 'while'
    FUNCTION = 'function'
    RETURN = 'return'
    PRINT = 'print'  # For print statements
    TRUE = 'true'
    FALSE = 'false'
    NULL = 'null'
    
    # Operators
    PLUS = '+'
    MINUS = '-'
    STAR = '*'
    SLASH = '/'
    PERCENT = '%'
    STAR_STAR = '**'  # For exponentiation
    SLASH_SLASH = '//'  # For integer division
    BANG = '!'
    EQUAL = '='
    EQUAL_EQUAL = '=='
    BANG_EQUAL = '!='
    LESS = '<'
    LESS_EQUAL = '<='
    GREATER = '>'
    GREATER_EQUAL = '>='
    ARROW = '->'  # For function return type annotation
    
    # Punctuation
    LPAREN = '('
    RPAREN = ')'
    LBRACE = '{'  # LEFT_BRACE
    RBRACE = '}'  # RIGHT_BRACE
    LBRACKET = '['
    RBRACKET = ']'
    SEMICOLON = ';'
    COMMA = ','
    DOT = '.'
    COLON = ':'
    QUESTION = '?'
    
    # Other
    COMMENT = 'COMMENT'
    WHITESPACE = 'WHITESPACE'
    UNKNOWN = 'UNKNOWN'  # For invalid characters
    
    def __str__(self):
        return self.name

# Create a mapping from string values to token types for the lexer
TOKEN_MAP: Dict[str, TokenType] = {t.value: t for t in TokenType}
