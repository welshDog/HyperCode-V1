from typing import List

from .ast import *
from .lexer import Token
from .tokens import TokenType


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
            if self.match(TokenType.FUN):
                return self.function("function")
            if self.match(TokenType.VAR):
                return self.var_declaration()
            return self.statement()
        except ParseError as e:
            self.synchronize()
            return None

    def var_declaration(self) -> Stmt:
        # The 'var' keyword has already been consumed by the match() call in declaration()
        # So we can directly consume the identifier
        name = self.consume(TokenType.IDENTIFIER, "Expected variable name.")

        # Parse the initializer if present
        initializer = None
        if self.match(TokenType.EQUAL):
            initializer = self.expression()

        # Require semicolon at the end
        self.consume(TokenType.SEMICOLON, "Expected ';' after variable declaration.")

        # Create and return the Var statement
        return Var(name=name, initializer=initializer)

    def statement(self) -> Stmt:
        if self.match(TokenType.IF):
            return self.if_statement()
        if self.match(TokenType.PRINT):
            return self.print_statement()
        if self.match(TokenType.RETURN):
            return self.return_statement()
        if self.match(TokenType.INTENT):
            return self.intent_statement()
        if self.match(TokenType.LBRACE):
            return Block(self.block())
        return self.expression_statement()

    def print_statement(self) -> Stmt:
        value = self.expression()
        self.consume(TokenType.SEMICOLON, "Expected ';' after value.")
        return Print(value)

    def return_statement(self) -> Stmt:
        keyword = self.previous()
        value = None
        if not self.check(TokenType.SEMICOLON):
            value = self.expression()
        self.consume(TokenType.SEMICOLON, "Expected ';' after return value.")
        return Return(keyword, value)

    def intent_statement(self) -> Stmt:
        # Parse the intent description (string literal)
        description = self.consume(TokenType.STRING, "Expected intent description string.")
        
        # Parse the intent block
        self.consume(TokenType.LBRACE, "Expected '{' after intent description.")
        statements = []
        while not self.check(TokenType.RBRACE) and not self.is_at_end():
            statements.append(self.declaration())
        self.consume(TokenType.RBRACE, "Expected '}' after intent block.")
        
        return Intent(description.literal, statements)

    def expression_statement(self) -> Stmt:
        expr = self.expression()
        self.consume(TokenType.SEMICOLON, "Expected ';' after expression.")
        return Expression(expr)

    def if_statement(self) -> Stmt:
        self.consume(TokenType.LPAREN, "Expected '(' after 'if'.")
        condition = self.expression()
        self.consume(TokenType.RPAREN, "Expected ')' after if condition.")

        then_branch = self.statement()
        else_branch = None
        if self.match(TokenType.ELSE):
            else_branch = self.statement()

        return If(condition, then_branch, else_branch)

    def function(self, kind: str) -> Fun:
        name = self.consume(TokenType.IDENTIFIER, f"Expected {kind} name.")
        self.consume(TokenType.LPAREN, f"Expected '(' after {kind} name.")
        parameters = []
        if not self.check(TokenType.RPAREN):
            while True:
                if len(parameters) >= 255:
                    self.error(self.peek(), "Can't have more than 255 parameters.")
                parameters.append(
                    self.consume(TokenType.IDENTIFIER, "Expected parameter name.")
                )
                if not self.match(TokenType.COMMA):
                    break
        self.consume(TokenType.RPAREN, "Expected ')' after parameters.")

        self.consume(TokenType.LBRACE, f"Expected '{{' before {kind} body.")
        body = self.block()
        return Fun(name, parameters, body)

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
        expr = self._primary()
        
        # Handle function calls and property access
        while True:
            if self.match(TokenType.LPAREN):
                expr = self.finish_call(expr)
            elif self.match(TokenType.DOT):
                name = self.consume(TokenType.IDENTIFIER, "Expected property name after '.'.")
                expr = Get(expr, name)
            else:
                break
            
        return expr
    
    def _primary(self) -> Expr:
        if self.match(TokenType.FALSE):
            return Literal(False)
        if self.match(TokenType.TRUE):
            return Literal(True)
        if self.match(TokenType.NIL):
            return Literal(None)

        if self.match(TokenType.NUMBER, TokenType.STRING):
            # Convert the string value to the appropriate Python type
            token = self.previous()
            if token.type == TokenType.NUMBER:
                # Try to convert to int first, then float if needed
                try:
                    value = int(token.literal)
                except ValueError:
                    value = float(token.literal)
            else:  # STRING
                value = token.literal
            return Literal(value)

        if self.match(TokenType.IDENTIFIER):
            return Variable(self.previous())

        if self.match(TokenType.LPAREN):
            expr = self.expression()
            self.consume(TokenType.RPAREN, "Expected ')' after expression.")    
            return Grouping(expr)

        raise self.error(self.peek(), "Expected expression.")
    
    def finish_call(self, callee: Expr) -> Call:
        paren = self.previous()
        arguments = []
        
        if not self.check(TokenType.RPAREN):
            arguments.append(self.expression())
            while self.match(TokenType.COMMA):
                arguments.append(self.expression())
        
        self.consume(TokenType.RPAREN, "Expected ')' after arguments.")
        return Call(callee, paren, arguments)

    # Helper methods
    def match(self, *types: TokenType) -> bool:
        for type_ in types:
            if self.check(type_):
                self.advance()
                return True
        return False

    def consume(self, type_: TokenType, message: str) -> Token:
        if self.check(type_):
            token = self.advance()
            return token
        error = self.error(self.peek(), message)
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
                TokenType.FUN,
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
