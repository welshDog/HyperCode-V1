# Copyright 2025 welshDog (Lyndz Williams)
#
# Licensed under the MIT License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Abstract Syntax Tree (AST) nodes for the HyperCode language.
"""

from dataclasses import dataclass
from typing import List, Optional


# Base class for all AST nodes
class Node:
    """Base class for all AST nodes."""

    pass


@dataclass
class Expression(Node):
    """Base class for all expression nodes."""

    pass


@dataclass
class Statement(Node):
    """Base class for all statement nodes."""

    pass


@dataclass
class Program(Node):
    """Represents the entire program as a list of statements."""

    statements: List[Statement]


@dataclass
class Identifier(Expression):
    """Represents an identifier (e.g., a variable name)."""

    name: str


@dataclass
class Literal(Expression):
    """Represents a literal value (e.g., number, string)."""

    value: any


@dataclass
class VariableDeclaration(Statement):
    """Represents a variable declaration (let or const)."""

    name: Identifier
    value: Optional[Expression]
    is_const: bool


@dataclass
class BinaryOperation(Expression):
    """Represents a binary operation (e.g., a + b)."""

    left: Expression
    operator: str
    right: Expression
