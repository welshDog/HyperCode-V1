"""
Core package for the HyperCode language implementation.

This package contains the core components of the HyperCode language,
including the lexer, parser, and semantic analyzer.
"""

from .ast import *
from .error_handler import report, report_parse_error
from .lexer import Lexer
from .parser import ParseError, Parser
from .tokens import Token, TokenType

# Optimizer and SemanticAnalyzer are not implemented yet

__all__ = [
    "Lexer",
    "Token",
    "TokenType",
    "Parser",
    "Interpreter",
    "Environment",
    "ParseError",
    "report_parse_error",
    "report",
    # AST nodes are imported via * from ast
]
