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
Build script for the HyperCode language.

This script provides a command-line interface to compile HyperCode source files
to a specified target language (currently, only Python is supported).
"""

import argparse
import sys
from pathlib import Path

# Add project root to the Python path to allow imports from core, backends, etc.
sys.path.append(str(Path(__file__).parent))

from backends.python import PythonBackend
from core.parser import Parser
from hypercode.core.lexer import Lexer


def build(source_file: str, target: str = "python"):
    """
    Builds a HyperCode source file to the target language.

    Args:
        source_file: The path to the HyperCode source file (.hc).
        target: The target language for compilation.
    """
    print(f"Building {source_file} for target '{target}'...")

    source_path = Path(source_file)
    if not source_path.exists():
        print(f"Error: Source file not found at '{source_file}'")
        sys.exit(1)

    source_code = source_path.read_text()

    # 1. Lexing
    lexer = Lexer()
    tokens = lexer.tokenize(source_code)
    print(f"Generated {len(tokens)} tokens.")

    # 2. Parsing
    parser = Parser(tokens)
    ast = parser.parse_program()
    print("Successfully generated AST.")

    # 3. Code Generation
    if target == "python":
        backend = PythonBackend()
    else:
        print(f"Error: Target '{target}' is not supported.")
        sys.exit(1)

    output_code = backend.visit(ast)
    print("Successfully generated target code.")

    # 4. Output
    output_filename = source_path.stem + ".py"
    output_path = source_path.parent / output_filename
    output_path.write_text(output_code)

    print("\n--- Generated Python Code ---\n")
    print(output_code)
    print("\n--- End Generated Code ---\n")
    print(f"✅ Successfully compiled to '{output_path}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Build HyperCode source files.")
    parser.add_argument(
        "source_file", help="The path to the HyperCode source file (.hc)."
    )
    parser.add_argument(
        "--target",
        default="python",
        help="The target language for compilation (default: python).",
    )
    args = parser.parse_args()

    build(args.source_file, args.target)
