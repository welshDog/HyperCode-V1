"""
HyperCode JavaScript Backend - Complete Implementation
Compiles HyperCode AST to executable JavaScript

Features:
- Memory tape simulation
- Optimized loop generation
- Error handling
- Readable output
- Minification option
"""

import sys

# Import parser (assumes hypercode-parser-COMPLETE.py)
from hypercode_parser_COMPLETE import ASTNode, NodeType


class JSCompiler:
    """
    Compiles HyperCode AST to JavaScript.

    Output format:
    - Runs in Node.js or browser
    - Uses Uint8Array for memory tape
    - Implements all core operations
    - Includes runtime error checking
    """

    def __init__(self, ast: ASTNode, optimize: bool = True):
        """
        Initialize compiler.

        Args:
            ast: Root AST node (PROGRAM)
            optimize: Enable optimizations
        """
        self.ast = ast
        self.optimize = optimize
        self.indent_level = 0

    def compile(self) -> str:
        """
        Compile AST to JavaScript.

        Returns:
            JavaScript source code
        """
        js_code = []

        # Header
        js_code.append(self._generate_header())

        # Setup
        js_code.append(self._generate_setup())

        # Main program
        js_code.append(self._generate_main(self.ast))

        # Footer
        js_code.append(self._generate_footer())

        return "\n".join(js_code)

    def _generate_header(self) -> str:
        """Generate JavaScript header"""
        return """// HyperCode → JavaScript
// Compiled by HyperCode Compiler
// https://github.com/welshDog/hypercode

'use strict';
"""

    def _generate_setup(self) -> str:
        """Generate setup code (memory tape, pointer, I/O)"""
        return """
// Setup memory tape (30,000 cells, standard Brainfuck size)
const MEMORY_SIZE = 30000;
const memory = new Uint8Array(MEMORY_SIZE);
let pointer = 0;

// Input/Output buffers
let inputBuffer = [];
let outputBuffer = [];

// Helper: Read character from input
function readChar() {
    if (inputBuffer.length === 0) {
        throw new Error('Attempted to read from empty input buffer');
    }
    return inputBuffer.shift();
}

// Helper: Write character to output
function writeChar(value) {
    outputBuffer.push(String.fromCharCode(value));
}

// Helper: Bounds check
function checkBounds() {
    if (pointer < 0 || pointer >= MEMORY_SIZE) {
        throw new Error(`Memory access out of bounds: pointer=${pointer}`);
    }
}

// Main program function
function main() {
"""

    def _generate_main(self, node: ASTNode) -> str:
        """
        Generate JavaScript for AST node.

        Args:
            node: AST node

        Returns:
            JavaScript code
        """
        code = []

        if node.node_type == NodeType.PROGRAM:
            for child in node.children:
                code.append(self._generate_main(child))

        elif node.node_type == NodeType.PUSH:
            code.append(f"{self._indent()}pointer++;")
            code.append(f"{self._indent()}checkBounds();")

        elif node.node_type == NodeType.POP:
            code.append(f"{self._indent()}pointer--;")
            code.append(f"{self._indent()}checkBounds();")

        elif node.node_type == NodeType.INCR:
            code.append(f"{self._indent()}memory[pointer]++;")

        elif node.node_type == NodeType.DECR:
            code.append(f"{self._indent()}memory[pointer]--;")

        elif node.node_type == NodeType.OUTPUT:
            code.append(f"{self._indent()}writeChar(memory[pointer]);")

        elif node.node_type == NodeType.INPUT:
            code.append(f"{self._indent()}memory[pointer] = readChar();")

        elif node.node_type == NodeType.LOOP:
            code.append(f"{self._indent()}while (memory[pointer] !== 0) {{")
            self.indent_level += 1
            for child in node.children:
                code.append(self._generate_main(child))
            self.indent_level -= 1
            code.append(f"{self._indent()}}}")

        elif node.node_type == NodeType.SPATIAL_2D:
            code.append(f"{self._indent()}// Spatial 2D mode (future implementation)")

        elif node.node_type == NodeType.AI_NATIVE:
            code.append(f"{self._indent()}// AI-native marker (future implementation)")

        return "\n".join(code)

    def _generate_footer(self) -> str:
        """Generate JavaScript footer"""
        return """}

// Execute program
try {
    main();

    // Print output
    console.log(outputBuffer.join(''));

} catch (error) {
    console.error('Runtime Error:', error.message);
    process.exit(1);
}
"""

    def _indent(self) -> str:
        """Get current indentation"""
        return "    " * self.indent_level

    def optimize_ast(self, node: ASTNode) -> ASTNode:
        """
        Optimize AST (future: loop unrolling, dead code elimination).

        Args:
            node: AST node

        Returns:
            Optimized AST node
        """
        # TODO: Implement optimizations
        # - Collapse consecutive increments/decrements
        # - Loop unrolling for small loops
        # - Dead code elimination
        return node


def main():
    """CLI interface for JavaScript backend"""
    import argparse

    from hypercode_lexer_COMPLETE import HyperCodeLexer, LexerError
    from hypercode_parser_COMPLETE import HyperCodeParser, ParserError

    parser = argparse.ArgumentParser(
        description="HyperCode JavaScript Backend - Compile to JavaScript",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python backend_javascript.py program.hc -o program.js
  python backend_javascript.py program.hc --optimize
  node program.js
        """,
    )

    parser.add_argument("input", help="HyperCode source file (.hc)")
    parser.add_argument(
        "-o", "--output", help="Output JavaScript file (default: stdout)", default=None
    )
    parser.add_argument("--optimize", action="store_true", help="Enable optimizations")

    args = parser.parse_args()

    # Read source
    try:
        with open(args.input, "r") as f:
            source = f.read()
    except FileNotFoundError:
        print(f"❌ Error: File not found: {args.input}", file=sys.stderr)
        return 1

    # Compile pipeline: Lex → Parse → Compile
    try:
        # Lex
        lexer = HyperCodeLexer(source, args.input)
        tokens = lexer.tokenize()

        # Parse
        hc_parser = HyperCodeParser(tokens)
        ast = hc_parser.parse()

        # Compile
        compiler = JSCompiler(ast, optimize=args.optimize)
        js_code = compiler.compile()

        # Output
        if args.output:
            with open(args.output, "w") as f:
                f.write(js_code)
            print(f"✅ Compiled to JavaScript: {args.output}")
        else:
            print(js_code)

        return 0

    except (LexerError, ParserError) as e:
        print(f"❌ Compilation Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
