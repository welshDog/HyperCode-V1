# src/hypercode/core/__init__.py
"""
HyperCode Core Module

This package contains the core components of the HyperCode language:
- Lexer: Converts source code into tokens
- Parser: Converts tokens into an Abstract Syntax Tree (AST)
- Interpreter: Executes the AST
- AST: Abstract Syntax Tree node definitions
- Tokens: Token definitions and types
"""

# Core components
from .lexer import Lexer
from .parser import Parser, ParseError
from .interpreter import Interpreter
from .ast import *
from .tokens import TokenType, Token

# Re-export commonly used components
__all__ = [
    "Lexer",
    "Parser",
    "ParseError",
    "Interpreter",
    "TokenType",
    "Token",
    # AST nodes will be available directly from hypercode.core
]
