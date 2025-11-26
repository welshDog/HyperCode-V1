
from .ast import *
from .tokens import TokenType

from .ast import *
from .tokens import TokenType

class Return(Exception):
    def __init__(self, value):
        self.value = value

class HyperCodeFunction:
    def __init__(self, declaration: Fun, closure: "Environment"):
        self.declaration = declaration
        self.closure = closure

    def __str__(self):
        return f"<fn {self.declaration.name.lexeme}>"

    def arity(self):
        return len(self.declaration.params)

    def call(self, interpreter, arguments):
        environment = Environment(self.closure)
        for i, param in enumerate(self.declaration.params):
            environment.define(param.lexeme, arguments[i])

        try:
            interpreter.execute_block(self.declaration.body, environment)
        except Return as return_value:
            return return_value.value

        return None

class Environment:
    def __init__(self, enclosing=None):
        self.values = {}
        self.enclosing = enclosing

    def define(self, name: str, value):
        self.values[name] = value

    def get(self, name: Token):
        if name.lexeme in self.values:
            return self.values[name.lexeme]
        if self.enclosing is not None:
            return self.enclosing.get(name)
        raise RuntimeError(f"Undefined variable '{name.lexeme}'.")

    def assign(self, name: Token, value):
        if name.lexeme in self.values:
            self.values[name.lexeme] = value
            return
        if self.enclosing is not None:
            self.enclosing.assign(name, value)
            return
        raise RuntimeError(f"Undefined variable '{name.lexeme}'.")


class Interpreter(Visitor):
    def __init__(self):
        self.globals = Environment()
        self.environment = self.globals

    def interpret(self, statements: List[Stmt]):
        try:
            for statement in statements:
                self.execute(statement)
        except Exception as e:
            print(f"Runtime error: {e}")

    def execute(self, stmt: Stmt):
        stmt.accept(self)

    def execute_block(self, statements: List[Stmt], environment: Environment):
        previous = self.environment
        try:
            self.environment = environment
            for statement in statements:
                self.execute(statement)
        finally:
            self.environment = previous

    def evaluate(self, expr: Expr):
        return expr.accept(self)

    def visit_Expression(self, stmt: Expression):
        self.evaluate(stmt.expression)

    def visit_Print(self, stmt: Print):
        value = self.evaluate(stmt.expression)
        print(value)

    def visit_Var(self, stmt: Var):
        value = None
        if stmt.initializer is not None:
            value = self.evaluate(stmt.initializer)
        self.environment.define(stmt.name.lexeme, value)

    def visit_Block(self, stmt: Block):
        self.execute_block(stmt.statements, Environment(self.environment))

    def visit_Assign(self, expr: Assign):
        value = self.evaluate(expr.value)
        self.environment.assign(expr.name, value)
        return value

    def visit_Binary(self, expr: Binary):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)

        op_type = expr.operator.type

        if op_type == TokenType.PLUS:
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left + right
            if isinstance(left, str) and isinstance(right, str):
                return left + right
            raise RuntimeError("Operands must be two numbers or two strings.")
        if op_type == TokenType.MINUS:
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left - right
            raise RuntimeError("Operands must be numbers.")
        if op_type == TokenType.STAR:
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                return left * right
            raise RuntimeError("Operands must be numbers.")
        if op_type == TokenType.SLASH:
            if isinstance(left, (int, float)) and isinstance(right, (int, float)):
                if right == 0:
                    raise RuntimeError("Division by zero.")
                return left / right
            raise RuntimeError("Operands must be numbers.")
        
        if op_type == TokenType.GREATER:
            return left > right
        if op_type == TokenType.GREATER_EQUAL:
            return left >= right
        if op_type == TokenType.LESS:
            return left < right
        if op_type == TokenType.LESS_EQUAL:
            return left <= right

        if op_type == TokenType.BANG_EQUAL:
            return left != right
        if op_type == TokenType.EQUAL_EQUAL:
            return left == right

        return None # Should not happen

    def visit_Grouping(self, expr: Grouping):
        return self.evaluate(expr.expression)

    def visit_Literal(self, expr: Literal):
        return expr.value

    def visit_Unary(self, expr: Unary):
        right = self.evaluate(expr.right)

        op_type = expr.operator.type
        if op_type == TokenType.MINUS:
            if isinstance(right, (int, float)):
                return -right
            raise RuntimeError("Operand must be a number.")
        if op_type == TokenType.BANG:
            return not self.is_truthy(right)

        return None # Should not happen

    def visit_Variable(self, expr: Variable):
        return self.environment.get(expr.name)

    def visit_If(self, stmt: If):
        if self.is_truthy(self.evaluate(stmt.condition)):
            self.execute(stmt.then_branch)
        elif stmt.else_branch is not None:
            self.execute(stmt.else_branch)

    def is_truthy(self, obj):
        if obj is None:
            return False
        if isinstance(obj, bool):
            return obj
        return True

    def visit_Fun(self, stmt: Fun):
        function = HyperCodeFunction(stmt, self.environment)
        self.environment.define(stmt.name.lexeme, function)

    def visit_Return(self, stmt: Return):
        value = None
        if stmt.value is not None:
            value = self.evaluate(stmt.value)
        raise Return(value)

    def visit_Call(self, expr: Call):
        callee = self.evaluate(expr.callee)

        arguments = []
        for argument in expr.arguments:
            arguments.append(self.evaluate(argument))

        if not self.is_callable(callee):
            raise RuntimeError("Can only call functions and classes.")

        function = callee
        if len(arguments) != function.arity():
            raise RuntimeError(f"Expected {function.arity()} arguments but got {len(arguments)}.")

        return function.call(self, arguments)

    def is_callable(self, obj):
        return isinstance(obj, HyperCodeFunction)

# The Visitor pattern boilerplate
class Visitor:
    def visit_Expression(self, stmt: "Expression"):
        raise NotImplementedError
    def visit_Print(self, stmt: "Print"):
        raise NotImplementedError
    def visit_Var(self, stmt: "Var"):
        raise NotImplementedError
    def visit_Block(self, stmt: "Block"):
        raise NotImplementedError
    def visit_If(self, stmt: "If"):
        raise NotImplementedError
    def visit_Fun(self, stmt: "Fun"):
        raise NotImplementedError
    def visit_Return(self, stmt: "Return"):
        raise NotImplementedError
    def visit_Assign(self, expr: "Assign"):
        raise NotImplementedError
    def visit_Binary(self, expr: "Binary"):
        raise NotImplementedError
    def visit_Grouping(self, expr: "Grouping"):
        raise NotImplementedError
    def visit_Literal(self, expr: "Literal"):
        raise NotImplementedError
    def visit_Unary(self, expr: "Unary"):
        raise NotImplementedError
    def visit_Variable(self, expr: "Variable"):
        raise NotImplementedError
    def visit_Call(self, expr: "Call"):
        raise NotImplementedError

