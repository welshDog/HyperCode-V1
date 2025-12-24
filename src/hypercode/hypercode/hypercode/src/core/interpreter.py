# HyperCode Interpreter - Executes HyperCode AST
import time
from typing import Any
from typing import Callable as PyCallable
from typing import Dict, List

from .ast import *
from .tokens import Token, TokenType


class RuntimeError(Exception):
    def __init__(self, message: str, token: Token = None):
        self.message = message
        self.token = token
        super().__init__(self.message)


class Environment:
    def __init__(self, enclosing=None):
        self.values: Dict[str, Any] = {}
        self.enclosing = enclosing

    def define(self, name: str, value: Any):
        self.values[name] = value

    def get(self, name: str):
        if name in self.values:
            return self.values[name]
        if self.enclosing:
            return self.enclosing.get(name)
        raise RuntimeError(f"Undefined variable '{name}'")

    def assign(self, name: str, value: Any):
        if name in self.values:
            self.values[name] = value
            return
        if self.enclosing:
            self.enclosing.assign(name, value)
            return
        raise RuntimeError(f"Undefined variable '{name}'")


class Callable:
    def arity(self) -> int:
        raise NotImplementedError()

    def call(self, interpreter, arguments: List[Any]) -> Any:
        raise NotImplementedError()


class HyperCodeFunction(Callable):
    def __init__(self, declaration, closure):
        self.declaration = declaration
        self.closure = closure

    def call(self, interpreter, arguments):
        environment = Environment(self.closure)
        for i in range(len(self.declaration.params)):
            environment.define(self.declaration.params[i].lexeme, arguments[i])

        try:
            interpreter.execute_block(self.declaration.body, environment)
        except ReturnException as return_value:
            return return_value.value

        return None

    def arity(self):
        return len(self.declaration.params)


class ReturnException(Exception):
    def __init__(self, value):
        self.value = value


class Interpreter:
    def __init__(self):
        self.globals = Environment()
        self.environment = self.globals
        self.output: List[str] = []
        self.locals = {}

        # Native functions
        class Clock(Callable):
            def arity(self) -> int:
                return 0

            def call(self, interpreter, arguments: List[Any]) -> float:
                return time.time()

            def __str__(self) -> str:
                return "<native fn>"

        class Double(Callable):
            def arity(self) -> int:
                return 1

            def call(self, interpreter, arguments: List[Any]) -> float:
                if not isinstance(arguments[0], (int, float)):
                    raise RuntimeError("Operand must be a number.")
                return arguments[0] * 2

            def __str__(self) -> str:
                return "<native fn>"

        class Square(Callable):
            def arity(self) -> int:
                return 1

            def call(self, interpreter, arguments: List[Any]) -> float:
                if not isinstance(arguments[0], (int, float)):
                    raise RuntimeError("Operand must be a number.")
                return arguments[0] * arguments[0]

            def __str__(self) -> str:
                return "<native fn>"

        self.globals.define("clock", Clock())
        self.globals.define("double", Double())
        self.globals.define("square", Square())

    def execute_block(self, statements, environment):
        previous = self.environment
        try:
            self.environment = environment
            for statement in statements:
                self.execute(statement)
        finally:
            self.environment = previous

    def interpret(self, statements: List[Stmt]):
        try:
            for statement in statements:
                self.execute(statement)
        except ReturnException:
            # A return from the top-level script. We can just ignore it and exit gracefully.
            pass
        except RuntimeError as error:
            print(f"❌ Runtime Error: {error.message}")
            if error.token:
                print(f"   at line {error.token.line}")

    def execute(self, stmt: Stmt):
        return stmt.accept(self)

    def evaluate(self, expr: Expr):
        return expr.accept(self)

    def visit_Expression(self, stmt: Expression):
        self.evaluate(stmt.expression)
        return None

    def visit_Print(self, stmt: Print):
        value = self.evaluate(stmt.expression)
        output = self.stringify(value)
        self.output.append(output)
        print(output)
        return None

    def visit_Let(self, stmt: Let):
        value = None
        if stmt.initializer:
            value = self.evaluate(stmt.initializer)
        self.environment.define(stmt.name.lexeme, value)
        return None

    def visit_Block(self, stmt: Block):
        self.execute_block(stmt.statements, Environment(self.environment))
        return None

    def visit_BlockDecl(self, stmt: BlockDecl):
        # For now, just execute the block in a new scope.
        # In the future, this could define a callable/reusable block.
        self.execute_block(stmt.body, Environment(self.environment))
        return None

    def visit_Intent(self, stmt: Intent):
        for statement in stmt.statements:
            self.execute(statement)
        return None

    def visit_Function(self, stmt: Function):
        function = HyperCodeFunction(stmt, self.environment)
        self.environment.define(stmt.name.lexeme, function)
        return None

    def visit_Return(self, stmt: Return):
        value = None
        if stmt.value is not None:
            value = self.evaluate(stmt.value)
        raise ReturnException(value)

    def visit_Literal(self, expr: Literal):
        return expr.value

    def visit_Grouping(self, expr: Grouping):
        return self.evaluate(expr.expression)

    def visit_Variable(self, expr: Variable):
        return self.environment.get(expr.name.lexeme)

    def visit_Assign(self, expr: Assign):
        value = self.evaluate(expr.value)
        self.environment.assign(expr.name.lexeme, value)
        return value

    def visit_Pipe(self, expr: Pipe):
        # Evaluate the head of the pipe
        result = self.evaluate(expr.head)

        # Sequentially call each step in the pipe
        for step_expr in expr.steps:
            callee = self.evaluate(step_expr)
            if not isinstance(callee, Callable):
                # For simplicity, we assume pipe steps are simple identifiers for now
                if isinstance(step_expr, Variable):
                    raise RuntimeError(
                        f"'{step_expr.name.lexeme}' is not a function.", step_expr.name
                    )
                else:
                    raise RuntimeError("Pipe steps must be callable functions.")

            # Check arity
            if callee.arity() != 1:
                if isinstance(step_expr, Variable):
                    raise RuntimeError(
                        f"Function '{step_expr.name.lexeme}' in pipe must accept exactly one argument.",
                        step_expr.name,
                    )
                else:
                    raise RuntimeError(
                        "Functions in a pipe must accept exactly one argument."
                    )

            result = callee.call(self, [result])

        # If there's a target, assign the final result to it
        if expr.target:
            self.environment.define(expr.target.lexeme, result)

        return result

    def visit_State(self, expr: State):
        payload = None
        if expr.payload:
            payload = self.evaluate(expr.payload)

        return {"kind": expr.name.lexeme, "payload": payload}

    def visit_Call(self, expr: Call):
        callee = self.evaluate(expr.callee)

        arguments = []
        for argument in expr.arguments:
            arguments.append(self.evaluate(argument))

        if not isinstance(callee, Callable):
            raise RuntimeError("Can only call functions and classes.", expr.paren)

        if len(arguments) != callee.arity():
            raise RuntimeError(
                f"Expected {callee.arity()} arguments but got {len(arguments)}.",
                expr.paren,
            )

        return callee.call(self, arguments)

    def visit_Binary(self, expr: Binary):
        left = self.evaluate(expr.left)
        right = self.evaluate(expr.right)
        op_type = expr.operator.type

        if op_type == TokenType.PLUS:
            if isinstance(left, str) or isinstance(right, str):
                return str(left) + str(right)
            return left + right
        elif op_type == TokenType.MINUS:
            return left - right
        elif op_type == TokenType.STAR:
            return left * right
        elif op_type == TokenType.SLASH:
            if right == 0:
                raise RuntimeError("Division by zero", expr.operator)
            return left / right
        elif op_type == TokenType.GREATER:
            return left > right
        elif op_type == TokenType.GREATER_EQUAL:
            return left >= right
        elif op_type == TokenType.LESS:
            return left < right
        elif op_type == TokenType.LESS_EQUAL:
            return left <= right
        elif op_type == TokenType.EQUAL_EQUAL:
            return left == right
        elif op_type == TokenType.BANG_EQUAL:
            return left != right
        return None

    def visit_Unary(self, expr: Unary):
        right = self.evaluate(expr.right)
        if expr.operator.type == TokenType.MINUS:
            return -right
        elif expr.operator.type == TokenType.BANG:
            return not self.is_truthy(right)
        return None

    def is_truthy(self, value):
        if value is None:
            return False
        if isinstance(value, bool):
            return value
        return True

    def stringify(self, value):
        if value is None:
            return "nil"
        if isinstance(value, dict) and "kind" in value and "payload" in value:
            return f"@{value['kind']}({self.stringify(value['payload'])})"
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, float):
            text = str(value)
            if text.endswith(".0"):
                text = text[:-2]
            return text
        return str(value)

    def get_output(self) -> str:
        return "\n".join(self.output)
