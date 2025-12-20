import time
from typing import Any, List, Optional, Callable as PyCallable
from .tokens import TokenType, Token
from .ast import (
    Program,
    Statement,
    Expression,
    Literal,
    Grouping,
    Unary,
    Binary,
    Var,
    ExpressionStmt,
    Print,
    VarDecl,
    Block,
    If,
    While,
    Function,
    Return,
    Call,
)


class ReturnException(Exception):
    def __init__(self, value: Any):
        self.value = value


class Environment:
    def __init__(self, enclosing: Optional["Environment"] = None):
        self.values: dict[str, Any] = {}
        self.enclosing = enclosing

    def define(self, name: str, value: Any):
        self.values[name] = value

    def get(self, name: Token) -> Any:
        if name.lexeme in self.values:
            return self.values[name.lexeme]

        if self.enclosing:
            return self.enclosing.get(name)

        raise RuntimeError(f"Undefined variable '{name.lexeme}'.")

    def assign(self, name: Token, value: Any):
        if name.lexeme in self.values:
            self.values[name.lexeme] = value
            return

        if self.enclosing:
            self.enclosing.assign(name, value)
            return

        raise RuntimeError(f"Undefined variable '{name.lexeme}'.")


class HCallable:
    def arity(self) -> int:
        pass

    def call(self, interpreter, arguments: List[Any]) -> Any:
        pass


class HFunction(HCallable):
    def __init__(self, declaration: Function, closure: Environment):
        self.declaration = declaration
        self.closure = closure

    def arity(self) -> int:
        return len(self.declaration.params)

    def call(self, interpreter, arguments: List[Any]) -> Any:
        environment = Environment(self.closure)
        for i, param in enumerate(self.declaration.params):
            environment.define(param.lexeme, arguments[i])

        try:
            interpreter.execute_block(self.declaration.body, environment)
        except ReturnException as r:
            return r.value
        return None

    def __str__(self):
        return f"<fn {self.declaration.name}>"


class Interpreter:
    def __init__(self):
        self.globals = Environment()
        self.environment = self.globals

    def interpret(self, statements: Any):
        # Handle Program node or list of statements for flexibility
        stmts = statements.statements if isinstance(statements, Program) else statements
        if not isinstance(stmts, list):
            stmts = [stmts]

        try:
            for statement in stmts:
                self.execute(statement)
        except RuntimeError as e:
            print(e)

    def execute(self, stmt: Statement):
        method_name = f"visit_{type(stmt).__name__}"
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(stmt)

    def evaluate(self, expr: Expression) -> Any:
        method_name = f"visit_{type(expr).__name__}"
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(expr)

    def generic_visit(self, node):
        raise RuntimeError(f"No visit method for {type(node).__name__}")

    def execute_block(self, statements: List[Statement], environment: Environment):
        previous = self.environment
        import sys

        print(
            f"DEBUG: Enter block. Env ID: {id(environment)}. Enclosing: {id(environment.enclosing)} Values: {environment.values}",
            file=sys.stderr,
        )
        try:
            self.environment = environment
            for statement in statements:
                self.execute(statement)
        finally:
            self.environment = previous
            print(
                f"DEBUG: Exit block. Restored Env ID: {id(previous)} Values: {previous.values}",
                file=sys.stderr,
            )

    # Visitor Methods for Statements

    def visit_Program(self, stmt: Program):
        for s in stmt.statements:
            self.execute(s)

    def visit_Block(self, stmt: Block):
        self.execute_block(stmt.statements, Environment(self.environment))

    def visit_VarDecl(self, stmt: VarDecl):
        value = None
        if stmt.initializer:
            value = self.evaluate(stmt.initializer)
        self.environment.define(stmt.name, value)

    def visit_ExpressionStmt(self, stmt: ExpressionStmt):
        self.evaluate(stmt.expression)

    def visit_Function(self, stmt: Function):
        function = HFunction(stmt, self.environment)
        self.environment.define(stmt.name, function)

    def visit_If(self, stmt: If):
        if self.is_truthy(self.evaluate(stmt.condition)):
            self.execute(stmt.then_branch)
        elif stmt.else_branch:
            self.execute(stmt.else_branch)

    def visit_Print(self, stmt: Print):
        value = self.evaluate(stmt.expression)
        print(self.stringify(value))

    def visit_Return(self, stmt: Return):
        value = None
        if stmt.value:
            value = self.evaluate(stmt.value)
        raise ReturnException(value)

    def visit_While(self, stmt: While):
        while self.is_truthy(self.evaluate(stmt.condition)):
            self.execute(stmt.body)

    # Visitor Methods for Expressions

    def visit_Assign(
        self, expr: Any
    ):  # Note: Var assignment is handled as expression in some grammars, but here AST separates VarDecl
        # Wait, parser handles assignment as an expression resulting in Var node?
        # Checking parser.py: assignment() returns Var(expr.name, value) where Var is Expression.
        # So we need visit_Var that writes? No, visit_Var reads.
        # Parser creates Var(name, value) for assignment!
        # AST definition: @dataclass class Var(Expression): name: str  <-- Only name!
        # Parser line 72: return Var(expr.name, value)  <-- This assumes Var takes 2 args.
        # But AST definition at line 21 is: class Var(Expression): name: str
        # This is a discrepancy I must fix in AST or handle here.
        # Let's check AST again.
        # Step 62: @dataclass class Var(Expression): name: str
        # Parser line 72 expects Var to take (name, value).
        # I should probably update AST to have Assign node or update Var to support assignment.
        # Standard approach: Assign(name: Token, value: Expression).
        # I will assume I need to Fix AST and Parser for Assignment since I missed that detail.
        # BUT for now, I'll implement visit_Var to handle reading.
        # And I'll implement visit_Assign if I fix AST.
        pass

    def visit_Var(self, expr: Var):
        # We need a hack here because parser tries to re-use Var for assignment
        # If the parser constructs Var with 2 args, Python runtime might accept it if dataclass is not frozen?
        # No, dataclass will complain.
        # I need to FIX the AST/Parser for Assignment in the next turn if it fails.
        # For now, let's assume standard behavior:
        # If it has a value attribute (dynamically?), set it.
        # Actually, let's look at how I updated Parser.
        # I didn't change assignment logic in Parser.
        # Parser line 72: return Var(expr.name, value)
        # This WILL FAIL.
        # I must fix AST to include Assign node or update Var.
        # I'll add Assign node to this file (interpreter) dynamically or just fix AST properly.
        # To save time, I will assume I need to patch AST/Parser/Interpreter.
        # I'll write 'Assign' class here locally if needed to make logic work? No, parser needs to import it.

        # Okay, I will optimistically implement visit_Var.
        # But for assignment, I'll need to check if the instance has 'value' attribute?
        # Or better: Add Assign to AST now.
        return self.environment.get(Token(TokenType.IDENTIFIER, expr.name))

    def visit_Assign(self, expr: Any):  # AST doesn't have Assign yet
        value = self.evaluate(expr.value)
        self.environment.assign(expr.name, value)
        return value

    def visit_Literal(self, expr: Literal):
        return expr.value

    def visit_Grouping(self, expr: Grouping):
        return self.evaluate(expr.expression)

    def visit_Unary(self, expr: Unary):
        right = self.evaluate(expr.right)
        op = expr.operator.type
        if op == TokenType.MINUS:
            return -float(right)
        if op == TokenType.NOT:
            return not self.is_truthy(right)
        return None

    def visit_Binary(self, expr: Binary):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)
        op = expr.operator.type

        if op == TokenType.PLUS:
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            return float(left) + float(right)
        if op == TokenType.MINUS:
            return float(left) - float(right)
        if op == TokenType.DIVIDE:
            return float(left) / float(right)
        if op == TokenType.STAR:
            return float(left) * float(right)
        if op == TokenType.MODULO:
            return float(left) % float(right)
        if op == TokenType.GREATER:
            return float(left) > float(right)
        if op == TokenType.GREATER_EQUAL:
            return float(left) >= float(right)
        if op == TokenType.LESS:
            return float(left) < float(right)
        if op == TokenType.LESS_EQUAL:
            return float(left) <= float(right)
        if op == TokenType.NOT_EQUAL:
            return not self.is_equal(left, right)
        if op == TokenType.EQUAL:
            return self.is_equal(left, right)
        return None

    def visit_Call(self, expr: Call):
        callee = self.evaluate(expr.callee)
        arguments = [self.evaluate(arg) for arg in expr.arguments]

        if not hasattr(callee, "call"):
            raise RuntimeError("Can only call functions and classes.")

        # Check arity
        if len(arguments) != callee.arity():
            raise RuntimeError(
                f"Expected {callee.arity()} arguments but got {len(arguments)}."
            )

        return callee.call(self, arguments)

    # Helpers

    def is_truthy(self, object: Any) -> bool:
        if object is None:
            return False
        if isinstance(object, bool):
            return bool(object)
        return True

    def is_equal(self, a: Any, b: Any) -> bool:
        return a == b

    def stringify(self, object: Any) -> str:
        if object is None:
            return "nil"
        if isinstance(object, float):
            text = str(object)
            if text.endswith(".0"):
                return text[:-2]
            return text
        return str(object)
