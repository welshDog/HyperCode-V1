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
from typing import List, Optional
import re

@dataclass
class Token:
    """Represents a single token in the source code."""
    type: str
    value: str
    line: int
    column: int

    def __str__(self):
        return f"Token({self.type}, {repr(self.value)}, line={self.line}, col={self.column})"

class Lexer:
    """
    Lexical analyzer for the HyperCode language.
    
    Converts source code into a sequence of tokens that can be processed
    by the parser.
    """
    
    # Define token types
    KEYWORDS = {
        'if': 'IF',
        'else': 'ELSE',
        'for': 'FOR',
        'while': 'WHILE',
        'function': 'FUNCTION',
        'return': 'RETURN',
        'let': 'LET',
        'const': 'CONST',
        'true': 'TRUE',
        'false': 'FALSE',
        'null': 'NULL'
    }
    
    # Token specifications - ordered by priority
    TOKENS = [
        # Comments first to handle them before other tokens
        ('COMMENT', r'//.*|/\*[\s\S]*?\*/'),
        # Whitespace
        ('WHITESPACE', r'\s+'),
        # String literals - handle both single and double quoted strings with escaped quotes
        ('STRING', r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\''),
        # Numbers (including decimals with optional leading/trailing digits)
        ('NUMBER', r'\d*\.?\d+'),
        # Keywords and identifiers
        ('IDENTIFIER', r'[a-zA-Z_]\w*'),
        # Multi-character operators
        ('EQUALS', r'=='),
        ('NOT_EQUALS', r'!='),
        ('LESS_EQUAL', r'<='),
        ('GREATER_EQUAL', r'>='),
        # Single-character operators and punctuation
        ('PLUS', r'\+'),
        ('MINUS', r'-'),
        ('MULTIPLY', r'\*'),
        ('DIVIDE', r'/'),
        ('ASSIGN', r'='),
        ('LESS', r'<'),
        ('GREATER', r'>'),
        ('LPAREN', r'\('),
        ('RPAREN', r'\)'),
        ('LBRACE', r'\{'),
        ('RBRACE', r'\}'),
        ('LBRACKET', r'\['),
        ('RBRACKET', r'\]'),
        ('COMMA', r','),
        ('SEMICOLON', r';'),
        ('COLON', r':'),
        ('DOT', r'\.'),
    ]
    
    def __init__(self):
        """Initialize the lexer with an empty token list and position."""
        self.tokens: List[Token] = []
        self.pos = 0
        self.line = 1
        self.column = 1
        self.source = ""
        
        # Compile regex patterns
        self.token_patterns = []
        for token_type, pattern in self.TOKENS:
            self.token_patterns.append((token_type, re.compile(pattern)))
    
    def tokenize(self, source: str) -> List[Token]:
        """
        Convert source code into a list of tokens.
        
        Args:
            source: The source code to tokenize
            
        Returns:
            List of Token objects
        """
        self.source = source
        self.tokens = []
        self.pos = 0
        self.line = 1
        self.column = 1
        
        while self.pos < len(self.source):
            if not self._match_patterns():
                # Handle unknown characters
                self._handle_unknown()
                
        return self.tokens

    def _match_patterns(self) -> bool:
        """Try to match the current position against all token patterns."""
        for token_type, pattern in self.token_patterns:
            if match := pattern.match(self.source, self.pos):
                value = match.group(0)
                
                # Add token unless it's whitespace or a comment
                if token_type not in ('WHITESPACE', 'COMMENT'):
                    # Check if the identifier is a keyword
                    final_type = self.KEYWORDS.get(value, token_type) if token_type == 'IDENTIFIER' else token_type
                    self._add_token(final_type, value)

                self._update_position(value)
                self.pos = match.end()
                return True
                
        return False

    def _update_position(self, value: str):
        """Update line and column numbers based on the token's value."""
        if '\n' in value:
            lines = value.split('\n')
            self.line += len(lines) - 1
            self.column = len(lines[-1]) + 1
        else:
            self.column += len(value)
    
    def _add_token(self, token_type: str, value: str):
        """Add a token to the token list."""
        self.tokens.append(Token(token_type, value, self.line, self.column))
    
    def _handle_unknown(self):
        """Handle unknown characters in the source."""
        char = self.source[self.pos]
        self.tokens.append(Token('UNKNOWN', char, self.line, self.column))
        self.pos += 1
        self.column += 1
