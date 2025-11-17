from dataclasses import dataclass
from typing import TYPE_CHECKING, List, Optional, Union

if TYPE_CHECKING:
    from .tokens import Token


# Base Node class
class Node:
    def accept(self, visitor):
        method_name = f"visit_{self.__class__.__name__}"
        visitor_method = getattr(visitor, method_name, None)
        if visitor_method is None:
            raise NotImplementedError(f"No visit_{self.__class__.__name__} method")
        return visitor_method(self)


# Expressions
@dataclass
class Expr(Node):
    pass


@dataclass
class Literal(Expr):
    value: Union[str, int, float, bool, None]


@dataclass
class Variable(Expr):
    name: "Token"


@dataclass
class Assign(Expr):
    name: "Token"
    value: Expr


@dataclass
class Binary(Expr):
    left: Expr
    operator: "Token"
    right: Expr


@dataclass
class Unary(Expr):
    operator: "Token"
    right: Expr


@dataclass
class Grouping(Expr):
    expression: Expr


# Statements
@dataclass
class Stmt(Node):
    pass


@dataclass
class Expression(Stmt):
    expression: Expr


@dataclass
class Print(Stmt):
    expression: Expr


@dataclass
class Var(Stmt):
    name: "Token"
    initializer: Optional[Expr]


@dataclass
class Block(Stmt):
    statements: List[Stmt]


# Program
@dataclass
class Program(Node):
    statements: List[Stmt]
