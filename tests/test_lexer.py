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
Comprehensive test suite for the HyperCode lexer

File: tests\test_lexer.py
"""

import unittest
from pathlib import Path
import sys

# Add the project root to the Python path
sys.path.append(str(Path(__file__).parent.parent))

from hypercode.core.lexer import Lexer, Token

class TestLexer(unittest.TestCase):
    """Test cases for the HyperCode lexer"""
    
    def setUp(self):
        """Set up a new lexer for each test."""
        self.lexer = Lexer()
    
    def assert_tokens_match(self, source, expected_tokens):
        """Helper method to assert that tokens match expected output."""
        tokens = self.lexer.tokenize(source)
        token_types = [(t.type, t.value) for t in tokens]
        self.assertEqual(token_types, expected_tokens)
    
    def test_empty_string(self):
        """Test that an empty string produces no tokens."""
        self.assert_tokens_match("", [])
    
    def test_whitespace(self):
        """Test that whitespace is ignored."""
        self.assert_tokens_match("  \t\n  ", [])
    
    def test_comments(self):
        """Test that comments are ignored."""
        self.assert_tokens_match("// This is a comment\nlet x = 5", [
            ('LET', 'let'),
            ('IDENTIFIER', 'x'),
            ('ASSIGN', '='),
            ('NUMBER', '5')
        ])
    
    def test_keywords(self):
        """Test that keywords are properly tokenized."""
        self.assert_tokens_match("if else for while function return let const true false null", [
            ('IF', 'if'),
            ('ELSE', 'else'),
            ('FOR', 'for'),
            ('WHILE', 'while'),
            ('FUNCTION', 'function'),
            ('RETURN', 'return'),
            ('LET', 'let'),
            ('CONST', 'const'),
            ('TRUE', 'true'),
            ('FALSE', 'false'),
            ('NULL', 'null')
        ])
    
    def test_operators(self):
        """Test that operators are properly tokenized."""
        self.assert_tokens_match("+-*/= == != < > <= >=", [
            ('PLUS', '+'),
            ('MINUS', '-'),
            ('MULTIPLY', '*'),
            ('DIVIDE', '/'),
            ('ASSIGN', '='),
            ('EQUALS', '=='),
            ('NOT_EQUALS', '!='),
            ('LESS', '<'),
            ('GREATER', '>'),
            ('LESS_EQUAL', '<='),
            ('GREATER_EQUAL', '>=')
        ])
    
    def test_numbers(self):
        """Test that numbers are properly tokenized."""
        self.assert_tokens_match("123 45.67 0.5 .5", [
            ('NUMBER', '123'),
            ('NUMBER', '45.67'),
            ('NUMBER', '0.5'),
            ('NUMBER', '.5')
        ])
    
    def test_strings(self):
        """Test that strings are properly tokenized."""
        self.assert_tokens_match('"hello" \'world\' "escaped \"quote\""', [
            ('STRING', '"hello"'),
            ('STRING', "'world'"),
            ('STRING', '"escaped \"quote\""')
        ])
    
    def test_identifiers(self):
        """Test that identifiers are properly tokenized."""
        self.assert_tokens_match("variable_name _private CONSTANT123", [
            ('IDENTIFIER', 'variable_name'),
            ('IDENTIFIER', '_private'),
            ('IDENTIFIER', 'CONSTANT123')
        ])
    
    def test_punctuation(self):
        """Test that punctuation is properly tokenized."""
        self.assert_tokens_match("(){}[],;:.", [
            ('LPAREN', '('),
            ('RPAREN', ')'),
            ('LBRACE', '{'),
            ('RBRACE', '}'),
            ('LBRACKET', '['),
            ('RBRACKET', ']'),
            ('COMMA', ','),
            ('SEMICOLON', ';'),
            ('COLON', ':'),
            ('DOT', '.')
        ])
    
    def test_unknown_characters(self):
        """Test that unknown characters are properly handled."""
        tokens = self.lexer.tokenize("let x = @#$")
        self.assertEqual(tokens[0].type, 'LET')
        self.assertEqual(tokens[1].type, 'IDENTIFIER')
        self.assertEqual(tokens[2].type, 'ASSIGN')
        self.assertEqual(tokens[3].type, 'UNKNOWN')
        self.assertEqual(tokens[3].value, '@')
        self.assertEqual(tokens[4].type, 'UNKNOWN')
        self.assertEqual(tokens[4].value, '#')
        self.assertEqual(tokens[5].type, 'UNKNOWN')
        self.assertEqual(tokens[5].value, '$')
    
    def test_line_numbers(self):
        """Test that line numbers are tracked correctly."""
        source = """let x = 5
let y = 10
let z = x + y"""
        tokens = self.lexer.tokenize(source)
        
        # First line
        self.assertEqual(tokens[0].line, 1)
        self.assertEqual(tokens[0].type, 'LET')
        
        # Second line
        self.assertEqual(tokens[4].line, 2)
        self.assertEqual(tokens[4].type, 'LET')
        
        # Third line
        self.assertEqual(tokens[8].line, 3)
        self.assertEqual(tokens[8].type, 'LET')

if __name__ == '__main__':
    unittest.main()
