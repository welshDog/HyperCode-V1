# src/hypercode/core/ast.py
from dataclasses import dataclass
from typing import Any, List, Optional, Union

# Base classes
class Node:
    pass

class Statement(Node):
    pass

class Expression(Node):
    pass

# Expression nodes
@dataclass
class Literal(Expression):
    value: Any

@dataclass
class Var(Expression):
    name: str

@dataclass
class Binary(Expression):
    left: Expression
    operator: Any  # Token
    right: Expression

@dataclass
class Unary(Expression):
    operator: Any  # Token
    right: Expression

@dataclass
class Grouping(Expression):
    expression: Expression

@dataclass
class Call(Expression):
    callee: Expression
    arguments: List[Expression]

# Intent node
@dataclass
class Intent(Statement):
    """Represents an intent declaration in HyperCode."""
    name: str
    parameters: List[Expression]
    body: List[Statement]

# Statement nodes
@dataclass
class ExpressionStmt(Statement):
    expression: Expression

@dataclass
class VarDecl(Statement):
    name: str
    initializer: Optional[Expression] = None

# Program node
@dataclass
class Program:
    statements: List[Statement]
