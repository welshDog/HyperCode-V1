# src/core/lexer.py
"""
HyperCode Lexer Module

Tokenizes HyperCode source code into a stream of tokens for parsing.
Handles keywords, identifiers, literals, operators, and special syntax.
"""

import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from .tokens import Token, TokenType


@dataclass
class LexerError:
    """
    Represents a lexical analysis error.

    Attributes:
        message: Description of the error
        line: Line number where the error occurred (1-based)
        column: Column number where the error occurred (1-based)
        length: Length of the problematic token (default: 1)
    """
    message: str
    line: int
    column: int
    length: int = 1


class Lexer:
    """
    Lexical analyzer for the HyperCode programming language.

    Converts source code into a sequence of tokens that can be parsed.
    Handles syntax highlighting, error reporting, and source mapping.
    """

    def __init__(self, source: str):
        """Initialize the lexer with source code."""
        self.source = source
        self.tokens: List[Token] = []
        self.errors: List[LexerError] = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.column = 1
        
        # Pre-compile regex patterns for better performance
        self.identifier_regex = re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*')
        self.number_regex = re.compile(r'\d+')
        
        # Cache for keywords
        self.KEYWORDS = {
            'and': TokenType.AND,
            'break': TokenType.BREAK,
            'class': TokenType.CLASS,
            'continue': TokenType.CONTINUE,
            'else': TokenType.ELSE,
            'false': TokenType.FALSE,
            'for': TokenType.FOR,
            'fun': TokenType.FUN,
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
        
        # Use a lookup table for single-character tokens
        self.single_char_tokens = {
            '(': TokenType.LEFT_PAREN,
            ')': TokenType.RIGHT_PAREN,
            '{': TokenType.LEFT_BRACE,
            '}': TokenType.RIGHT_BRACE,
            ',': TokenType.COMMA,
            '.': TokenType.DOT,
            '-': TokenType.MINUS,
            '+': TokenType.PLUS,
            ';': TokenType.SEMICOLON,
            '*': TokenType.STAR,
            '%': TokenType.PERCENT,
            '!': TokenType.BANG,
            '=': TokenType.EQUAL,
            '<': TokenType.LESS,
            '>': TokenType.GREATER,
            ':': TokenType.COLON,
            '?': TokenType.QUESTION,
        }

    def scan_tokens(self) -> List[Token]:
        """Scan the source code and return a list of tokens."""
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        
        # Add EOF token
        self.add_token(TokenType.EOF)
        return self.tokens

    def scan_token(self):
        """Scan a single token."""
        c = self.advance()
        
        # Handle single-character tokens
        if c in self.single_char_tokens:
            # Check for multi-character tokens
            if c == '=' and self.match('='):
                self.add_token(TokenType.EQUAL_EQUAL)
            elif c == '!' and self.match('='):
                self.add_token(TokenType.BANG_EQUAL)
            elif c == '<' and self.match('='):
                self.add_token(TokenType.LESS_EQUAL)
            elif c == '>' and self.match('='):
                self.add_token(TokenType.GREATER_EQUAL)
            elif c == '-' and self.match('>'):
                self.add_token(TokenType.ARROW)
            else:
                self.add_token(self.single_char_tokens[c])
        
        # Handle numbers
        elif c.isdigit():
            self.number()
            
        # Handle strings
        elif c == '"':
            self.string()
            
        # Handle string interpolation (f-strings)
        elif c == 'f' and self.peek() == '"':
            self.advance()  # Consume the 'f'
            self.string(interpolated=True)
            
        # Handle docstrings
        elif c == '/' and self.peek() == '*' and self.peek_next() == '*':
            self.docstring()
            
        # Handle comments
        elif c == '/' and self.peek() == '/':
            while self.peek() != '\n' and not self.is_at_end():
                self.advance()
                
        # Handle whitespace
        elif c in ' \r\t':
            pass
            
        # Handle newlines
        elif c == '\n':
            self.line += 1
            self.column = 1
            
        # Handle identifiers and keywords
        elif c.isalpha() or c == '_':
            self.identifier()
            
        # Handle errors
        else:
            self.error(f"Unexpected character: {c}")

    def number(self):
        """Lex a number literal."""
        while self.peek().isdigit() or self.peek() == '_':
            self.advance()

        # Look for decimal part
        if self.peek() == '.' and (self.peek_next().isdigit() or self.peek_next() == '_'):
            self.advance()  # Consume the '.'

            while self.peek().isdigit() or self.peek() == '_':
                self.advance()

        # Look for scientific notation
        if self.peek().lower() == 'e':
            self.advance()  # Consume 'e' or 'E'
            if self.peek() in '+-':
                self.advance()  # Consume sign
            while self.peek().isdigit() or self.peek() == '_':
                self.advance()

        # Parse the number
        value = self.source[self.start:self.current]
        # Handle underscores in numbers (e.g., 1_000_000)
        value = value.replace('_', '')
        try:
            if '.' in value or 'e' in value.lower():
                self.add_token(TokenType.NUMBER, float(value))
            else:
                # Try to parse as int first, fall back to float if too large
                self.add_token(TokenType.NUMBER, int(value))
        except ValueError:
            self.error(f"Invalid number: {value}")

    def string(self, interpolated=False):
        """Lex a string literal."""
        start_line = self.line
        start_col = self.column
        
        while (not self.is_at_end()) and (self.peek() != '"' or (interpolated and self.peek() == '{')):
            if self.peek() == '\n':
                self.line += 1
                self.column = 0
            elif self.peek() == '\\':
                # Handle escape sequences
                self.advance()
                if self.is_at_end():
                    break
                # Handle common escape sequences
                if self.peek() in '\\"nrt':
                    self.advance()
            self.advance()
            
            # Handle string interpolation
            if interpolated and self.peek() == '{':
                # Add the string part before the interpolation
                value = self.source[self.start + 1:self.current]  # +1 to exclude the opening quote
                self.add_token(TokenType.STRING, value)
                
                # Add the interpolation start token
                self.advance()  # Consume the {
                self.add_token(TokenType.LEFT_BRACE)
                
                # Reset to start a new token after the {
                self.start = self.current
                return
                
        # Unterminated string
        if self.is_at_end():
            self.error("Unterminated string", start_line, start_col)
            return
            
        # The closing "
        self.advance()
        
        # Get the string value (without quotes)
        value = self.source[self.start + 1:self.current - 1]
        self.add_token(TokenType.STRING, value)

    def docstring(self):
        """Lex a docstring."""
        start_line = self.line
        start_col = self.column
        
        # Skip the opening /**
        self.advance()  # Skip *
        self.advance()  # Skip /
        
        while not (self.peek() == '*' and self.peek_next() == '/'):
            if self.is_at_end():
                self.error("Unterminated docstring", start_line, start_col)
                return
            if self.peek() == '\n':
                self.line += 1
                self.column = 0
            self.advance()
            
        # Skip the closing */
        self.advance()  # Skip *
        self.advance()  # Skip /
        
        # Get the docstring content (without /** and */)
        content = self.source[self.start + 3:self.current - 2].strip()
        self.add_token(TokenType.DOCSTRING, content)

    def identifier(self):
        """Lex an identifier or keyword."""
        while self.peek().isalnum() or self.peek() == '_':
            self.advance()
            
        # Check if the identifier is a keyword
        text = self.source[self.start:self.current]
        token_type = self.KEYWORDS.get(text, TokenType.IDENTIFIER)
        self.add_token(token_type)

    def error(self, message: str, line: Optional[int] = None, column: Optional[int] = None):
        """Report a lexing error."""
        line = line or self.line
        column = column or self.column
        length = self.current - self.start
        self.errors.append(LexerError(
            message=message,
            line=line,
            column=column,
            length=max(1, length)  # At least length 1
        ))
        
        # Try to recover by skipping to the next whitespace or known delimiter
        while not self.is_at_end() and not self.peek().isspace() and self.peek() not in ';{}()[]':
            self.advance()

    def is_at_end(self) -> bool:
        """Check if we've reached the end of the source."""
        return self.current >= len(self.source)

    def advance(self) -> str:
        """Consume and return the next character."""
        if self.is_at_end():
            return '\0'
        char = self.source[self.current]
        self.current += 1
        self.column += 1
        return char

    def match(self, expected: str) -> bool:
        """Conditionally consume a character if it matches the expected value."""
        if self.is_at_end():
            return False
        if self.source[self.current] != expected:
            return False
        self.current += 1
        self.column += 1
        return True

    def peek(self) -> str:
        """Look at the next character without consuming it."""
        if self.is_at_end():
            return '\0'
        return self.source[self.current]

    def peek_next(self) -> str:
        """Look at the character after the next one without consuming it."""
        if self.current + 1 >= len(self.source):
            return '\0'
        return self.source[self.current + 1]

    def add_token(self, token_type: TokenType, literal: Any = None):
        """Add a new token to the token list."""
        text = self.source[self.start:self.current]
        self.tokens.append(Token(token_type, text, literal, self.line, self.column))