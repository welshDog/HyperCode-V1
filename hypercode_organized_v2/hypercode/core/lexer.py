"""
HyperCode Lexer

This module implements the lexical analyzer for the HyperCode language.
It converts source code into a sequence of tokens that can be processed by the parser.
"""

import re
from typing import Any, Dict, Iterator, List, Optional, Pattern, Tuple, Union

from .tokens import Token, TokenType


def _parse_literal_value(token_type: TokenType, text: str) -> Any:
    """Parse a literal value from the token text.

    Args:
        token_type: The type of the token
        text: The text content of the token

    Returns:
        The parsed literal value
    """
    if token_type == TokenType.STRING:
        return text[1:-1]  # Remove quotes
    elif token_type == TokenType.NUMBER:
        return int(text)
    elif token_type == TokenType.FLOAT:
        return float(text)
    elif token_type == TokenType.TRUE:
        return True
    elif token_type == TokenType.FALSE:
        return False
    elif token_type == TokenType.NIL:
        return None
    return text



class LexerError(Exception):
    """Exception raised for errors encountered during lexical analysis.
    
    Attributes:
        message: Explanation of the error
        line: Line number where the error occurred (1-based)
        column: Column number where the error occurred (1-based)
    """

    def __init__(self, message: str, line: int, column: int) -> None:
        """Initialize the LexerError.
        
        Args:
            message: Error message
            line: Line number where error occurred (1-based)
            column: Column number where error occurred (1-based)
        """
        self.message = message
        self.line = line
        self.column = column
        super().__init__(f"{message} at line {line}, column {column}")


# Removed extracted_function as it was redundant

class Lexer:
    """Lexical analyzer for the HyperCode language.

    The lexer converts source code into a sequence of tokens that can be processed
    by the parser. It handles:
    - Whitespace and comments
    - Numbers (integers and floats)
    - Strings (single and double quoted)
    - Keywords and identifiers
    - Operators and delimiters
    
    The lexer uses regex patterns to match tokens and maintains position
    information for error reporting.
    """

    # Define keywords mapping
    KEYWORDS: Dict[str, TokenType] = {
        # Control flow
        "if": TokenType.IF,
        "else": TokenType.ELSE,
        "for": TokenType.FOR,
        "while": TokenType.WHILE,
        "in": TokenType.IN,
        "match": TokenType.MATCH,
        "with": TokenType.WITH,
        "then": TokenType.THEN,
        # Functions and modules
        "function": TokenType.FUNCTION,
        "return": TokenType.RETURN,
        "import": TokenType.IMPORT,
        "export": TokenType.EXPORT,
        "as": TokenType.AS,
        # Variable declarations
        "let": TokenType.LET,
        "const": TokenType.CONST,
        "var": TokenType.VAR,
        # Types and interfaces
        "type": TokenType.TYPE,
        "interface": TokenType.INTERFACE,
        "class": TokenType.CLASS,
        # Literals
        "true": TokenType.TRUE,
        "false": TokenType.FALSE,
        "nil": TokenType.NIL,
        # Block control
        "end": TokenType.END,
        # HyperCode specific
        "intent": TokenType.INTENT,
        "print": TokenType.PRINT,
    }

    # Define token patterns using regular expressions
    TOKEN_PATTERNS: List[Tuple[Pattern, Optional[TokenType]]] = [
        # Whitespace (ignored)
        (re.compile(r"\s+"), None),
        # Comments (ignored)
        (re.compile(r"#.*"), None),
        # Multi-line comments (ignored)
        (re.compile(r'"{3}[\s\S]*?"{3}'), None),
        # Numbers (integers and floats)
        (re.compile(r"\d+\.\d+"), TokenType.FLOAT),  # Float
        (re.compile(r"\d+"), TokenType.NUMBER),  # Integer
        # Strings (single and double quoted)
        (re.compile(r'"(?:\\.|[^"\\])*"'), TokenType.STRING),
        (re.compile(r"'(?:\\.|[^'\\])*'"), TokenType.STRING),
        # Identifiers and keywords
        (re.compile(r"[a-zA-Z_][a-zA-Z0-9_]*"), None),  # Handled specially
        # Operators
        (re.compile(r"\+="), TokenType.PLUS_ASSIGN),
        (re.compile(r"-="), TokenType.MINUS_ASSIGN),
        (re.compile(r"\*="), TokenType.MULTIPLY_ASSIGN),
        (re.compile(r"/="), TokenType.DIVIDE_ASSIGN),
        (re.compile(r"%="), TokenType.MODULO_ASSIGN),
        (re.compile(r"\*\*="), TokenType.EXPONENT_ASSIGN),
        (re.compile(r"=="), TokenType.EQUAL),
        (re.compile(r"!="), TokenType.NOT_EQUAL),
        (re.compile(r"<="), TokenType.LESS_EQUAL),
        (re.compile(r">="), TokenType.GREATER_EQUAL),
        (re.compile(r"\+\+"), TokenType.PLUS),
        (re.compile(r"--"), TokenType.MINUS),
        (re.compile(r"\*\*"), TokenType.EXPONENT),
        (re.compile(r"&&"), TokenType.AND),
        (re.compile(r"\|\|"), TokenType.OR),
        (re.compile(r"!"), TokenType.BANG),  # Changed from NOT to BANG
        (re.compile(r"&"), TokenType.BITWISE_AND),
        (re.compile(r"\|"), TokenType.BITWISE_OR),
        (re.compile(r"\^"), TokenType.BITWISE_XOR),
        (re.compile(r"~"), TokenType.BITWISE_NOT),
        (re.compile(r"<<"), TokenType.LEFT_SHIFT),
        (re.compile(r">>"), TokenType.RIGHT_SHIFT),
        (re.compile(r"="), TokenType.ASSIGN),
        (re.compile(r"<"), TokenType.LESS),
        (re.compile(r">"), TokenType.GREATER),
        (re.compile(r"\+"), TokenType.PLUS),
        (re.compile(r"-"), TokenType.MINUS),
        (re.compile(r"\*"), TokenType.STAR),
        (re.compile(r"/"), TokenType.DIVIDE),
        (re.compile(r"%"), TokenType.MODULO),
        # Delimiters
        (re.compile(r"\("), TokenType.LEFT_PAREN),
        (re.compile(r"\)"), TokenType.RIGHT_PAREN),
        (re.compile(r"\["), TokenType.LEFT_BRACKET),
        (re.compile(r"\]"), TokenType.RIGHT_BRACKET),
        (re.compile(r"\{"), TokenType.LEFT_BRACE),
        (re.compile(r"\}"), TokenType.RIGHT_BRACE),
        (re.compile(r","), TokenType.COMMA),
        (re.compile(r"\."), TokenType.DOT),
        (re.compile(r":"), TokenType.COLON),
        (re.compile(r";"), TokenType.SEMICOLON),
        (re.compile(r"->"), TokenType.ARROW),
        (re.compile(r"\.\."), TokenType.RANGE),
    ]

    def __init__(self, source: str, filename: str = "<string>") -> None:
        """Initialize the lexer with source code.

        Args:
            source: The source code to tokenize
            filename: The name of the source file (for error reporting)
        """
        self.source = source
        self.filename = filename
        self.tokens: List[Token] = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.column = 1
        self.indent_stack = [0]  # Track indentation levels
        self.paren_level = 0  # Track parentheses nesting level
        self.brace_level = 0  # Track braces nesting level
        self.bracket_level = 0  # Track brackets nesting level

    def scan_tokens(self) -> List[Token]:
        """Scan the source code and return a list of tokens.

        Returns:
            A list of tokens representing the source code.
        """
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        # Add EOF token
        self.add_token(TokenType.EOF, "")
        return self.tokens

    def scan_token(self) -> None:
        """Scan the next token from the source code."""
        # Get the next character
        char = self.advance()

        # Check for newlines and indentation
        if char == "\n":
            self.handle_newline()
            return
        elif char.isspace():
            # Skip other whitespace
            return

        # Try to match token patterns
        for pattern, token_type in self.TOKEN_PATTERNS:
            match = pattern.match(self.source, self.start)
            if match and match.start() == self.start:
                # Update current position
                self.current = match.end()

                # Get the matched text
                text = match.group(0)

                # Handle identifiers and keywords
                if token_type is None and pattern.pattern == r"[a-zA-Z_][a-zA-Z0-9_]*":
                    self.handle_identifier(text)
                # Handle other tokens
                elif token_type is not None:
                    # Parse literal value based on token type
                    literal = _parse_literal_value(token_type, text)
                    self.add_token(token_type, text, literal)

                # Update column position
                self.column += len(text)
                return

        # If we get here, it's an unexpected character
        self.error(f"Unexpected character: {char}")

    def handle_identifier(self, text: str) -> None:
        """Handle identifiers and keywords."""
        # Check if it's a keyword
        token_type = self.KEYWORDS.get(text)
        if token_type is None:
            # It's an identifier
            self.add_token(TokenType.IDENTIFIER, text)
        else:
            # It's a keyword
            self.add_token(token_type, text)

    def handle_newline(self) -> None:
        """Handle newlines and indentation."""
        # Add a NEWLINE token if we're not in the middle of a block
        if self.paren_level == 0 and self.brace_level == 0 and self.bracket_level == 0:
            self.add_token(TokenType.NEWLINE, "\n")

            # Calculate indentation level
            indent = 0
            while self.peek() == " " or self.peek() == "\t":
                if self.peek() == " ":
                    indent += 1
                else:  # tab
                    indent += 4  # Treat tabs as 4 spaces
                self.advance()

            # Handle indentation changes
            current_indent = self.indent_stack[-1]
            if indent > current_indent:
                self.indent_stack.append(indent)
                self.add_token(TokenType.INDENT, " " * (indent - current_indent))
            elif indent < current_indent:
                # Pop indentation levels until we find a matching one
                while self.indent_stack and self.indent_stack[-1] > indent:
                    self.indent_stack.pop()
                    self.add_token(TokenType.DEDENT, "")
                if self.indent_stack and self.indent_stack[-1] != indent:
                    self.error("Inconsistent indentation")

        # Update line and column counters
        self.line += 1
        self.column = 1

    def add_token(
        self, token_type: TokenType, lexeme: str, literal: Any = None
    ) -> None:
        """Add a new token to the token list."""
        # Calculate end position
        end_line = self.line
        end_column = self.column + len(lexeme) - 1

        # Create and add the token
        token = Token(
            type=token_type,
            lexeme=lexeme,
            literal=literal,
            line=self.line,
            column=self.column,
            end_line=end_line,
            end_column=end_column,
        )
        self.tokens.append(token)

        # Update column position
        self.column = end_column + 1

    def advance(self) -> str:
        """Consume and return the next character in the source."""
        if self.is_at_end():
            return "\0"

        char = self.source[self.current]
        self.current += 1

        # Update line and column counters
        if char == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        return char

    def peek(self, offset: int = 0) -> str:
        """Look ahead at the next character without consuming it."""
        pos = self.current + offset
        if pos >= len(self.source):
            return "\0"
        return self.source[pos]

    def is_at_end(self) -> bool:
        """Check if we've reached the end of the source."""
        return self.current >= len(self.source)

    def error(self, message: str) -> None:
        """Raise a lexer error."""
        raise LexerError(message, self.line, self.column)


def tokenize(source: str, filename: str = "<string>") -> List[Token]:
    """Tokenize the given source code.
    
    This is a convenience function that creates a Lexer instance and returns
    all tokens from the source.
    
    Args:
        source: The source code to tokenize
        filename: The name of the source file (for error reporting)
        
    Returns:
        List of tokens representing the source code.
        
    Raises:
        LexerError: If there's an error during tokenization
    """
    lexer = Lexer(source, filename)
    return lexer.scan_tokens()
    lexer = Lexer(source, filename)
    return lexer.scan_tokens()
