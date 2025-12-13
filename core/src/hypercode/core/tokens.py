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
    FUNCTION = auto()  # For function declarations
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
    RETURNS = auto()
    CONSTRAINTS = auto()
    WITH = auto()
    PARALLEL = auto()
    AGGREGATE = auto()

    # HyperCode specific keywords
    MAIN = auto()  # Main program entry point
    EMIT = auto()  # Output a value
    OUTPUT = auto()  # Output target
    INPUT = auto()  # Input operation
    STORE = auto()  # Variable assignment
    GOTO = auto()  # Goto statement
    LABEL = auto()  # Label for goto
    REPEAT = auto()  # Repeat loop
    TIMES = auto()  # Used with repeat

    # Special tokens
    COMMENT = auto()  # Comments

    # Literals
    IDENTIFIER = auto()
    STRING = auto()
    NUMBER = auto()
    FLOAT = auto()

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
    ARROW = auto()  # -> for function return types
    PIPE = auto()  # | for function chaining
    PARALLEL_OP = auto()  # || for parallel execution

    # Spatial/Visual Syntax
    LARROW = auto()  # <- for assignment
    RARROW = auto()  # -> for data flow
    LPARALLEL = auto()  # { for parallel start
    RPARALLEL = auto()  # } for parallel end
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
    AT = auto()  # @ for decorators
    HASH = auto()  # # for comments and metadata

    # AI Integration
    AI_INTENT = auto()
    AI_CONSTRAINT = auto()
    AI_EXAMPLE = auto()

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
