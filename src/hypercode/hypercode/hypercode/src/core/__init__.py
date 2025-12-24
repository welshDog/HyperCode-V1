# src/core/__init__.py
"""
HyperCode Core Module

This is the main package for the HyperCode language implementation.
"""

from .lexer import Lexer, LexerError
# Import key components to make them available at the package level
from .tokens import KEYWORDS, Token, TokenType

__all__ = ["Token", "TokenType", "KEYWORDS", "Lexer", "LexerError"]
