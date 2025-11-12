from typing import List, Any
from .tokens import Token, TokenType

class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.tokens: List[Token] = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.column = 1

        self.KEYWORDS = {
            "if": TokenType.IF,
            "else": TokenType.ELSE,
            "for": TokenType.FOR,
            "while": TokenType.WHILE,
            "fun": TokenType.FUN,
            "return": TokenType.RETURN,
            "let": TokenType.LET,
            "const": TokenType.CONST,
            "var": TokenType.VAR,
            "print": TokenType.PRINT,
            "true": TokenType.TRUE,
            "false": TokenType.FALSE,
            "nil": TokenType.NIL,
            "class": TokenType.CLASS,
        }

    def tokenize(self) -> List[Token]:
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(TokenType.EOF, "", None, self.line, self.column))
        return self.tokens

    def is_at_end(self) -> bool:
        return self.current >= len(self.source)

    def scan_token(self):
        char = self.advance()
        if char in " \r\t":
            return
        if char == '\n':
            self.line += 1
            self.column = 1
            return

        # Single-character tokens
        if char == '(': self.add_token(TokenType.LPAREN)
        elif char == ')': self.add_token(TokenType.RPAREN)
        elif char == '{': self.add_token(TokenType.LBRACE)
        elif char == '}': self.add_token(TokenType.RBRACE)
        elif char == '[': self.add_token(TokenType.LBRACKET)
        elif char == ']': self.add_token(TokenType.RBRACKET)
        elif char == ',': self.add_token(TokenType.COMMA)
        elif char == '.': self.add_token(TokenType.DOT)
        elif char == '-': self.add_token(TokenType.MINUS)
        elif char == '+': self.add_token(TokenType.PLUS)
        elif char == ';': self.add_token(TokenType.SEMICOLON)
        elif char == ':': self.add_token(TokenType.COLON)
        elif char == '*': self.add_token(TokenType.STAR)

        # Two-character tokens
        elif char == '!':
            self.add_token(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG)
        elif char == '=':
            self.add_token(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL)
        elif char == '<':
            self.add_token(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS)
        elif char == '>':
            self.add_token(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER)

        # Comments
        elif char == '/':
            if self.match('/'):
                while self.peek() != '\n' and not self.is_at_end():
                    self.advance()
            else:
                self.add_token(TokenType.SLASH)

        # Literals
        elif char == '"': self.string()
        elif self.is_digit(char): self.number()
        elif self.is_alpha(char): self.identifier()

        else:
            self.add_token(TokenType.UNKNOWN)

    def advance(self) -> str:
        self.current += 1
        self.column += 1
        return self.source[self.current - 1]

    def add_token(self, type: TokenType, literal: Any = None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(type, text, literal, self.line, self.column))

    def match(self, expected: str) -> bool:
        if self.is_at_end(): return False
        if self.source[self.current] != expected: return False
        self.current += 1
        self.column += 1
        return True

    def peek(self) -> str:
        if self.is_at_end(): return '\0'
        return self.source[self.current]

    def peek_next(self) -> str:
        if self.current + 1 >= len(self.source): return '\0'
        return self.source[self.current + 1]

    def string(self):
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == '\n':
                self.line += 1
                self.column = 0
            self.advance()

        if self.is_at_end():
            # Unterminated string
            self.add_token(TokenType.UNKNOWN)
            return

        self.advance() # The closing "
        value = self.source[self.start + 1:self.current - 1]
        self.add_token(TokenType.STRING, value)

    def is_digit(self, char: str) -> bool:
        return '0' <= char <= '9'

    def number(self):
        while self.is_digit(self.peek()):
            self.advance()

        if self.peek() == '.' and self.is_digit(self.peek_next()):
            self.advance()
            while self.is_digit(self.peek()):
                self.advance()

        value = float(self.source[self.start:self.current])
        self.add_token(TokenType.NUMBER, value)

    def is_alpha(self, char: str) -> bool:
        return 'a' <= char <= 'z' or 'A' <= char <= 'Z' or char == '_'

    def is_alpha_numeric(self, char: str) -> bool:
        return self.is_alpha(char) or self.is_digit(char)

    def identifier(self):
        while self.is_alpha_numeric(self.peek()):
            self.advance()

        text = self.source[self.start:self.current]
        token_type = self.KEYWORDS.get(text, TokenType.IDENTIFIER)
        self.add_token(token_type)
