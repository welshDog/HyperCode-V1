from typing import List

from .ast import *
from .lexer import Token
from .token_types import TokenType


class ParseError(Exception):
    pass


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0

    def parse(self) -> List[Stmt]:
        """Parse the entire program."""
        statements = []
        while not self.is_at_end():
            declaration = self.declaration()
            if declaration is not None:
                statements.append(declaration)
        return statements

    def declaration(self) -> Stmt:
        try:
            if self.match(TokenType.VAR):
                print("Found VAR token, calling var_declaration")
                stmt = self.var_declaration()
                print(f"Returning from var_declaration: {stmt}")
                return stmt
            return self.statement()
        except ParseError as e:
            print(f"Caught ParseError in declaration: {e}")
            self.synchronize()
            return None

    def var_declaration(self) -> Stmt:
        print("Starting var_declaration")

        # The 'var' keyword has already been consumed by the match() call in declaration()
        # So we can directly consume the identifier
        print(f"Current token before IDENTIFIER: {self.peek()}")
        name = self.consume(TokenType.IDENTIFIER, "Expected variable name.")
        print(f"Got identifier: {name.value}")

        # Parse the initializer if present
        initializer = None
        if self.match(TokenType.EQUAL):
            print("Found =, parsing expression")
            initializer = self.expression()

        # Require semicolon at the end
        print(f"Current token before semicolon: {self.peek()}")
        self.consume(TokenType.SEMICOLON, "Expected ';' after variable declaration.")
        print("Successfully parsed variable declaration")

        # Create and return the Var statement
        stmt = Var(name=name, initializer=initializer)
        print(f"Created Var statement: {stmt}")
        return stmt

    def statement(self) -> Stmt:
        if self.match(TokenType.PRINT):
            return self.print_statement()
        if self.match(TokenType.LBRACE):
            return Block(self.block())
        return self.expression_statement()

    def print_statement(self) -> Stmt:
        value = self.expression()
        self.consume(TokenType.SEMICOLON, "Expected ';' after value.")
        return Print(value)

    def expression_statement(self) -> Stmt:
        expr = self.expression()
        self.consume(TokenType.SEMICOLON, "Expected ';' after expression.")
        return Expression(expr)

    def block(self) -> List[Stmt]:
        statements = []
        while not self.check(TokenType.RIGHT_BRACE) and not self.is_at_end():
            statements.append(self.declaration())
        self.consume(TokenType.RIGHT_BRACE, "Expected '}' after block.")
        return statements

    def expression(self) -> Expr:
        return self.assignment()

    def assignment(self) -> Expr:
        expr = self.equality()

        if self.match(TokenType.EQUAL):
            equals = self.previous()
            value = self.assignment()

            if isinstance(expr, Variable):
                name = expr.name
                return Assign(name, value)

            self.error(equals, "Invalid assignment target.")

        return expr

    def equality(self) -> Expr:
        expr = self.comparison()

        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)

        return expr

    def comparison(self) -> Expr:
        expr = self.term()
        while self.match(
            TokenType.GREATER,
            TokenType.GREATER_EQUAL,
            TokenType.LESS,
            TokenType.LESS_EQUAL,
        ):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)
        return expr

    def term(self) -> Expr:
        expr = self.factor()
        while self.match(TokenType.MINUS, TokenType.PLUS):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)
        return expr

    def factor(self) -> Expr:
        expr = self.unary()
        while self.match(TokenType.SLASH, TokenType.STAR):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)
        return expr

    def unary(self) -> Expr:
        if self.match(TokenType.BANG, TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)
        return self.primary()

    def primary(self) -> Expr:
        if self.match(TokenType.FALSE):
            return Literal(False)
        if self.match(TokenType.TRUE):
            return Literal(True)
        if self.match(TokenType.NULL):
            return Literal(None)

        if self.match(TokenType.NUMBER, TokenType.STRING):
            # Convert the string value to the appropriate Python type
            token = self.previous()
            if token.type == TokenType.NUMBER:
                # Try to convert to int first, then float if needed
                try:
                    value = int(token.value)
                except ValueError:
                    value = float(token.value)
            else:  # STRING
                value = token.value
            return Literal(value)

        if self.match(TokenType.IDENTIFIER):
            return Variable(self.previous())

        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expected ')' after expression.")
            return Grouping(expr)

        raise self.error(self.peek(), "Expected expression.")

    # Helper methods
    def match(self, *types: TokenType) -> bool:
        for type_ in types:
            if self.check(type_):
                self.advance()
                return True
        return False

    def consume(self, type_: TokenType, message: str) -> Token:
        print(f"Consuming token. Expected: {type_}, Current: {self.peek()}")
        if self.check(type_):
            token = self.advance()
            print(f"Consumed token: {token}")
            return token
        error = self.error(self.peek(), message)
        print(f"Consume error: {error}")
        raise error

    def error(self, token: Token, message: str) -> ParseError:
        from .error_handler import report_parse_error

        report_parse_error(token, message)
        return ParseError()

    def synchronize(self) -> None:
        self.advance()
        while not self.is_at_end():
            if self.previous().type == TokenType.SEMICOLON:
                return

            # Only check for tokens that are statement starters
            if self.peek().type in (
                TokenType.VAR,
                TokenType.IF,
                TokenType.FOR,
                TokenType.WHILE,
                TokenType.PRINT,
                TokenType.RETURN,
                TokenType.FUNCTION,
            ):
                return

            self.advance()

    def check(self, type_: TokenType) -> bool:
        if self.is_at_end():
            return False
        return self.peek().type == type_

    def advance(self) -> Token:
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self) -> bool:
        return self.peek().type == TokenType.EOF

    def peek(self) -> Token:
        return self.tokens[self.current]

    def previous(self) -> Token:
        return self.tokens[self.current - 1]
