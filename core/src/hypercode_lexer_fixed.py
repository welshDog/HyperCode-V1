HyperCode Lexer - Enhanced Version
Supports numbers, identifiers, and basic expressions
"""

from dataclasses import dataclass
from enum import Enum
from typing import List, Dict, Optional
import sys

class TokenType(Enum):
    # Core operations
    PUSH = "PUSH"        # >
    POP = "POP"          # <
    INCR = "INCR"        # +
    DECR = "DECR"        # -
    OUTPUT = "OUTPUT"    # .
    INPUT = "INPUT"      # ,
    LOOP_START = "LOOP_START"  # [
    LOOP_END = "LOOP_END"      # ]
    STRING = "STRING"    # "..." or '...'
    COMMENT = "COMMENT"  # ;
    
    # New token types
    NUMBER = "NUMBER"        # 123, 3.14, etc.
    IDENTIFIER = "IDENTIFIER" # variable names
    ASSIGN = "ASSIGN"        # =
    PLUS = "PLUS"            # +
    MINUS = "MINUS"          # -
    MULTIPLY = "MULTIPLY"    # *
    DIVIDE = "DIVIDE"        # /
    LPAREN = "LPAREN"        # (
    RPAREN = "RPAREN"        # )
    
    # Control flow
    IF = "IF"
    ELSE = "ELSE"
    WHILE = "WHILE"
    FUNC = "FUNC"
    RETURN = "RETURN"
    
    # Literals
    TRUE = "TRUE"
    FALSE = "FALSE"
    NULL = "NULL"
    
    # Special
    EOF = "EOF"
    UNKNOWN = "UNKNOWN"

@dataclass
class Token:
    type: TokenType
    value: str
    raw_value: str
    position: int
    line: int
    column: int

    def __repr__(self) -> str:
        return f"Token({self.type.value}, '{self.value}')"

class HyperCodeLexer:
    def __init__(self, text: str):
        self.text = text
        self.position = 0
        self.line = 1
        self.column = 1
        self.current_char = self.text[0] if text else None
        
        # Keywords mapping
        self.KEYWORDS = {
            'if': TokenType.IF,
            'else': TokenType.ELSE,
            'while': TokenType.WHILE,
            'func': TokenType.FUNC,
            'return': TokenType.RETURN,
            'true': TokenType.TRUE,
            'false': TokenType.FALSE,
            'null': TokenType.NULL,
        }

    def _error(self, message: str):
        raise Exception(f"Lexer error at {self.line}:{self.column}: {message}")

    def _advance(self):
        self.position += 1
        if self.position < len(self.text):
            self.current_char = self.text[self.position]
            self.column += 1
        else:
            self.current_char = None

    def _skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            if self.current_char == '\n':
                self.line += 1
                self.column = 0
            self._advance()

    def _is_digit(self, char: str) -> bool:
        return char is not None and '0' <= char <= '9'

    def _is_alpha(self, char: str) -> bool:
        return char is not None and (char.isalpha() or char == '_')

    def _is_alnum(self, char: str) -> bool:
        return char is not None and (char.isalnum() or char == '_')

    def _read_number(self) -> Token:
        start_pos = self.position
        start_line = self.line
        start_col = self.column
        
        value = ''
        has_decimal = False
        
        while self.current_char is not None:
            if self._is_digit(self.current_char):
                value += self.current_char
                self._advance()
            elif self.current_char == '.' and not has_decimal:
                has_decimal = True
                value += self.current_char
                self._advance()
                if self.current_char is None or not self._is_digit(self.current_char):
                    self._error("Invalid number format")
            else:
                break
        
        if value.endswith('.'):
            self._error("Invalid number format")
        
        return Token(
            type=TokenType.NUMBER,
            value=value,
            raw_value=value,
            position=start_pos,
            line=start_line,
            column=start_col
        )

    def _read_identifier(self) -> Token:
        start_pos = self.position
        start_line = self.line
        start_col = self.column
        
        value = self.current_char
        self._advance()
        
        while self.current_char is not None and self._is_alnum(self.current_char):
            value += self.current_char
            self._advance()
        
        token_type = self.KEYWORDS.get(value.lower(), TokenType.IDENTIFIER)
        
        return Token(
            type=token_type,
            value=value,
            raw_value=value,
            position=start_pos,
            line=start_line,
            column=start_col
        )

    def _read_string(self) -> Token:
        start_pos = self.position
        start_line = self.line
        start_col = self.column
        
        quote = self.current_char
        self._advance()
        
        value = ''
        raw_value = quote
        
        while self.current_char is not None and self.current_char != quote:
            if self.current_char == '\\':
                self._advance()
                if self.current_char is None:
                    self._error("Unterminated string literal")
                # Handle escape sequences here if needed
                value += self.current_char
                raw_value += '\\' + self.current_char
            else:
                value += self.current_char
                raw_value += self.current_char
            self._advance()
        
        if self.current_char != quote:
            self._error("Unterminated string literal")
        
        self._advance()  # Skip the closing quote
        raw_value += quote
        
        return Token(
            type=TokenType.STRING,
            value=value,
            raw_value=raw_value,
            position=start_pos,
            line=start_line,
            column=start_col
        )

    def _read_comment(self) -> Token:
        start_pos = self.position
        start_line = self.line
        start_col = self.column
        
        value = ''
        self._advance()  # Skip the semicolon
        
        while self.current_char is not None and self.current_char != '\n':
            value += self.current_char
            self._advance()
        
        return Token(
            type=TokenType.COMMENT,
            value=value,
            raw_value=';' + value,
            position=start_pos,
            line=start_line,
            column=start_col
        )

    def get_next_token(self) -> Token:
        while self.current_char is not None:
            if self.current_char.isspace():
                self._skip_whitespace()
                continue
                
            if self._is_digit(self.current_char):
                return self._read_number()
                
            if self._is_alpha(self.current_char):
                return self._read_identifier()
                
            if self.current_char in ('"', "'"):
                return self._read_string()
                
            if self.current_char == ';':
                return self._read_comment()
                
            # Handle operators and punctuation
            if self.current_char == '=':
                self._advance()
                return Token(
                    type=TokenType.ASSIGN,
                    value='=',
                    raw_value='=',
                    position=self.position-1,
                    line=self.line,
                    column=self.column-1
                )
                
            # Handle other single-character tokens
            token_type = None
            if self.current_char == '+':
                token_type = TokenType.PLUS
            elif self.current_char == '-':
                token_type = TokenType.MINUS
            elif self.current_char == '*':
                token_type = TokenType.MULTIPLY
            elif self.current_char == '/':
                token_type = TokenType.DIVIDE
            elif self.current_char == '(':
                token_type = TokenType.LPAREN
            elif self.current_char == ')':
                token_type = TokenType.RPAREN
            elif self.current_char == '>':
                token_type = TokenType.PUSH
            elif self.current_char == '<':
                token_type = TokenType.POP
            elif self.current_char == '[':
                token_type = TokenType.LOOP_START
            elif self.current_char == ']':
                token_type = TokenType.LOOP_END
            elif self.current_char == '.':
                token_type = TokenType.OUTPUT
            elif self.current_char == ',':
                token_type = TokenType.INPUT
                
            if token_type is not None:
                char = self.current_char
                self._advance()
                return Token(
                    type=token_type,
                    value=char,
                    raw_value=char,
                    position=self.position-1,
                    line=self.line,
                    column=self.column-1
                )
                
            self._error(f"Unknown character: '{self.current_char}'")
        
        return Token(
            type=TokenType.EOF,
            value='',
            raw_value='',
            position=self.position,
            line=self.line,
            column=self.column
        )

def test_lexer():
    """Test the enhanced lexer"""
    code = """
    // Simple variable assignments
    x = 42
    y = 3.14
    name = "HyperCode"
    
    // Control flow
    if x > 10 {
        print("x is greater than 10")
    } else {
        print("x is 10 or less")
    }
    
    // Function definition
    func add(a, b) {
        return a + b
    }
    
    // Function call
    result = add(5, 3.5)
    """
    
    lexer = HyperCodeLexer(code)
    tokens = []
    
    while True:
        token = lexer.get_next_token()
        tokens.append(token)
        if token.type == TokenType.EOF:
            break
    
    print("Tokens:")
    for token in tokens:
        print(f"  {token}")

if __name__ == "__main__":
    test_lexer()