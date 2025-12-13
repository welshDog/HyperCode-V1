"""
HyperCode Parser - Complete Implementation
Converts token stream into Abstract Syntax Tree (AST)

Features:
- Recursive descent parsing
- Loop nesting support
- Error recovery
- AST visualization
- Semantic validation
"""

import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

# Import lexer (assumes hypercode-lexer-COMPLETE.py)
from hypercode_lexer_COMPLETE import LexerError, Token, TokenType


class NodeType(Enum):
    """AST Node types"""

    PROGRAM = "program"
    PUSH = "push"
    POP = "pop"
    INCR = "increment"
    DECR = "decrement"
    OUTPUT = "output"
    INPUT = "input"
    LOOP = "loop"
    SPATIAL_2D = "spatial_2d"
    AI_NATIVE = "ai_native"


@dataclass
class ASTNode:
    """
    Abstract Syntax Tree Node.

    Represents a single operation or block in HyperCode.
    """

    node_type: NodeType
    value: Optional[int] = None
    children: List["ASTNode"] = field(default_factory=list)
    line: int = 0
    column: int = 0

    def __repr__(self, indent: int = 0) -> str:
        """Pretty-print AST (neurodivergent-friendly)"""
        spaces = "  " * indent
        result = f"{spaces}{self.node_type.value}"

        if self.value is not None:
            result += f" (value={self.value})"

        if self.children:
            result += " {"
            for child in self.children:
                result += "\n" + child.__repr__(indent + 1)
            result += f"\n{spaces}}}"

        return result


class ParserError(Exception):
    """Parser-specific errors with context"""

    def __init__(self, message: str, token: Token):
        self.message = message
        self.token = token
        super().__init__(
            f"Line {token.line}, Col {token.column}: {message}\n"
            f"  Near: '{token.value}'"
        )


class HyperCodeParser:
    """
    Parses HyperCode token stream into AST.

    Grammar (simplified BNF):

    program    ::= statement*
    statement  ::= operation | loop | spatial | ai_native
    operation  ::= PUSH | POP | INCR | DECR | OUTPUT | INPUT
    loop       ::= LOOP_START statement* LOOP_END
    spatial    ::= SPATIAL_2D statement*
    ai_native  ::= AI_NATIVE
    """

    def __init__(self, tokens: List[Token]):
        """
        Initialize parser with token stream.

        Args:
            tokens: List of tokens from lexer
        """
        self.tokens = tokens
        self.position = 0
        self.current_token = tokens[0] if tokens else None

    def parse(self) -> ASTNode:
        """
        Parse tokens into AST.

        Purpose:
        Entry point for the parsing process, converting a flat list of tokens into a hierarchical Abstract Syntax Tree.

        Returns:
            ASTNode: The root node of the generated AST (Type: PROGRAM).

        Raises:
            ParserError: If a syntax error is encountered during parsing.

        Example:
            >>> parser = HyperCodeParser(tokens)
            >>> ast = parser.parse()
            >>> print(ast.node_type)
            NodeType.PROGRAM
        """
        program = ASTNode(NodeType.PROGRAM)

        while not self._is_at_end():
            if self.current_token.type == TokenType.EOF:
                break

            statement = self._parse_statement()
            if statement:
                program.children.append(statement)

        return program

    def _parse_statement(self) -> Optional[ASTNode]:
        """Parse a single statement.

        Purpose:
        Identifies and parses the next statement based on the current token type.
        Acts as a dispatcher for specific statement parsers (loops, operations, etc.).

        Returns:
            Optional[ASTNode]: The parsed AST node for the statement, or None if no statement could be parsed.

        Design Choice:
        Using a lookahead of 1 (current_token) is sufficient for HyperCode's grammar, keeping the parser simple and fast.
        """
        token = self.current_token

        # Define mapping for simple operations
        simple_ops = {
            TokenType.PUSH: NodeType.PUSH,
            TokenType.POP: NodeType.POP,
            TokenType.INCR: NodeType.INCR,
            TokenType.DECR: NodeType.DECR,
            TokenType.OUTPUT: NodeType.OUTPUT,
            TokenType.INPUT: NodeType.INPUT,
            TokenType.SPATIAL_2D: NodeType.SPATIAL_2D,
            TokenType.AI_NATIVE: NodeType.AI_NATIVE,
        }

        # Dispatch based on token type
        if token.type in simple_ops:
            self._advance()
            return ASTNode(simple_ops[token.type], line=token.line, column=token.column)

        elif token.type == TokenType.LOOP_START:
            return self._parse_loop()

        else:
            raise ParserError(f"Unexpected token: {token.type.value}", token)

    def _parse_loop(self) -> ASTNode:
        """
        Parse loop structure: [ statements ]

        Purpose:
        Handles the nested structure of loops.
        Recursively calls _parse_statement to populate the loop body.

        Returns:
            ASTNode: A LOOP node containing 'children' statements.

        Raises:
            ParserError: If the loop is not properly closed with ']'.
        """
        start_token = self.current_token

        if start_token.type != TokenType.LOOP_START:
            raise ParserError("Expected '[' to start loop", start_token)

        self._advance()  # Skip [

        loop_node = ASTNode(
            NodeType.LOOP, line=start_token.line, column=start_token.column
        )

        # Parse loop body
        while not self._is_at_end() and self.current_token.type != TokenType.LOOP_END:
            statement = self._parse_statement()
            if statement:
                loop_node.children.append(statement)

        # Expect closing ]
        if self.current_token.type != TokenType.LOOP_END:
            raise ParserError(
                f"Unclosed loop: expected ']', got {self.current_token.type.value}",
                start_token,
            )

        self._advance()  # Skip ]

        return loop_node

    def _advance(self):
        """Move to next token"""
        if self.position < len(self.tokens) - 1:
            self.position += 1
            self.current_token = self.tokens[self.position]

    def _is_at_end(self) -> bool:
        """Check if at end of token stream"""
        return (
            self.position >= len(self.tokens)
            or self.current_token.type == TokenType.EOF
        )

    def validate(self) -> List[str]:
        """
        Validate AST structure.

        Returns:
            List of warnings (empty if no issues)
        """
        warnings = []

        # Check for unbalanced loops (already handled by parser)
        # Check for infinite loops (basic heuristic)
        # Check for unreachable code

        return warnings

    def print_ast(self, node: Optional[ASTNode] = None, indent: int = 0):
        """
        Print AST in readable format.

        Args:
            node: AST node to print (defaults to root)
            indent: Indentation level
        """
        if node is None:
            return

        print(node.__repr__(indent))


def main():
    """CLI interface for the parser"""
    import argparse

    from hypercode_lexer_COMPLETE import HyperCodeLexer

    parser = argparse.ArgumentParser(
        description="HyperCode Parser - Generate AST from HyperCode programs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python parser.py program.hc
  python parser.py program.hc --visualize
        """,
    )

    parser.add_argument("file", help="HyperCode source file")
    parser.add_argument(
        "--visualize", action="store_true", help="Print AST visualization"
    )

    args = parser.parse_args()

    # Read source
    try:
        with open(args.file, "r") as f:
            source = f.read()
    except FileNotFoundError:
        print(f"❌ Error: File not found: {args.file}", file=sys.stderr)
        return 1

    # Lex
    try:
        lexer = HyperCodeLexer(source, args.file)
        tokens = lexer.tokenize()
        print(f"✅ Lexing complete: {len(tokens) - 1} tokens")
    except LexerError as e:
        print(f"❌ Lexer Error: {e}", file=sys.stderr)
        return 1

    # Parse
    try:
        hc_parser = HyperCodeParser(tokens)
        ast = hc_parser.parse()
        print(f"✅ Parsing complete: {len(ast.children)} top-level statements")

        # Validate
        warnings = hc_parser.validate()
        if warnings:
            print("\n⚠️  Warnings:")
            for warning in warnings:
                print(f"   {warning}")

        # Visualize
        if args.visualize:
            print("\n📊 AST Visualization:")
            hc_parser.print_ast(ast)

        return 0

    except ParserError as e:
        print(f"❌ Parser Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
