import sys
import os
import pytest

# Add source directory to path to find the renamed module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from hypercode_lexer_COMPLETE import HyperCodeLexer, TokenType, LexerError

class TestHyperCodeLexer:
    """Tests for the Core HyperCode Lexer (hypercode_lexer_COMPLETE.py)"""

    def test_empty_input(self):
        """1. Empty input should result in single EOF token"""
        lexer = HyperCodeLexer("")
        tokens = lexer.tokenize()
        assert len(tokens) == 1
        assert tokens[0].type == TokenType.EOF

    def test_whitespace_only(self):
        """2. Whitespace should be ignored"""
        lexer = HyperCodeLexer(" \t\n   ")
        tokens = lexer.tokenize()
        assert len(tokens) == 1
        assert tokens[0].type == TokenType.EOF
        # Check line tracking
        assert tokens[0].line > 1

    def test_core_ops(self):
        """3. All core ops should tokenize correctly"""
        code = "> < + - . , [ ]"
        lexer = HyperCodeLexer(code)
        tokens = lexer.tokenize()
        # 8 ops + EOF
        assert len(tokens) == 9
        types = [t.type for t in tokens[:-1]]
        assert types == [
            TokenType.PUSH, TokenType.POP, 
            TokenType.INCR, TokenType.DECR,
            TokenType.OUTPUT, TokenType.INPUT,
            TokenType.LOOP_START, TokenType.LOOP_END
        ]

    def test_spatial_mode(self):
        """4. Spatial mode marker @"""
        lexer = HyperCodeLexer("@")
        tokens = lexer.tokenize()
        assert len(tokens) == 2
        assert tokens[0].type == TokenType.SPATIAL_2D

    def test_ai_native(self):
        """5. AI Native marker #"""
        lexer = HyperCodeLexer("#")
        tokens = lexer.tokenize()
        assert len(tokens) == 2
        assert tokens[0].type == TokenType.AI_NATIVE

    def test_comments(self):
        """6. Comments should be skipped entirely"""
        code = "; this is a comment\n+"
        lexer = HyperCodeLexer(code)
        tokens = lexer.tokenize()
        # Should be INCR, EOF (Comment is skipped, newline is whitespace)
        assert len(tokens) == 2
        assert tokens[0].type == TokenType.INCR

    def test_invalid_character(self):
        """7. Invalid characters should raise LexerError"""
        lexer = HyperCodeLexer("$")
        with pytest.raises(LexerError) as exc:
            lexer.tokenize()
        assert "Unexpected character: '$'" in str(exc.value)

    def test_large_input_stress(self):
        """8. Stress test with large input"""
        code = "+" * 1000
        lexer = HyperCodeLexer(code)
        tokens = lexer.tokenize()
        assert len(tokens) == 1001 # 1000 INCR + EOF
        assert all(t.type == TokenType.INCR for t in tokens[:-1])

    def test_consecutive_semantics(self):
        """9. Consecutive special markers"""
        code = "@@##"
        lexer = HyperCodeLexer(code)
        tokens = lexer.tokenize()
        assert len(tokens) == 5
        assert tokens[0].type == TokenType.SPATIAL_2D
        assert tokens[1].type == TokenType.SPATIAL_2D
        assert tokens[2].type == TokenType.AI_NATIVE
        assert tokens[3].type == TokenType.AI_NATIVE

    def test_unicode_in_comments(self):
        """10. Unicode inside comments should be parsing safe"""
        code = "; 🔍 Verifying...\n>"
        lexer = HyperCodeLexer(code)
        tokens = lexer.tokenize()
        # Should find PUSH after comment
        assert len(tokens) == 2
        assert tokens[0].type == TokenType.PUSH
