"""
HyperCode Lexer - Complete Implementation
Tokenizes HyperCode programs with full neurodivergent-friendly features

Features:
- 8 core operations (Brainfuck-inspired)
- Spatial 2D mode (@)
- AI-native markers (#)
- Comments (;)
- Position tracking
- Error reporting
- Colorized output (for ADHD/dyslexia)
"""

from dataclasses import dataclass
from typing import List, Optional, Tuple
from enum import Enum
import sys


class TokenType(Enum):
    """HyperCode token types - minimal yet powerful"""
    # Core operations (Brainfuck-inspired)
    PUSH = "PUSH"           # > move pointer right
    POP = "POP"             # < move pointer left
    INCR = "INCR"           # + increment cell
    DECR = "DECR"           # - decrement cell
    OUTPUT = "OUTPUT"       # . output character
    INPUT = "INPUT"         # , read character
    LOOP_START = "LOOP_START"   # [ start loop
    LOOP_END = "LOOP_END"       # ] end loop
    
    # HyperCode extensions
    SPATIAL_2D = "SPATIAL_2D"   # @ enter 2D spatial mode
    AI_NATIVE = "AI_NATIVE"     # # AI-native code marker
    COMMENT = "COMMENT"         # ; comment line
    
    # Special
    EOF = "EOF"             # End of file
    UNKNOWN = "UNKNOWN"     # Unknown character


@dataclass
class Token:
    """Represents a single token with position tracking"""
    type: TokenType
    value: str
    position: int
    line: int
    column: int
    
    def __repr__(self) -> str:
        """Neurodivergent-friendly representation"""
        return f"Token({self.type.value:15} | '{self.value}' | L{self.line}:C{self.column})"


class LexerError(Exception):
    """Lexer-specific errors with context"""
    def __init__(self, message: str, line: int, column: int):
        self.message = message
        self.line = line
        self.column = column
        super().__init__(f"Line {line}, Col {column}: {message}")


class HyperCodeLexer:
    """
    Tokenizes HyperCode programs with accessibility features.
    
    Design principles:
    - Clear error messages (neurodivergent-friendly)
    - Position tracking (helps with debugging)
    - Colorized output (optional, for visual learners)
    - Comments preserved (for documentation)
    """
    
    # Token mapping (simple, explicit)
    TOKEN_MAP = {
        '>': TokenType.PUSH,
        '<': TokenType.POP,
        '+': TokenType.INCR,
        '-': TokenType.DECR,
        '.': TokenType.OUTPUT,
        ',': TokenType.INPUT,
        '[': TokenType.LOOP_START,
        ']': TokenType.LOOP_END,
        '@': TokenType.SPATIAL_2D,
        '#': TokenType.AI_NATIVE,
        ';': TokenType.COMMENT,
    }
    
    def __init__(self, source: str, filename: str = "<stdin>"):
        """
        Initialize lexer with source code.
        
        Args:
            source: HyperCode source code
            filename: Source filename (for error reporting)
        """
        self.source = source
        self.filename = filename
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []
    
    def tokenize(self) -> List[Token]:
        """
        Convert HyperCode source to token stream.
        
        Returns:
            List of Token objects
            
        Raises:
            LexerError: On invalid syntax
        """
        self.tokens = []
        
        while self.position < len(self.source):
            char = self.source[self.position]
            
            # Handle comments (skip until end of line)
            if char == ';':
                self._skip_comment()
                continue
            
            # Handle whitespace (track position but don't create tokens)
            if char.isspace():
                self._advance_position(char)
                continue
            
            # Handle valid tokens
            if char in self.TOKEN_MAP:
                token_type = self.TOKEN_MAP[char]
                token = Token(
                    type=token_type,
                    value=char,
                    position=self.position,
                    line=self.line,
                    column=self.column
                )
                self.tokens.append(token)
                self._advance_position(char)
            else:
                # Unknown character - helpful error message
                raise LexerError(
                    f"Unexpected character: '{char}' (ASCII {ord(char)})\n"
                    f"Valid operations: > < + - . , [ ] @ # ;",
                    self.line,
                    self.column
                )
        
        # Add EOF token
        self.tokens.append(Token(
            type=TokenType.EOF,
            value="",
            position=self.position,
            line=self.line,
            column=self.column
        ))
        
        return self.tokens
    
    def _advance_position(self, char: str):
        """Update position tracking after processing character"""
        self.position += 1
        
        if char == '\n':
            self.line += 1
            self.column = 1
        else:
            self.column += 1
    
    def _skip_comment(self):
        """Skip characters until end of line"""
        while self.position < len(self.source) and self.source[self.position] != '\n':
            self._advance_position(self.source[self.position])
    
    def get_tokens(self) -> List[Token]:
        """Return current token list"""
        return self.tokens
    
    def filter_tokens(self, exclude_types: Optional[List[TokenType]] = None) -> List[Token]:
        """
        Get tokens excluding certain types.
        
        Args:
            exclude_types: Token types to exclude
            
        Returns:
            Filtered token list
        """
        if exclude_types is None:
            exclude_types = [TokenType.UNKNOWN, TokenType.EOF]
        
        return [t for t in self.tokens if t.type not in exclude_types]
    
    def print_tokens(self, colorize: bool = False):
        """
        Print tokens in readable format.
        
        Args:
            colorize: Use ANSI colors (helps ADHD/dyslexia)
        """
        if colorize and sys.stdout.isatty():
            # Color codes for different token types
            colors = {
                TokenType.PUSH: '\033[94m',      # Blue
                TokenType.POP: '\033[94m',       # Blue
                TokenType.INCR: '\033[92m',      # Green
                TokenType.DECR: '\033[92m',      # Green
                TokenType.OUTPUT: '\033[93m',    # Yellow
                TokenType.INPUT: '\033[93m',     # Yellow
                TokenType.LOOP_START: '\033[95m', # Magenta
                TokenType.LOOP_END: '\033[95m',   # Magenta
                TokenType.SPATIAL_2D: '\033[96m', # Cyan
                TokenType.AI_NATIVE: '\033[91m',  # Red
            }
            reset = '\033[0m'
            
            for token in self.tokens:
                color = colors.get(token.type, '')
                print(f"{color}{token}{reset}")
        else:
            # Plain text output
            for token in self.tokens:
                print(token)
    
    def get_statistics(self) -> dict:
        """
        Get token statistics (useful for analysis).
        
        Returns:
            Dictionary with token counts
        """
        stats = {}
        for token in self.tokens:
            if token.type != TokenType.EOF:
                stats[token.type.value] = stats.get(token.type.value, 0) + 1
        return stats


def main():
    """CLI interface for the lexer"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="HyperCode Lexer - Tokenize HyperCode programs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python lexer.py program.hc
  python lexer.py program.hc --colorize
  echo "+++>." | python lexer.py -
        """
    )
    
    parser.add_argument(
        'file',
        help='HyperCode source file (or - for stdin)'
    )
    parser.add_argument(
        '--colorize',
        action='store_true',
        help='Use colored output (ADHD/dyslexia-friendly)'
    )
    parser.add_argument(
        '--stats',
        action='store_true',
        help='Show token statistics'
    )
    
    args = parser.parse_args()
    
    # Read source
    if args.file == '-':
        source = sys.stdin.read()
        filename = '<stdin>'
    else:
        try:
            with open(args.file, 'r') as f:
                source = f.read()
            filename = args.file
        except FileNotFoundError:
            print(f"❌ Error: File not found: {args.file}", file=sys.stderr)
            return 1
    
    # Tokenize
    try:
        lexer = HyperCodeLexer(source, filename)
        tokens = lexer.tokenize()
        
        print(f"✅ Successfully tokenized: {filename}")
        print(f"   Total tokens: {len(tokens) - 1}")  # Exclude EOF
        print()
        
        # Print tokens
        lexer.print_tokens(colorize=args.colorize)
        
        # Print statistics
        if args.stats:
            print("\n📊 Token Statistics:")
            stats = lexer.get_statistics()
            for token_type, count in sorted(stats.items()):
                print(f"   {token_type:15} : {count}")
        
        return 0
        
    except LexerError as e:
        print(f"❌ Lexer Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
