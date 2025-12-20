# src/hypercode/core/parser.py
from typing import List, Optional, Any, Dict, Union
from .tokens import Token, TokenType
from .ast import (
    Expression,
    Statement,
    Var,
    Binary,
    Unary,
    Grouping,
    Literal,
    Call,
    ExpressionStmt,
    VarDecl,
    Program,
    Block,
    If,
    While,
    Function,
    Return,
    Print,
    Assign,
)


class ParserError(Exception):
    def __init__(self, message: str, token: Token):
        self.message = message
        self.token = token
        super().__init__(f"{message} at line {token.line}, column {token.column}")


class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0

    def parse(self) -> Program:
        """Parse the tokens into an AST."""
        statements = []
        while not self.is_at_end():
            stmt = self.declaration()
            if stmt:
                statements.append(stmt)
        return Program(statements)

    def declaration(self) -> Optional[Statement]:
        """Parse a declaration."""
        try:
            if self.match(TokenType.FUNCTION):
                return self.function("function")
            if self.match(TokenType.VAR):
                return self.var_declaration()
            return self.statement()
        except ParserError as e:
            self.synchronize()
            return None

    def function(self, kind: str) -> Function:
        """Parse a function declaration."""
        name = self.consume(TokenType.IDENTIFIER, f"Expect {kind} name.")
        self.consume(TokenType.LEFT_PAREN, f"Expect '(' after {kind} name.")
        parameters = []
        if not self.check(TokenType.RIGHT_PAREN):
            while True:
                if len(parameters) >= 255:
                    self.error(self.peek(), "Can't have more than 255 parameters.")
                parameters.append(
                    self.consume(TokenType.IDENTIFIER, "Expect parameter name.")
                )
                if not self.match(TokenType.COMMA):
                    break
        self.consume(TokenType.RIGHT_PAREN, "Expect ')' after parameters.")
        self.consume(TokenType.LEFT_BRACE, f"Expect '{{' before {kind} body.")
        body = self.block()
        return Function(name.lexeme, parameters, body)

    def var_declaration(self) -> Statement:
        """Parse a variable declaration."""
        name = self.consume(TokenType.IDENTIFIER, "Expect variable name.")

        initializer = None
        if self.match(TokenType.ASSIGN):
            initializer = self.expression()

        self.consume(TokenType.SEMICOLON, "Expect ';' after variable declaration.")
        return VarDecl(name.lexeme, initializer)

    def statement(self) -> Statement:
        """Parse a statement."""
        if self.match(TokenType.IF):
            return self.if_statement()
        if self.match(TokenType.WHILE):
            return self.while_statement()
        if self.match(TokenType.FOR):
            return self.for_statement()
        if self.match(TokenType.PRINT):
            return self.print_statement()
        if self.match(TokenType.RETURN):
            return self.return_statement()
        if self.match(TokenType.LEFT_BRACE):
            return Block(self.block())

        return self.expression_statement()

    def if_statement(self) -> Statement:
        self.consume(TokenType.LEFT_PAREN, "Expect '(' after 'if'.")
        condition = self.expression()
        self.consume(TokenType.RIGHT_PAREN, "Expect ')' after if condition.")
        then_branch = self.statement()
        else_branch = None
        if self.match(TokenType.ELSE):
            else_branch = self.statement()
        return If(condition, then_branch, else_branch)

    def while_statement(self) -> Statement:
        self.consume(TokenType.LEFT_PAREN, "Expect '(' after 'while'.")
        condition = self.expression()
        self.consume(TokenType.RIGHT_PAREN, "Expect ')' after while condition.")
        body = self.statement()
        return While(condition, body)

    def for_statement(self) -> Statement:
        self.consume(TokenType.LEFT_PAREN, "Expect '(' after 'for'.")

        initializer = None
        if self.match(TokenType.SEMICOLON):
            initializer = None
        elif self.match(TokenType.VAR):
            initializer = self.var_declaration()
        else:
            initializer = self.expression_statement()

        condition = None
        if not self.check(TokenType.SEMICOLON):
            condition = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after loop condition.")

        increment = None
        if not self.check(TokenType.RIGHT_PAREN):
            increment = self.expression()
        self.consume(TokenType.RIGHT_PAREN, "Expect ')' after for clauses.")

        body = self.statement()

        if increment:
            body = Block([body, ExpressionStmt(increment)])

        if condition is None:
            condition = Literal(True)
        body = While(condition, body)

        if initializer:
            body = Block([initializer, body])

        return body

    def print_statement(self) -> Statement:
        value = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after value.")
        return Print(value)

    def return_statement(self) -> Statement:
        keyword = self.previous()
        value = None
        if not self.check(TokenType.SEMICOLON):
            value = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after return value.")
        return Return(keyword, value)

    def block(self) -> List[Statement]:
        statements = []
        while not self.check(TokenType.RIGHT_BRACE) and not self.is_at_end():
            statements.append(self.declaration())
        self.consume(TokenType.RIGHT_BRACE, "Expect '}' after block.")
        return statements

    def expression_statement(self) -> Statement:
        """Parse an expression statement."""
        expr = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after expression.")
        return ExpressionStmt(expr)

    def expression(self) -> Expression:
        """Parse an expression."""
        return self.assignment()

    def assignment(self) -> Expression:
        """Parse an assignment expression."""
        expr = self.equality()

        if self.match(TokenType.ASSIGN):
            equals = self.previous()
            value = self.assignment()

            if isinstance(expr, Var):
                # Convert Var expression to assignment target
                # We need a Token for the name, but Var only has the string name.
                # We'll rely on the interpreter to handle the Token/String conversion or reconstruction
                # Or better: check how Var is created. It's from IDENTIFIER token.
                # We'll use the 'equals' token location for error reporting, but we need the name token.
                # Let's reconstruct a Token for now or update AST Var to hold Token.
                # For MVP, let's just assume we can pass the string name if we change Assign to take string?
                # No, standard Lox use Token.
                # Let's change Assign in AST to take str?
                # Or just assume expr.name is the name.
                # Wait, Var has .name (str).
                # New Assign(name: Token, value: Expression).
                # We can mock the token.
                name_token = Token(
                    TokenType.IDENTIFIER, expr.name, None, equals.line, equals.column
                )
                return Assign(name_token, value)

            raise ParserError("Invalid assignment target.", equals)

        return expr

    def equality(self) -> Expression:
        """Parse an equality expression."""
        expr = self.comparison()

        while self.match(TokenType.NOT_EQUAL, TokenType.EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)

        return expr

    def comparison(self) -> Expression:
        """Parse a comparison expression."""
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

    def term(self) -> Expression:
        """Parse a term expression."""
        expr = self.factor()

        while self.match(TokenType.MINUS, TokenType.PLUS):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)

        return expr

    def factor(self) -> Expression:
        """Parse a factor expression."""
        expr = self.unary()

        while self.match(TokenType.DIVIDE, TokenType.STAR, TokenType.MODULO):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)

        return expr

    def unary(self) -> Expression:
        """Parse a unary expression."""
        if self.match(TokenType.NOT, TokenType.MINUS):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)

        return self.primary()

    def primary(self) -> Expression:
        """Parse a primary expression."""
        if self.match(TokenType.FALSE):
            return Literal(False)
        if self.match(TokenType.TRUE):
            return Literal(True)
        if self.match(TokenType.NIL):
            return Literal(None)

        if self.match(TokenType.NUMBER, TokenType.STRING):
            return Literal(self.previous().literal)

        if self.match(TokenType.IDENTIFIER):
            return Var(self.previous().lexeme)

        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN, "Expect ')' after expression.")
            return Grouping(expr)

        raise ParserError("Expect expression.", self.peek())

    # Helper methods
    def match(self, *types: TokenType) -> bool:
        """Check if the current token matches any of the given types."""
        for type_ in types:
            if self.check(type_):
                self.advance()
                return True
        return False

    def consume(self, type_: TokenType, message: str) -> Token:
        """Consume a token of the given type or raise an error."""
        if self.check(type_):
            return self.advance()

        raise ParserError(message, self.peek())

    def check(self, type_: TokenType) -> bool:
        """Check if the current token is of the given type."""
        if self.is_at_end():
            return False
        return self.peek().type == type_

    def advance(self) -> Token:
        """Advance to the next token and return the previous one."""
        if not self.is_at_end():
            self.current += 1
        return self.previous()

    def is_at_end(self) -> bool:
        """Check if we've consumed all tokens."""
        return self.peek().type == TokenType.EOF

    def peek(self) -> Token:
        """Return the current token without consuming it."""
        return self.tokens[self.current]

    def previous(self) -> Token:
        """Return the most recently consumed token."""
        return self.tokens[self.current - 1]

    def synchronize(self) -> None:
        """Recover from a syntax error by discarding tokens until a statement boundary."""
        self.advance()

        while not self.is_at_end():
            if self.previous().type == TokenType.SEMICOLON:
                return

            if self.peek().type in (
                TokenType.CLASS,
                TokenType.FUNCTION,
                TokenType.VAR,
                TokenType.FOR,
                TokenType.IF,
                TokenType.WHILE,
                TokenType.PRINT,
                TokenType.RETURN,
            ):
                return

            self.advance()
