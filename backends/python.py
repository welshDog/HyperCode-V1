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
Python backend for the HyperCode compiler.

This module translates the HyperCode AST into Python code.
"""

from core import ast

class NodeVisitor:
    """
    Base class for visiting AST nodes.
    
    Implements the visitor pattern to traverse the AST.
    """
    def visit(self, node):
        """Dispatch to the appropriate visitor method."""
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        """Default visitor for unhandled nodes."""
        raise NotImplementedError(f"No visit_{type(node).__name__} method")

class PythonBackend(NodeVisitor):
    """
    Generates Python code from a HyperCode AST.
    """
    def visit_Program(self, node: ast.Program) -> str:
        """Generate code for the entire program."""
        return '\n'.join(self.visit(stmt) for stmt in node.statements)

    def visit_VariableDeclaration(self, node: ast.VariableDeclaration) -> str:
        """Generate code for a variable declaration."""
        # In Python, there's no direct equivalent for 'const'.
        # We could enforce this with runtime checks or static analysis,
        # but for a direct translation, we'll treat them the same.
        if node.value:
            return f"{self.visit(node.name)} = {self.visit(node.value)}"
        return f"{self.visit(node.name)} = None"

    def visit_Identifier(self, node: ast.Identifier) -> str:
        """Generate code for an identifier."""
        return node.name

    def visit_Literal(self, node: ast.Literal) -> str:
        """Generate code for a literal value."""
        if isinstance(node.value, str):
            return f'"{node.value}"'
        return str(node.value)

    def visit_BinaryOperation(self, node: ast.BinaryOperation) -> str:
        """Generate code for a binary operation."""
        left = self.visit(node.left)
        right = self.visit(node.right)
        return f"({left} {node.operator} {right})"
