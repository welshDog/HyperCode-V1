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

from hypercode.core.lexer import Lexer
from hypercode.core.parser import Parser


def run_test(source_code: str):
    """Test the lexer and parser with the given source code."""
    print(f"Testing source:\n---\n{source_code}\n---")

    try:
        # Test Lexer
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        print("\nTokens:")
        for token in tokens:
            print(f"  {token}")

        # Test Parser
        parser = Parser(tokens)
        ast = parser.parse()
        print("\nAST:")
        print(ast)
        print("\n✅ Core components test passed!")

    except Exception as e:
        print(f"\n❌ Test failed: {e}")


if __name__ == "__main__":
    # Use a simple test case that the current parser can handle
    test_code = """
    let x = 42;
    const y = \"hello\";
    """
    run_test(test_code)
