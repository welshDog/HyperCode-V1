"""Tests for HyperCode syntax features."""

import pytest
from hypercode.core.lexer import Lexer  # type: ignore
from hypercode.core.tokens import TokenType  # type: ignore


def test_program_structure():
    """Test basic program structure and entry point."""
    source = """
    main {
        // Empty program
    }
    """
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    # Should have: main, {, }
    assert len(tokens) >= 3
    assert tokens[0].type == TokenType.IDENTIFIER
    assert tokens[0].lexeme == "main"
    assert tokens[1].type == TokenType.LEFT_BRACE
    assert tokens[2].type == TokenType.RIGHT_BRACE


def test_function_definition():
    """Test function definition syntax."""
    source = """
    function sayHello() {
        emit 72, output  // 'H'
        emit 101, output // 'e'
        emit 108, output // 'l'
        emit 108, output // 'l'
        emit 111, output // 'o'
    }
    """
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    # Check for function keyword, identifier, and braces
    assert tokens[0].type == TokenType.FUNCTION
    assert tokens[1].type == TokenType.IDENTIFIER
    assert tokens[1].lexeme == "sayHello"
    assert tokens[2].type == TokenType.LEFT_PAREN
    assert tokens[3].type == TokenType.RIGHT_PAREN
    assert tokens[4].type == TokenType.LEFT_BRACE


def test_io_operations():
    """Test input/output operations."""
    source = """
    main {
        emit 65, output     // 'A'
        emit input, store x // Read input
        emit x, output      // Echo input
    }
    """
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    # Check for emit, output, input, and store keywords
    emit_tokens = [t for t in tokens if t.type == TokenType.EMIT]
    output_tokens = [t for t in tokens if t.lexeme == "output"]
    input_tokens = [t for t in tokens if t.lexeme == "input"]
    store_tokens = [t for t in tokens if t.type == TokenType.STORE]

    assert len(emit_tokens) == 3
    assert len(output_tokens) == 2
    assert len(input_tokens) == 1
    assert len(store_tokens) == 1


def test_variables():
    """Test variable declarations and assignments."""
    source = """
    main {
        x = 10
        y = x + 5
        z = input
        w = z - 3
    }
    """
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    # Check for assignment operators and identifiers
    equals_tokens = [t for t in tokens if t.type == TokenType.EQUAL]
    plus_tokens = [t for t in tokens if t.type == TokenType.PLUS]
    minus_tokens = [t for t in tokens if t.type == TokenType.MINUS]

    assert len(equals_tokens) == 4
    assert len(plus_tokens) == 1
    assert len(minus_tokens) == 1


def test_loops():
    """Test loop constructs."""
    source = """
    main {
        x = 5
        repeat x times {
            emit 88, output  // 'X'
        }
    }
    """
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    # Check for repeat keyword and loop structure
    repeat_tokens = [t for t in tokens if t.type == TokenType.REPEAT]
    times_tokens = [t for t in tokens if t.lexeme == "times"]

    assert len(repeat_tokens) == 1
    assert len(times_tokens) == 1


def test_conditionals():
    """Test if/else conditionals."""
    source = """
    main {
        x = 0
        if x == 0 {
            emit 89, output  // 'Y'
        } else {
            emit 78, output  // 'N'
        }
    }
    """
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    # Check for if, else, and comparison operators
    if_tokens = [t for t in tokens if t.type == TokenType.IF]
    else_tokens = [t for t in tokens if t.type == TokenType.ELSE]
    eq_tokens = [t for t in tokens if t.type == TokenType.EQUAL_EQUAL]

    assert len(if_tokens) == 1
    assert len(else_tokens) == 1
    assert len(eq_tokens) == 1


def test_goto():
    """Test goto and labels."""
    source = """
    main {
        x = 3
        [ow:loop]
        emit x, output
        x = x - 1
        if x > 0 {
            goto loop
        }
    }
    """
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    # Check for label and goto
    label_tokens = [t for t in tokens if t.type == TokenType.LABEL]
    goto_tokens = [t for t in tokens if t.type == TokenType.GOTO]

    assert len(label_tokens) == 1
    assert len(goto_tokens) == 1
    assert any(t.lexeme == "loop" for t in tokens)


def test_comments():
    """Test that comments are properly ignored."""
    source = """
    // This is a comment
    main {
        // Another comment
        x = 42  // Inline comment
    } // End of program
    """
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    # Check that no token has the COMMENT type
    comment_tokens = [t for t in tokens if t.type == TokenType.COMMENT]
    assert len(comment_tokens) == 0

    # Check that we still have the main program structure
    main_tokens = [t for t in tokens if t.lexeme == "main"]
    assert len(main_tokens) == 1


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
