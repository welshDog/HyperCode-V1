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
Test harness for core HyperCode components.
"""

import sys
from pathlib import Path

# Add project root to the Python path to allow imports from core, backends, etc.
sys.path.append(str(Path(__file__).parent.parent))

from hypercode.core.interpreter import Interpreter
from hypercode.core.lexer import Lexer
from hypercode.core.parser import Parser


def run_test(source_code: str):
    """Test the lexer, parser, and interpreter with the given source code."""
    print(f"Testing source:\n---\n{source_code}\n---")

    try:
        # Test Lexer
        lexer = Lexer(source_code)
        tokens = lexer.scan_tokens()
        print("\nTokens:")
        for token in tokens:
            print(f"  {token}")

        # Test Parser
        parser = Parser(tokens)
        statements = parser.parse()
        print("\nAST:")
        print(statements)

        # Test Interpreter
        print("\nInterpreter Output:")
        interpreter = Interpreter()
        interpreter.interpret(statements)

        print("\n✅ Core components test passed!")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")


if __name__ == "__main__":
    # Use a simple test case that the current parser can handle
    test_code = """
    fun fib(n) {
        if (n < 2) {
            return n;
        }
        return fib(n - 2) + fib(n - 1);
    }

    var result = fib(10);
    print(result);
    """
    run_test(test_code)
