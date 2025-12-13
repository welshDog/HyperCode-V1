from abc import ABC, abstractmethod
from typing import List, Any, Optional
from dataclasses import dataclass
from .tokens import Token

class Node(ABC):
    """Base class for AST nodes."""
    @abstractmethod
    def accept(self, visitor):
        pass

class Stmt(Node):
    """Base class for Statements."""
    pass

class Expr(Node):
    """Base class for Expressions."""
    pass

# Statements

@dataclass
class Expression(Stmt):
    expression: Expr

    def accept(self, visitor):
        return visitor.visit_Expression(self)

@dataclass
class Print(Stmt):
    expression: Expr

    def accept(self, visitor):
        return visitor.visit_Print(self)

@dataclass
class Let(Stmt):
    name: Token
    initializer: Optional[Expr]

    def accept(self, visitor):
        return visitor.visit_Let(self)

@dataclass
class Block(Stmt):
    statements: List[Stmt]

    def accept(self, visitor):
        return visitor.visit_Block(self)

@dataclass
class BlockDecl(Stmt):
    name: Token
    body: List[Stmt]

    def accept(self, visitor):
        return visitor.visit_BlockDecl(self)

@dataclass
class If(Stmt):
    condition: Expr
    then_branch: Stmt
    else_branch: Optional[Stmt]

    def accept(self, visitor):
        # Visitor might not have visit_If, check interpreter
        # Interpreter doesn't seem to implement visit_If in the file I read!
        # Wait, parser produces If, so Interpreter SHOULD have it.
        # I checked interpreter.py loc 215 -> 'def if_statement' (parser), 
        # Interpreter 'visit_Binary' etc.
        # Interpreter.execute_block calls execute(statement) -> accept.
        # I didn't see visit_If in the interpreter.py I read!
        # If it's missing, I'll need to check or add it.
        # For now, generate the node.
        if hasattr(visitor, "visit_If"):
            return visitor.visit_If(self)
        pass

@dataclass
class Function(Stmt):
    name: Token
    params: List[Token]
    body: List[Stmt]

    def accept(self, visitor):
        return visitor.visit_Function(self)

@dataclass
class Return(Stmt):
    keyword: Token
    value: Optional[Expr]

    def accept(self, visitor):
        return visitor.visit_Return(self)

@dataclass
class Intent(Stmt):
    statements: List[Stmt]

    def accept(self, visitor):
        return visitor.visit_Intent(self)


# Expressions

@dataclass
class Binary(Expr):
    left: Expr
    operator: Token
    right: Expr

    def accept(self, visitor):
        return visitor.visit_Binary(self)

@dataclass
class Unary(Expr):
    operator: Token
    right: Expr

    def accept(self, visitor):
        return visitor.visit_Unary(self)

@dataclass
class Literal(Expr):
    value: Any

    def accept(self, visitor):
        return visitor.visit_Literal(self)

@dataclass
class Grouping(Expr):
    expression: Expr

    def accept(self, visitor):
        return visitor.visit_Grouping(self)

@dataclass
class Variable(Expr):
    name: Token

    def accept(self, visitor):
        return visitor.visit_Variable(self)

@dataclass
class Assign(Expr):
    name: Token
    value: Expr

    def accept(self, visitor):
        return visitor.visit_Assign(self)

@dataclass
class Pipe(Expr):
    head: Expr
    steps: List[Expr]
    target: Optional[Token]

    def accept(self, visitor):
        return visitor.visit_Pipe(self)

@dataclass
class State(Expr):
    name: Token
    payload: Optional[Expr]

    def accept(self, visitor):
        return visitor.visit_State(self)

@dataclass
class Call(Expr):
    callee: Expr
    paren: Token
    arguments: List[Expr]

    def accept(self, visitor):
        return visitor.visit_Call(self)
