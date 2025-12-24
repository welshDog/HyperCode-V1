import pytest

from hypercode.core.lexer import Lexer, TokenType


def test_lexer_escaped_strings():
    """Test handling of strings with escaped characters."""
    source = r'"Hello\nWorld" "It\'s a test" "C:\\path\\to\\file"'
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    assert len(tokens) == 4  # 3 strings + EOF
    assert tokens[0].type == TokenType.STRING
    assert tokens[0].lexeme == '"Hello\\nWorld"'
    assert tokens[1].lexeme == '"It\\\'s a test"'
    assert tokens[2].lexeme == '"C:\\\\path\\\\to\\\\file"'


def test_lexer_numbers():
    """Test various number formats."""
    source = "42 3.14 0.5 .5 1e10 2e-5 0x1A 0b1010 0o755"
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    number_tokens = [t for t in tokens if t.type == TokenType.NUMBER]
    assert len(number_tokens) == 9
    assert [t.lexeme for t in number_tokens] == [
        "42",
        "3.14",
        "0.5",
        ".5",
        "1e10",
        "2e-5",
        "0x1A",
        "0b1010",
        "0o755",
    ]


def test_lexer_operators():
    """Test all operators."""
    # Test each operator individually to ensure they're recognized
    operators = [
        ("+", TokenType.PLUS),
        ("-", TokenType.MINUS),
        ("*", TokenType.STAR),
        ("/", TokenType.SLASH),
        ("=", TokenType.EQUAL),
        (">", TokenType.GREATER),
        (">=", TokenType.GREATER_EQUAL),
        ("<", TokenType.LESS),
        ("<=", TokenType.LESS_EQUAL),
        ("==", TokenType.EQUAL_EQUAL),
        ("!=", TokenType.BANG_EQUAL),
    ]

    for op_str, expected_type in operators:
        lexer = Lexer(op_str)
        tokens = lexer.tokenize()

        # We should have exactly two tokens: the operator and EOF
        assert len(tokens) == 2, f"Expected 2 tokens for '{op_str}', got {len(tokens)}"
        assert (
            tokens[0].type == expected_type
        ), f"Expected {expected_type} for '{op_str}', got {tokens[0].type}"
        assert tokens[1].type == TokenType.EOF

    # Test for division and comments using SLASH and SLASH_SLASH
    source = "10 / 3  # This is a comment"
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    # Should be: NUMBER(10), WHITESPACE, SLASH(/), WHITESPACE, NUMBER(3), WHITESPACE, COMMENT, EOF
    token_types = [t.type for t in tokens]
    assert TokenType.SLASH in token_types, "SLASH operator not found in tokens"

    # Find the SLASH token and verify its value
    slash_tokens = [t for t in tokens if t.type == TokenType.SLASH]
    assert (
        len(slash_tokens) == 1
    ), f"Expected exactly one SLASH token, got {len(slash_tokens)}"
    assert (
        slash_tokens[0].lexeme == "/"
    ), f"Expected '/' as token lexeme, got {slash_tokens[0].lexeme}"


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

    # Get non-EOF tokens (whitespace and comments are already filtered out by the lexer)
    code_tokens = [t for t in tokens if t.type != TokenType.EOF]

    # We should have: let, x, =, 42, let, y, =, 3.14
    assert len(code_tokens) == 8, f"Expected 8 code tokens, got {len(code_tokens)}"
    assert code_tokens[0].type == TokenType.LET
    assert code_tokens[1].type == TokenType.IDENTIFIER and code_tokens[1].lexeme == "x"
    assert code_tokens[2].type == TokenType.EQUAL
    assert code_tokens[3].type == TokenType.NUMBER and code_tokens[3].lexeme == "42"
    assert code_tokens[4].type == TokenType.LET
    assert code_tokens[5].type == TokenType.IDENTIFIER and code_tokens[5].lexeme == "y"
    assert code_tokens[6].type == TokenType.EQUAL
    assert code_tokens[7].type == TokenType.NUMBER and code_tokens[7].lexeme == "3.14"


def test_lexer_whitespace():
    """Test handling of various whitespace characters."""
    source = "let\t x\n=\r\n42\f\v"
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    assert [t.type for t in tokens] == [
        TokenType.LET,
        TokenType.IDENTIFIER,
        TokenType.EQUAL,
        TokenType.NUMBER,
        TokenType.EOF,
    ]


def test_lexer_error_handling():
    """Test error handling for invalid tokens."""
    source = "let x = @invalid#token"
    lexer = Lexer(source)

    with pytest.raises(SyntaxError, match="Invalid character '@' at line 1, column 9"):
        lexer.tokenize()


def test_lexer_hex_numbers():
    """Test hexadecimal number literals."""
    source = "0x1A 0x2f 0xDEADBEEF 0x123abc 0XFF"
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    numbers = [t for t in tokens if t.type == TokenType.NUMBER]
    assert len(numbers) == 5
    assert [t.lexeme for t in numbers] == [
        "0x1A",
        "0x2f",
        "0xDEADBEEF",
        "0x123abc",
        "0XFF",
    ]
    assert [t.literal for t in numbers] == [26, 47, 0xDEADBEEF, 0x123ABC, 0xFF]


def test_lexer_binary_numbers():
    """Test binary number literals."""
    source = "0b1010 0b0011 0b1111_0000 0B0101"
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    numbers = [t for t in tokens if t.type == TokenType.NUMBER]
    assert len(numbers) == 4
    assert [t.lexeme for t in numbers] == ["0b1010", "0b0011", "0b1111_0000", "0B0101"]
    assert [t.literal for t in numbers] == [10, 3, 0b11110000, 5]


def test_lexer_scientific_notation():
    """Test scientific notation numbers."""
    source = "1e3 2.5e-2 1.23e+4 1E5 1e-3"
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    numbers = [t for t in tokens if t.type == TokenType.NUMBER]
    assert len(numbers) == 5
    assert [t.literal for t in numbers] == [1e3, 2.5e-2, 1.23e4, 1e5, 1e-3]


def test_lexer_string_escapes():
    """Test string escape sequences."""
    source = (
        r'"Line 1\nLine 2" "Tab\tcharacter" "Quote: \"" "Backslash: \\" "\x41\x42\x43"'
    )
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    strings = [t for t in tokens if t.type == TokenType.STRING]
    assert len(strings) == 5
    assert strings[0].literal == "Line 1\nLine 2"
    assert strings[1].literal == "Tab\tcharacter"
    assert strings[2].literal == 'Quote: "'
    assert strings[3].literal == "Backslash: \\"
    assert strings[4].literal == "ABC"


def test_lexer_keywords():
    """Test all language keywords."""
    keywords = [
        "if",
        "else",
        "for",
        "while",
        "function",
        "return",
        "let",
        "const",
        "var",
        "true",
        "false",
        "null",
        "print",
    ]

    for keyword in keywords:
        lexer = Lexer(keyword)
        tokens = lexer.tokenize()
        assert len(tokens) == 2  # Keyword + EOF
        assert tokens[0].type != TokenType.IDENTIFIER
        assert tokens[0].lexeme == keyword


def test_lexer_position_tracking():
    """Test that line and column numbers are tracked correctly."""
    source = """
let x = 42
if x > 10 {
    print("Hello")
}"""
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    # Check positions of key tokens
    assert tokens[0].line == 3 and tokens[0].column == 1  # let
    assert tokens[1].line == 3 and tokens[1].column == 5  # x
    assert tokens[2].line == 3 and tokens[2].column == 7  # =
    assert tokens[3].line == 3 and tokens[3].column == 9  # 42
    assert tokens[4].line == 5 and tokens[4].column == 1  # if
    assert tokens[8].line == 5 and tokens[8].column == 11  # {
    assert tokens[9].line == 6 and tokens[9].column == 16  # print


def test_lexer_error_recovery():
    """Test that the lexer raises errors on invalid characters."""
    source = 'let x = @#$ 42 "valid" 123'
    lexer = Lexer(source)

    with pytest.raises(SyntaxError, match="Invalid character '@' at line 1, column 9"):
        lexer.tokenize()


def test_lexer_error_messages():
    """Test that lexer error messages are informative."""
    source = '"unclosed string'
    lexer = Lexer(source)

    with pytest.raises(SyntaxError, match="Invalid character '\"' at line 1, column 1"):
        lexer.tokenize()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
