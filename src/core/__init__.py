# src/core/__init__.py
"""
HyperCode Core Module

This is the main package for the HyperCode language implementation.
"""

# Import key components to make them available at the package level
from .tokens import Token, TokenType, KEYWORDS
from .lexer import Lexer, LexerError

__all__ = [
    'Token', 
    'TokenType', 
    'KEYWORDS', 
    'Lexer', 
    'LexerError'
]