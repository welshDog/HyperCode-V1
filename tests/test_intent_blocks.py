#!/usr/bin/env python3
"""Test script for Intent Blocks implementation"""

import sys

sys.path.append("src")

from hypercode.core.ast import Intent
from hypercode.core.lexer import Lexer
from hypercode.core.parser import Parser


def test_intent_block():
    """Test parsing of intent blocks"""
    code = """
    intent "Authenticate user with GitHub credentials" {
        var token = "github_token";
        var user = fetch_user(token);
        print("User authenticated: " + user.name);
    }
    """

    print("Testing Intent Block parsing...")
    print("Input code:")
    print(code)

    # Lex the code
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    print("\nTokens:")
    for token in tokens:
        print(f"  {token}")

    # Parse the tokens
    parser = Parser(tokens)
    statements = parser.parse()

    print("\nParsed statements:")
    for stmt in statements:
        print(f"  {type(stmt).__name__}: {stmt}")
        if isinstance(stmt, Intent):
            print(f"    Description: {stmt.description}")
            print(f"    Statements: {len(stmt.statements)}")

    # Verify we got an Intent statement
    assert len(statements) == 1, f"Expected 1 statement, got {len(statements)}"
    assert isinstance(
        statements[0], Intent
    ), f"Expected Intent statement, got {type(statements[0])}"
    assert statements[0].description == "Authenticate user with GitHub credentials"
    assert len(statements[0].statements) == 3

    print("\n✅ Intent Block parsing test passed!")


if __name__ == "__main__":
    test_intent_block()
