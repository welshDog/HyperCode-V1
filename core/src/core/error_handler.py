"""
HyperCode Error Handler
=======================

Provides centralized error reporting utilities for the HyperCode compiler and interpreter.
Handles formatting and outputting of syntax and runtime errors to stderr.
"""

import sys
from .tokens import Token, TokenType
from .telemetry import TelemetryCollector

def report_parse_error(token: Token, message: str):
    """
    Reports a parsing error at a specific token location.

    Args:
        token (Token): The token where the error occurred.
        message (str): The error message description.
    """
    if token.type == TokenType.EOF:
        print(f"[line {token.line}] Error at end: {message}", file=sys.stderr)
    else:
        print(f"[line {token.line}] Error at '{token.lexeme}': {message}", file=sys.stderr)
    
    # Log to telemetry
    TelemetryCollector().log_error("ParseError", message)
