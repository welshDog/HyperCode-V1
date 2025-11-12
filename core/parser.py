# Copyright 2025 welshDog (Lyndz Williams)
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Recursive descent parser for HyperCode."""

from dataclasses import dataclass
from typing import List, Optional, Union

from hypercode.core.lexer import Token, Token as TokenType 

class ParseError(Exception):
    """Raised when a parsing error occurs."""
    def __init__(self, message: str, token: Optional[Token] = None):
        self.message = message
        self.token = token
        super().__init__(self._format_message())

    def _format_message(self) -> str:
        if self.token:
            return f"[Line {self.token.line}] Error at '{self.token.value}': {self.message}"
        return f"Error: {self.message}"

@dataclass
class Expr:
    """Base class for all AST nodes."""
    pass

@dataclass
class Literal(Expr):
    value: object

@dataclass
class Binary(Expr):
    left: Expr
    operator: Token
    right: Expr

class Parser:
    """Recursive descent parser implementation."""
    
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0

    def parse(self) -> List[Expr]:
        """Parse the entire program."""
        try:
            return self.program()
        except ParseError as e:
            print(f"Parse error: {e}")
            return []

    def program(self) -> List[Expr]:
        """Parse a program (sequence of expressions)."""
        statements = []
        while not self.is_at_end():
            statements.append(self.expression())
            if self.match('SEMICOLON'):
                continue
            elif not self.is_at_end():
                 self.consume('SEMICOLON', "Expect ';' after expression.")
        return statements

    def expression(self) -> Expr:
        """Parse an expression."""
        return self.equality()

    def equality(self) -> Expr:
        """Parse equality expressions."""
        expr = self.comparison()

        while self.match('NOT_EQUALS', 'EQUALS'):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)

        return expr

    # Additional parsing methods...
    def comparison(self) -> Expr:
        """Parse comparison expressions."""
        expr = self.term()
        while self.match('GREATER', 'GREATER_EQUAL', 'LESS', 'LESS_EQUAL'):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)
        return expr

    def term(self) -> Expr:
        """Parse addition and subtraction."""
        expr = self.factor()
        while self.match('MINUS', 'PLUS'):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)
        return expr

    def factor(self) -> Expr:
        """Parse multiplication and division."""
        expr = self.unary()
        while self.match('DIVIDE', 'MULTIPLY'):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)
        return expr

    def unary(self) -> Expr:
        """Parse unary expressions."""
        if self.match('NOT', 'MINUS'):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)
        return self.primary()

    def primary(self) -> Expr:
        """Parse primary expressions (literals, grouping)."""
        if self.match('TRUE'): return Literal(True)
        if self.match('FALSE'): return Literal(False)
        if self.match('NULL'): return Literal(None)

        if self.match('NUMBER', 'STRING'):
            return Literal(self.previous().value)

        if self.match('LPAREN'):
            expr = self.expression()
            self.consume('RPAREN', "Expect ')' after expression.")
            return Grouping(expr)

        raise self.error(self.peek(), "Expect expression.")


    # Helper methods
    def match(self, *types: str) -> bool:
        """Check if the current token matches any of the given types."""
        for type_ in types:
            if self.check(type_):
                self.advance()
                return True
        return False

    def consume(self, type_: str, message: str) -> Token:
        """Consume a token of the given type or raise an error."""
        if self.check(type_):
            return self.advance()
        raise self.error(self.peek(), message)

    def error(self, token: Token, message: str) -> ParseError:
        """Create a parse error at the given token."""
        return ParseError(message, token)

    def synchronize(self) -> None:
        """Recover from a syntax error by synchronizing the parser."""
        self.advance()
        while not self.is_at_end():
            if self.previous().type == 'SEMICOLON':
                return
            # These token types are likely to start a new statement
            if self.peek().type in {
                'CLASS', 'FUNCTION', 'LET', 'CONST',
                'FOR', 'IF', 'WHILE',
                'PRINT', 'RETURN'
            }:
                return
            self.advance()
    
    # Private helper methods
    def peek(self) -> Token:
        return self.tokens[self.current]

    def previous(self) -> Token:
        return self.tokens[self.current - 1]

    def is_at_end(self) -> bool:
        return self.peek().type == 'EOF'

    def advance(self) -> Token:
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def check(self, type_: str) -> bool:
        if self.is_at_end():
            return False
        return self.peek().type == type_

@dataclass
class Unary(Expr):
    operator: Token
    right: Expr

@dataclass
class Grouping(Expr):
    expression: Expr
