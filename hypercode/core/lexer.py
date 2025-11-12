# Copyright 2025 welshDog (Lyndz Williams)
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Core HyperCode language implementation - Lexer

This module implements the lexical analyzer for the HyperCode language.
It converts source code into a sequence of tokens for further processing.
"""

from dataclasses import dataclass
from typing import List, Optional, Dict, Tuple, Pattern, Union
import re
from .token_types import TokenType, TOKEN_MAP

@dataclass
class Token:
    """Represents a single token in the source code."""
    type: TokenType
    value: str
    line: int
    column: int

    def __str__(self):
        return f"{self.type.name}({repr(self.value)}) at {self.line}:{self.column}"

class Lexer:
    """
    Lexical analyzer for the HyperCode language.
    
    Converts source code into a sequence of tokens that can be processed
    by the parser.
    """
    
    # Define keywords mapping
    KEYWORDS = {
        'if': TokenType.IF,
        'else': TokenType.ELSE,
        'for': TokenType.FOR,
        'while': TokenType.WHILE,
        'function': TokenType.FUNCTION,
        'return': TokenType.RETURN,
        'let': TokenType.LET,
        'const': TokenType.CONST,
        'var': TokenType.VAR,
        'true': TokenType.TRUE,
        'false': TokenType.FALSE,
        'null': TokenType.NULL,
        'print': TokenType.PRINT
    }
    
    # Token specifications - ordered by priority (longer patterns first)
    TOKENS = [
        # Whitespace first
        (TokenType.WHITESPACE, r'\s+'),
        
        # Multi-character operators (must come before single-character ones)
        (TokenType.STAR_STAR, r'\*\*'),
        (TokenType.SLASH_SLASH, r'//'),
        
        # Comments (after operators to avoid conflicts)
        (TokenType.COMMENT, r'#[^\r\n]*|//[^\r\n]*|/\*[\s\S]*?\*/'),
        (TokenType.EQUAL_EQUAL, r'=='),
        (TokenType.BANG_EQUAL, r'!='),
        (TokenType.LESS_EQUAL, r'<='),
        (TokenType.GREATER_EQUAL, r'>='),
        (TokenType.ARROW, r'->'),
        
        # Single-character operators
        (TokenType.PLUS, r'\+'),
        (TokenType.MINUS, r'-'),
        (TokenType.STAR, r'\*'),
        (TokenType.SLASH, r'/'),
        (TokenType.PERCENT, r'%'),
        (TokenType.EQUAL, r'='),
        (TokenType.BANG, r'!'),
        (TokenType.LESS, r'<'),
        (TokenType.GREATER, r'>'),
        # String literals (handle both single and double quoted strings with escaped quotes)
        (TokenType.STRING, r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\''),
        
        # Numbers (handle integers, decimals, and scientific notation)
        (TokenType.NUMBER, r'\d+\.\d+([eE][+-]?\d+)?|\d+[eE][+-]?\d+|\.\d+([eE][+-]?\d+)?|0[xX][0-9a-fA-F]+|0[bB][01]+|0[oO]?[0-7]+|\d+'),
        
        # Single-character operators and punctuation
        (TokenType.PLUS, r'\+'),
        (TokenType.MINUS, r'-'),
        (TokenType.STAR, r'\*'),
        (TokenType.SLASH, r'/'),
        (TokenType.PERCENT, r'%'),
        (TokenType.BANG, r'!'),
        (TokenType.EQUAL, r'='),
        (TokenType.LESS, r'<'),
        (TokenType.GREATER, r'>'),
        (TokenType.LPAREN, r'\('),
        (TokenType.RPAREN, r'\)'),
        (TokenType.LBRACE, r'\{'),
        (TokenType.RBRACE, r'\}'),
        (TokenType.LBRACKET, r'\['),
        (TokenType.RBRACKET, r'\]'),
        (TokenType.COMMA, r','),
        (TokenType.SEMICOLON, r';'),
        (TokenType.COLON, r':'),
        (TokenType.DOT, r'\.'),
        
        # Keywords and identifiers (must come after operators to avoid conflicts)
        (TokenType.IDENTIFIER, r'[a-zA-Z_]\w*'),
    ]
    
    def __init__(self, source: str = ""):
        """Initialize the lexer with source code.
        
        Args:
            source: The source code to tokenize
        """
        self.tokens: List[Token] = []
        self.pos = 0
        self.line = 1
        self.column = 1
        self.source = source
        
        # Compile regex patterns
        self.token_patterns: List[Tuple[TokenType, Pattern]] = []
        for token_type, pattern in self.TOKENS:
            self.token_patterns.append((token_type, re.compile(pattern)))
    
    def tokenize(self, source: Optional[str] = None) -> List[Token]:
        """
        Convert source code into a list of tokens.
        
        Args:
            source: Optional source code to tokenize. If not provided, uses the source
                   passed to the constructor.
            
        Returns:
            List of Token objects
            
        Raises:
            ValueError: If no source code is provided
        """
        if source is not None:
            self.source = source
        
        if not self.source:
            raise ValueError("No source code provided to tokenize")
            
        # Reset state
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens = []
        
        while self.pos < len(self.source):
            if not self._match_patterns():
                # Handle unknown characters
                self._handle_unknown()
                
        # Add EOF token
        self._add_token(TokenType.EOF, '')
        return self.tokens

    def _match_patterns(self) -> bool:
        """Try to match the current position against all token patterns."""
        for token_type, pattern in self.token_patterns:
            match = pattern.match(self.source, self.pos)
            if match:
                value = match.group(0)
                
                # Update position first for accurate line/column tracking
                self._update_position(value)
                
                # Skip whitespace and comments by default
                if token_type in (TokenType.WHITESPACE, TokenType.COMMENT):
                    # Only skip if it's not a SLASH_SLASH operator
                    if token_type != TokenType.SLASH_SLASH or value != '//':
                        self.pos = match.end()
                        return True
                
                # Special handling for identifiers that might be keywords
                if token_type == TokenType.IDENTIFIER and value in self.KEYWORDS:
                    token_type = self.KEYWORDS[value]
                
                # Add the token
                self._add_token(token_type, value)
                self.pos = match.end()
                return True
                
        return False

    def _update_position(self, text: str) -> None:
        """Update line and column numbers based on the given text."""
        lines = text.splitlines(keepends=True)
        if not lines:
            return
            
        # Update line and column based on the last line
        last_line = lines[-1]
        if '\n' in last_line or '\r' in last_line:
            # If the last character is a newline, move to the start of the next line
            self.line += len(lines)
            self.column = 1
        else:
            # Otherwise, just update the column
            self.column += len(last_line)
            
        # Add any additional newlines from the text
        self.line += text.count('\n')

    def _add_token(self, token_type: TokenType, value: str):
        """Add a token to the token list."""
        self.tokens.append(Token(
            type=token_type,
            value=value,
            line=self.line,
            column=self.column - len(value)
        ))

    def _handle_unknown(self):
        """Handle unknown characters in the source."""
        char = self.source[self.pos]
        if char.strip():  # Only raise for non-whitespace characters
            raise SyntaxError(
                f"Invalid character '{char}' at line {self.line}, column {self.column}"
            )
        # Skip the unknown character
        self.pos += 1
        self.column += 1
