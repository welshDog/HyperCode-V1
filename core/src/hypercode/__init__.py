"""
HyperCode - A neurodivergent-first programming language with AI compatibility.
"""

__version__ = "1.0.0"
__author__ = "welshDog (Lyndz Williams)"
__email__ = "hello@hypercode.dev"

# Core components
from .core.lexer import Lexer
from .core.tokens import TokenType

# Re-export commonly used components
__all__ = ["Lexer", "TokenType"]
