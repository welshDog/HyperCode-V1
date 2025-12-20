# src/hypercode/core/parser.py
from typing import List, Optional, Dict, Any, Union
from .tokens import Token, TokenType
from .ast import (
    Program, Statement, Expression, VarDecl, Function, Block,
    If, While, Print, Return, ExpressionStmt, Assign,
    Binary, Unary, Literal, Grouping, Call, Var
)


class ParserError(Exception):
    """Exception raised for errors during parsing.
    
    Attributes:
        token: The token where the error occurred
        message: Explanation of the error
    """
    
    def __init__(self, token: Token, message: str) -> None:
        self.token = token
        self.message = message
        super().__init__(self.message)


class Parser:
    """Parser for the HyperCode language.
    
    The parser converts a sequence of tokens into an Abstract Syntax Tree (AST).
    It uses a recursive descent parsing approach with Pratt parsing for expressions.
    """
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.current = 0
        self.had_error = False

    def error(self, token: Token, message: str) -> ParserError:
        """Report a parsing error."""
        self.had_error = True
        error_msg = f"[Line {token.line}] Error at '{token.lexeme}': {message}"
        print(error_msg)  # Print the error to help with debugging
        return ParserError(token, message)
    
    def synchronize(self) -> None:
        """Discard tokens until we find a statement boundary."""
        self.advance()
        
        while not self.is_at_end():
            if self.previous().type == TokenType.SEMICOLON or self.previous().type == TokenType.NEWLINE:
                return
                
            if self.peek().type in [
                TokenType.CLASS, TokenType.FUNCTION, TokenType.VAR, TokenType.LET,
                TokenType.FOR, TokenType.IF, TokenType.WHILE, TokenType.PRINT,
                TokenType.RETURN
            ]:
                return
                
            self.advance()
    
    def parse(self) -> Program:
        """Parse the tokens into an AST.
        
        Returns:
            The parsed program as an AST.
            
        Raises:
            ParserError: If there's a syntax error in the source code.
        """
        statements = []
        self.had_error = False
        
        while not self.is_at_end():
            try:
                stmt = self.declaration()
                if stmt:
                    statements.append(stmt)
            except ParserError as e:
                print(f"[line {e.token.line}] Error: {e.message}")
                self.synchronize()
                
        if self.had_error:
            raise ParserError(self.peek(), "Failed to parse due to previous errors")
            
        return Program(statements)

    def declaration(self) -> Optional[Statement]:
        """Parse a declaration."""
        try:
            # Skip newlines at the start
            while self.match(TokenType.NEWLINE):
                pass
                
            if self.is_at_end():
                return None
                
            if self.match(TokenType.FUNCTION):
                return self.function("function")
            if self.match(TokenType.VAR, TokenType.LET):
                return self.var_declaration()
                
            return self.statement()
            
        except ParserError as e:
            print(f"Error in declaration: {e}")
            self.synchronize()
            return None

    def statement(self) -> Optional[Statement]:
        """Parse a statement."""
        try:
            # Skip newlines at the start
            while self.match(TokenType.NEWLINE):
                pass
                
            if self.is_at_end():
                return None
                
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
                
            # Try to parse an expression statement
            if self.check_expression_start():
                return self.expression_statement()
                
            # If we get here, we couldn't parse a statement
            if not self.is_at_end():
                self.error(self.peek(), f"Unexpected token in statement: {self.peek().type}")
                
            return None
            
        except ParserError as e:
            print(f"Error in statement: {e}")
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

        self.consume_newline_or_semicolon("Expect newline or ';' after variable declaration.")
        return VarDecl(name.lexeme, initializer)

    def statement(self) -> Optional[Statement]:
        """Parse a statement."""
        try:
            # Skip newlines at the start
            while self.match(TokenType.NEWLINE):
                pass
                
            if self.is_at_end():
                return None
                
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
                
            # Try to parse an expression statement
            if self.check_expression_start():
                return self.expression_statement()
                
            # If we get here, we couldn't parse a statement
            if not self.is_at_end():
                self.error(self.peek(), f"Unexpected token in statement: {self.peek().type}")
                
            return None
            
        except ParserError as e:
            print(f"Error in statement: {e}")
            self.synchronize()
            return None
            
    def check_expression_start(self) -> bool:
        """Check if the current token can start an expression."""
        token = self.peek()
        return token.type in [
            TokenType.IDENTIFIER, TokenType.STRING, TokenType.NUMBER, TokenType.TRUE,
            TokenType.FALSE, TokenType.NIL, TokenType.LEFT_PAREN, TokenType.MINUS,
            TokenType.BANG, TokenType.LEFT_BRACKET, TokenType.LEFT_BRACE
        ]

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
        # For now, we'll implement a simplified version that just parses the syntax
        # but doesn't actually implement the full for loop semantics
        self.consume(TokenType.LEFT_PAREN, "Expect '(' after 'for'.")
        
        # Parse the initialization
        if self.match(TokenType.SEMICOLON):
            initializer = None
        elif self.match(TokenType.VAR, TokenType.LET):
            initializer = self.var_declaration()
        else:
            initializer = self.expression_statement()
        
        # Parse the condition
        condition = None
        if not self.check(TokenType.SEMICOLON):
            condition = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after loop condition.")
        
        # Parse the increment
        increment = None
        if not self.check(TokenType.RIGHT_PAREN):
            increment = self.expression()
        self.consume(TokenType.RIGHT_PAREN, "Expect ')' after for clauses.")
        
        # Parse the body
        body = self.statement()
        
        # For now, we'll just return a while loop with the same behavior
        if condition is None:
            condition = Literal(True)
            
        # If there's an increment, add it to the end of the body
        if increment is not None:
            if isinstance(body, Block):
                body.statements.append(ExpressionStmt(increment))
            else:
                body = Block([body, ExpressionStmt(increment)])
                
        # Create the while loop
        while_loop = While(condition, body)
        
        # If there's an initializer, wrap it in a block with the while loop
        if initializer is not None:
            return Block([initializer, while_loop])
            
        return while_loop

    def print_statement(self) -> Statement:
        value = self.expression()
        self.consume_newline_or_semicolon("Expect newline or ';' after value.")
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

    def consume_newline_or_semicolon(self, message: str) -> None:
        """Consume either a newline or semicolon."""
        if not (self.match(TokenType.SEMICOLON) or self.match(TokenType.NEWLINE)):
            # If we don't have a semicolon or newline, look ahead to see if we're at the end of the line
            if not (self.is_at_end() or self.check(TokenType.RIGHT_BRACE) or self.check(TokenType.ELSE) or self.check(TokenType.END)):
                self.error(self.peek(), message)

    def expression_statement(self) -> Statement:
        """Parse an expression statement."""
        expr = self.expression()
        self.consume_newline_or_semicolon("Expect newline or ';' after expression.")
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
