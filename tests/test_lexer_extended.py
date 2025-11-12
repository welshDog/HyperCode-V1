import pytest
from hypercode.core.lexer import Lexer, Token, TokenType

def test_lexer_escaped_strings():
    """Test handling of strings with escaped characters."""
    source = r'"Hello\nWorld" "It\'s a test" "C:\\path\\to\\file"'
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    assert len(tokens) == 4  # 3 strings + EOF
    assert tokens[0].type == TokenType.STRING
    assert tokens[0].value == '\"Hello\\nWorld\"'
    assert tokens[1].value == '\"It\\\'s a test\"'
    assert tokens[2].value == '\"C:\\\\path\\\\to\\\\file\"'

def test_lexer_numbers():
    """Test various number formats."""
    source = "42 3.14 0.5 .5 1e10 2e-5 0x1A 0b1010 0o755"
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    number_tokens = [t for t in tokens if t.type == TokenType.NUMBER]
    assert len(number_tokens) == 9
    assert [t.value for t in number_tokens] == [
        '42', '3.14', '0.5', '.5', '1e10', '2e-5', '0x1A', '0b1010', '0o755'
    ]

def test_lexer_operators():
    """Test all operators."""
    # Test each operator individually to ensure they're recognized
    operators = [
        ("+", TokenType.PLUS),
        ("-", TokenType.MINUS),
        ("*", TokenType.STAR),
        ("/", TokenType.SLASH),
        ("%", TokenType.PERCENT),
        ("**", TokenType.STAR_STAR),
        ("//", TokenType.SLASH_SLASH),
        ("=", TokenType.EQUAL),
        (">", TokenType.GREATER),
        (">=", TokenType.GREATER_EQUAL),
        ("<", TokenType.LESS),
        ("<=", TokenType.LESS_EQUAL),
        ("==", TokenType.EQUAL_EQUAL),
        ("!=", TokenType.BANG_EQUAL),
    ]
    
    for op_str, expected_type in operators:
        # Skip testing SLASH_SLASH in isolation as it's used for comments
        if expected_type == TokenType.SLASH_SLASH:
            continue
            
        lexer = Lexer(op_str)
        tokens = lexer.tokenize()
        
        # Should have the operator and EOF
        assert len(tokens) == 2, f"Expected 2 tokens for '{op_str}', got {len(tokens)}"
        assert tokens[0].type == expected_type, f"Expected {expected_type} for '{op_str}', got {tokens[0].type}"
        assert tokens[1].type == TokenType.EOF
    
    # Special test for SLASH_SLASH to ensure it's recognized in context
    source = "10 // 3"
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    # Should be: NUMBER(10), WHITESPACE, SLASH_SLASH(//), WHITESPACE, NUMBER(3), EOF
    token_types = [t.type for t in tokens]
    assert TokenType.SLASH_SLASH in token_types, "SLASH_SLASH operator not found in tokens"
    
    # Find the SLASH_SLASH token and verify its value
    slash_slash_tokens = [t for t in tokens if t.type == TokenType.SLASH_SLASH]
    assert len(slash_slash_tokens) == 1, f"Expected exactly one SLASH_SLASH token, got {len(slash_slash_tokens)}"
    assert slash_slash_tokens[0].value == "//", f"Expected '//' as token value, got {slash_slash_tokens[0].value}"

def test_lexer_comments():
    """Test handling of single-line and multi-line comments."""
    source = """
    # This is a comment
    let x = 42  # End of line comment
    /*
    Multi-line
    comment
    */
    let y = 3.14
    """
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    # Get non-whitespace, non-comment tokens
    code_tokens = [
        t for t in tokens 
        if t.type not in (TokenType.WHITESPACE, TokenType.COMMENT, TokenType.EOF)
    ]
    
    # Check the structure of the code
    # We expect 8 tokens: let, x, =, 42, let, y, =, 3.14
    assert len(code_tokens) == 8
    
    # First statement: let x = 42
    assert code_tokens[0].type == TokenType.LET
    assert code_tokens[1].type == TokenType.IDENTIFIER and code_tokens[1].value == 'x'
    assert code_tokens[2].type == TokenType.EQUAL
    assert code_tokens[3].type == TokenType.NUMBER and code_tokens[3].value == '42'
    
    # Second statement: let y = 3.14
    assert code_tokens[4].type == TokenType.LET
    assert code_tokens[5].type == TokenType.IDENTIFIER and code_tokens[5].value == 'y'
    assert code_tokens[6].type == TokenType.EQUAL
    assert code_tokens[7].type == TokenType.NUMBER and code_tokens[7].value == '3.14'

def test_lexer_whitespace():
    """Test handling of various whitespace characters."""
    source = "let\t x\n=\r\n42\f\v"
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    
    assert [t.type for t in tokens] == [
        TokenType.LET, TokenType.IDENTIFIER, TokenType.EQUAL, 
        TokenType.NUMBER, TokenType.EOF
    ]

def test_lexer_error_handling():
    """Test error handling for invalid tokens."""
    source = "let x = @invalid#token"
    lexer = Lexer(source)
    
    with pytest.raises(SyntaxError) as excinfo:
        lexer.tokenize()
    
    assert "Invalid character" in str(excinfo.value)
    assert "line 1, column 9" in str(excinfo.value)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
