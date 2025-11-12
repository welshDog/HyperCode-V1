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

# Add project root to the Python path
sys.path.append(str(Path(__file__).parent.parent))

from hypercode.core.lexer import Lexer
from core.parser import Parser
from backends.python import PythonBackend

def start_repl():
    """Starts the HyperCode Read-Eval-Print Loop."""
    print("HyperCode REPL (type 'exit' to quit)")
    
    lexer = Lexer()
    backend = PythonBackend()
    
    # The context in which the generated Python code will be executed
    exec_context = {}

    while True:
        try:
            source = input("hc> ")
            if source.lower() in ('exit', 'quit'):
                break
            if not source.strip():
                continue

            # 1. Lexing
            tokens = lexer.tokenize(source)
            
            # 2. Parsing
            # The parser expects a semicolon at the end of statements.
            # For the REPL, we can be more lenient and add it if it's missing.
            if tokens and tokens[-1].type != 'SEMICOLON':
                last_token = tokens[-1]
                tokens.append(type(last_token)('SEMICOLON', ';', last_token.line, last_token.column + 1))

            parser = Parser(tokens)
            ast = parser.parse_program()

            # 3. Code Generation
            python_code = backend.visit(ast)

            # 4. Evaluation
            # The `exec` function executes the code in the given context.
            # We can inspect the `exec_context` to see variables.
            exec(python_code, exec_context)
            
            # For simplicity, we don't print results yet, but the context is updated.
            # A more advanced REPL would parse expressions and print their values.

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start_repl()
