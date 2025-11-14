"""
Core package for the HyperCode language implementation.

This package contains the core components of the HyperCode language,
including the lexer, parser, and semantic analyzer.
"""

from .lexer import Lexer
from .tokens import Token, TokenType
from .parser import Parser, ParseError
from .ast import *
from .error_handler import report_parse_error, report
# Optimizer and SemanticAnalyzer are not implemented yet

__all__ = [
    'Lexer',
    'Token',
    'TokenType',
    'Parser',
    'ParseError',
    'report_parse_error',
    'report',
    # AST nodes are imported via * from ast
]
