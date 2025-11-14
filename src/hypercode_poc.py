"""
HyperCode POC - Neurodivergent-First Programming Language
Research-Backed Implementation

Combining:
- Plankalkül (1942): Spatial layout + explicit types
- Brainfuck (1993): Minimalism (8 core operations)
- Befunge (1993): 2D spatial programming
- Whitespace (2003): Pattern-based syntax
+ Modern AI integration + Accessibility-first design
"""

from enum import Enum
from typing import Dict, List, Tuple, Optional, Any
from dataclasses import dataclass, field

class TokenType(Enum):
    """Brainfuck-inspired core + modern aliases"""
    MOVE_RIGHT, MOVE_LEFT = ">", "<"
    INCREMENT, DECREMENT = "+", "-"
    OUTPUT, INPUT = ".", ","
    LOOP_START, LOOP_END = "[", "]"
    LET, PRINT, IF, ELSE = "let", "print", "if", "else"
    LOOP, WHILE, FN, RETURN = "loop", "while", "fn", "return"
    STRING = "STRING"
    NUMBER = "NUMBER"
    IDENTIFIER = "IDENTIFIER"
    EOF = "EOF"

@dataclass
class Token:
    type: TokenType
    value: str
    line: int
    column: int

class UserConfidenceLevel(Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"

class EnhancedLexer:
    """Smart tokenizer with escape handling + accessibility focus"""

    def __init__(self):
        self.tokens = []
        self.line, self.column, self.position = 1, 1, 0
        self.source = ""
        self.brainfuck_ops = {
            '>': ">", '<': "<", '+': "+", '-': "-",
            '.': ".", ',': ",", '[': "[", ']': "]"
        }
        self.keywords = {
            'let': "let", 'print': "print", 'if': "if",
            'else': "else", 'loop': "loop", 'fn': "fn"
        }

    def tokenize(self, source: str) -> Tuple[List[Token], List[str]]:
        self.source, self.position, self.line, self.column = source, 0, 1, 1
        self.tokens, errors = [], []

        while self.position < len(self.source):
            char = self.source[self.position]

            if char in ' \t':
                self.advance()
            elif char == '\n':
                self.line += 1
                self.column, self.position = 1, self.position + 1
            elif char == '#':
                while self.position < len(self.source) and self.source[self.position] != '\n':
                    self.advance()
            elif char in '\"' + "'":  # String handling
                self.handle_string(char, errors)
            elif char.isdigit():
                self.handle_number()
            elif char.isalpha() or char == '_':
                self.handle_identifier()
            elif char in self.brainfuck_ops:
                self.tokens.append(Token(TokenType(self.brainfuck_ops[char]), char, self.line, self.column))
                self.advance()
            else:
                errors.append(f"Unknown char: {char} at L{self.line}:C{self.column}")
                self.advance()

        self.tokens.append(Token(TokenType.EOF, '', self.line, self.column))
        return self.tokens, errors

    def handle_string(self, quote, errors):
        start_line, start_col = self.line, self.column
        self.advance()
        value = ""
        while self.position < len(self.source):
            c = self.source[self.position]
            if c == '\\' and self.position + 1 < len(self.source):
                next_c = self.source[self.position + 1]
                if next_c in 'nt':
                    value += '\n' if next_c == 'n' else '\t'
                    self.advance()
                    self.advance()
                else:
                    value += c
                    self.advance()
            elif c == quote:
                self.advance()
                self.tokens.append(Token(TokenType.STRING, value, start_line, start_col))
                return
            else:
                value += c
                self.advance()
        errors.append(f"Unclosed string at L{start_line}:C{start_col}")

    def handle_number(self):
        value = ""
        start_col = self.column
        while self.position < len(self.source) and self.source[self.position].isdigit():
            value += self.source[self.position]
            self.advance()
        self.tokens.append(Token(TokenType.NUMBER, value, self.line, start_col))

    def handle_identifier(self):
        value = ""
        start_col = self.column
        while self.position < len(self.source) and (self.source[self.position].isalnum() or self.source[self.position] == '_'):
            value += self.source[self.position]
            self.advance()
        token_type = self.keywords.get(value, "IDENTIFIER")
        self.tokens.append(Token(TokenType(token_type) if token_type != "IDENTIFIER" else TokenType.IDENTIFIER, value, self.line, start_col))

    def advance(self):
        self.position += 1
        self.column += 1

class ContextAwareErrorMessenger:
    """Friendly, adaptive error messages"""
    def __init__(self):
        self.errors = []

    def format_error(self, msg: str, line: int, col: int, level: UserConfidenceLevel):
        if level == UserConfidenceLevel.BEGINNER:
            return f"Hey! Issue at L{line}:C{col} - {msg}. Tip: Check syntax here."
        else:
            return f"L{line}:C{col} - {msg}"

class SemanticContextStreamer:
    """Understand programmer intent from tokens"""
    def analyze(self, tokens: List[Token]) -> Dict[str, Any]:
        intent = "unknown"
        patterns = []
        for token in tokens:
            if token.type == TokenType.LET:
                intent, patterns = "assignment", ["declaration"]
            elif token.type == TokenType.IF:
                intent, patterns = "conditional", ["branching"]
            elif token.type == TokenType.LOOP:
                intent, patterns = "iteration", ["looping"]
        return {"intent": intent, "patterns": patterns, "confidence": len(patterns) / 3.0}

class ConfidenceTracker:
    """Adapt system guidance to user skill level"""
    def __init__(self, level=UserConfidenceLevel.BEGINNER):
        self.level = level
        self.actions, self.errors = 0, 0

    def record(self, success: bool):
        self.actions += 1
        if not success:
            self.errors += 1

class HyperCodePOC:
    """Main system: Lexer + Error Messenger + Semantic Analyzer + Confidence Tracker"""
    def __init__(self, level=UserConfidenceLevel.BEGINNER):
        self.lexer = EnhancedLexer()
        self.error_messenger = ContextAwareErrorMessenger()
        self.semantic = SemanticContextStreamer()
        self.confidence = ConfidenceTracker(level)
        self.last_tokens, self.last_errors = [], []

    def compile(self, code: str) -> Dict[str, Any]:
        tokens, errors = self.lexer.tokenize(code)
        self.last_tokens, self.last_errors = tokens, errors
        semantic = self.semantic.analyze(tokens)
        return {
            "status": "success" if not errors else "warning",
            "tokens": len(tokens),
            "intent": semantic["intent"],
            "patterns": semantic["patterns"],
            "confidence": min(semantic["confidence"], 1.0),
            "errors": errors
        }

# Demo
if __name__ == "__main__":
    hc = HyperCodePOC()

    demos = [
        ('let x = 42', 'Simple variable'),
        ('print "Hello"', 'Output'),
        ('if (x > 0) { print "yes" }', 'Conditional'),
        ('loop { print "spin" }', 'Loop'),
    ]

    for code, desc in demos:
        result = hc.compile(code)
        print(f"{desc}: {result['intent']} ({result['confidence']:.0%})")
