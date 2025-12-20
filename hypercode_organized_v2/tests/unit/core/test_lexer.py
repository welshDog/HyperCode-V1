"""
Test script for the HyperCode lexer.

This script demonstrates basic usage of the HyperCode lexer.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from hypercode.core import tokenize

def test_lexer():
    """Test the lexer with sample HyperCode source code."""
    # Sample HyperCode source code
    source = """
    # This is a comment
    let x = 42
    let name = "HyperCode"
    
    if x > 10 then
        print("x is greater than 10")
    else
        print("x is 10 or less")
    
    function greet(name)
        return "Hello, " + name
    end
    
    let result = greet(name)
    print(result)
    """
    
    print("Testing HyperCode lexer...\n")
    print("Source code:")
    print("-" * 40)
    print(source)
    print("-" * 40)
    print("\nTokens:")
    print("-" * 40)
    
    try:
        # Tokenize the source code
        tokens = tokenize(source)
        
        # Print each token
        for token in tokens:
            print(f"{token.type.name:15} | {token.lexeme!r:20} | Line: {token.line:3}, Col: {token.column:3}")
            
        print("\nLexer test completed successfully!")
        return True
    except Exception as e:
        print(f"\nError during lexing: {e}")
        return False

if __name__ == "__main__":
    test_lexer()
