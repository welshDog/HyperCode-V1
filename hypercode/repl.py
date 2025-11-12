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
REPL (Read-Eval-Print Loop) for the HyperCode language.
"""

import sys
from pathlib import Path
import argparse

# Add project root to the Python path
sys.path.append(str(Path(__file__).parent.parent))

from hypercode.core.lexer import Lexer
from core.parser import Parser
from backends.python import PythonBackend

class HyperCodeREPL:
    def __init__(self, debug=False):
        self.debug = debug
        self.lexer = Lexer()
        self.backend = PythonBackend()
        self.exec_context = {}

    def _print_debug_info(self, source, tokens, ast, python_code):
        """Print detailed debug information."""
        print("\n=== Debug Mode ===")
        print("--- Source ---")
        print(source)
        print("\n--- Tokens ---")
        for token in tokens:
            print(f"  {token}")
        print("\n--- AST ---")
        print(ast)
        print("\n--- Python Code ---")
        print(python_code)
        print("=================\n")

    def start(self):
        """Starts the HyperCode Read-Eval-Print Loop."""
        print("HyperCode REPL (type 'exit' to quit)")
        while True:
            try:
                source = input("hc> ").strip()
                if source.lower() in ('exit', 'quit'):
                    break
                if not source:
                    continue

                # Lexing
                tokens = self.lexer.tokenize(source)

                # Parsing
                if tokens and tokens[-1].type != 'SEMICOLON':
                    last_token = tokens[-1]
                    tokens.append(type(last_token)('SEMICOLON', ';', last_token.line, last_token.column + 1))
                
                parser = Parser(tokens)
                ast = parser.parse_program()

                # Code Generation
                python_code = self.backend.visit(ast)

                if self.debug:
                    self._print_debug_info(source, tokens, ast, python_code)

                # Execution
                exec(python_code, self.exec_context)

            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                print(f"Error: {e}")

def main():
    """Main entry point for the REPL."""
    parser = argparse.ArgumentParser(description='HyperCode REPL')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode')
    args = parser.parse_args()
    
    repl = HyperCodeREPL(debug=args.debug)
    repl.start()

if __name__ == "__main__":
    main()
