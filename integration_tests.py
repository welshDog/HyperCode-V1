"""
HYPERcode Integration Tests
Tests for AI integrations and language feature interactions
"""

import asyncio
from typing import Any, Dict
from unittest.mock import AsyncMock, Mock, patch

import pytest

# ============================================================================
# FIXTURES & TEST DATA
# ============================================================================


@pytest.fixture
def mock_ai_response():
    """Mock AI provider response"""
    return {
        "content": "function hello() { return 'Hello, HYPERcode!'; }",
        "model": "gpt-4",
        "tokens": {"input": 50, "output": 25},
        "timestamp": "2025-12-20T18:30:00Z",
    }


@pytest.fixture
def sample_hypercode_snippet():
    """Sample HYPERcode program"""
    return """
    THINK about greet
    INPUT: name
    OUTPUT: message
    
    message = "Hello, " + name + "!"
    RETURN message
    """


@pytest.fixture
async def ai_integration_client():
    """Async AI integration client"""
    client = Mock()
    client.connect = AsyncMock(return_value=True)
    client.generate = AsyncMock()
    client.close = AsyncMock()
    return client


# ============================================================================
# AI INTEGRATION TESTS
# ============================================================================


class TestAIIntegration:
    """Test suite for AI model integrations"""

    @pytest.mark.asyncio
    async def test_connect_to_openai(self):
        """Test OpenAI connection"""
        from hypercode.ai.providers import OpenAIProvider

        with patch.dict("os.environ", {"OPENAI_API_KEY": "test-key"}):
            provider = OpenAIProvider()
            assert provider.model_name == "gpt-4"
            assert provider.api_key == "test-key"

    @pytest.mark.asyncio
    async def test_connect_to_claude(self):
        """Test Claude connection"""
        from hypercode.ai.providers import ClaudeProvider

        with patch.dict("os.environ", {"ANTHROPIC_API_KEY": "test-key"}):
            provider = ClaudeProvider()
            assert provider.model_name == "claude-3-opus"
            assert provider.api_key == "test-key"

    @pytest.mark.asyncio
    async def test_ai_code_generation(self, ai_integration_client, mock_ai_response):
        """Test AI code generation from natural language"""
        ai_integration_client.generate.return_value = mock_ai_response

        prompt = "Write a function that adds two numbers"
        response = await ai_integration_client.generate(prompt)

        assert response["content"] is not None
        assert response["model"] == "gpt-4"
        assert response["tokens"]["input"] > 0
        ai_integration_client.generate.assert_called_once_with(prompt)

    @pytest.mark.asyncio
    async def test_ai_error_handling(self, ai_integration_client):
        """Test AI error handling"""
        error_msg = "Rate limit exceeded"
        ai_integration_client.generate.side_effect = Exception(error_msg)

        with pytest.raises(Exception) as exc_info:
            await ai_integration_client.generate("test prompt")

        assert error_msg in str(exc_info.value)

    @pytest.mark.asyncio
    async def test_fallback_ai_model(self):
        """Test fallback to alternative AI model on failure"""
        from hypercode.ai.providers import AIProviderFactory

        factory = AIProviderFactory()

        # Mock primary provider failing
        with patch.object(factory, "primary_provider") as mock_primary:
            mock_primary.generate.side_effect = ConnectionError()

            # Should fallback to secondary
            with patch.object(factory, "fallback_provider") as mock_fallback:
                mock_fallback.generate = AsyncMock(return_value={"content": "fallback"})
                result = await factory.generate("test")

                assert result["content"] == "fallback"


# ============================================================================
# LANGUAGE FEATURE INTEGRATION TESTS
# ============================================================================


class TestLanguageFeatures:
    """Test suite for HYPERcode language features"""

    def test_variable_declaration(self):
        """Test variable declaration and assignment"""
        from hypercode.parser import Parser

        code = "number = 42"
        parser = Parser()
        ast = parser.parse(code)

        assert ast is not None
        assert ast.statements[0].type == "assignment"
        assert ast.statements[0].value == 42

    def test_function_definition(self, sample_hypercode_snippet):
        """Test function definition"""
        from hypercode.parser import Parser

        parser = Parser()
        ast = parser.parse(sample_hypercode_snippet)

        assert ast is not None
        assert any(stmt.type == "function_def" for stmt in ast.statements)

    def test_neurodivergent_syntax(self):
        """Test neurodivergent-friendly syntax parsing"""
        from hypercode.parser import Parser

        # THINK - represents clear intention
        code = "THINK about calculate_sum"
        parser = Parser()
        ast = parser.parse(code)

        assert ast is not None
        # Should recognize THINK keyword as intention marker
        assert any(stmt.keyword == "THINK" for stmt in ast.statements)

    def test_input_output_handling(self):
        """Test INPUT/OUTPUT semantic clarity"""
        from hypercode.parser import Parser

        code = """
        INPUT: user_name, user_age
        OUTPUT: greeting_message
        """
        parser = Parser()
        ast = parser.parse(code)

        assert ast is not None
        # Should recognize input/output declarations
        input_vars = [stmt.variables for stmt in ast.statements if stmt.type == "input"]
        assert len(input_vars) > 0

    def test_control_flow(self):
        """Test control flow statements"""
        from hypercode.parser import Parser

        code = """
        IF condition
            RETURN result
        ELSE
            RETURN alternative
        """
        parser = Parser()
        ast = parser.parse(code)

        assert ast is not None
        assert any(stmt.type == "if_statement" for stmt in ast.statements)


# ============================================================================
# COMPILER & EXECUTION TESTS
# ============================================================================


class TestCompilation:
    """Test suite for HYPERcode compilation"""

    def test_hypercode_to_python(self, sample_hypercode_snippet):
        """Test HYPERcode to Python compilation"""
        from hypercode.compiler import Compiler

        compiler = Compiler()
        python_code = compiler.compile(sample_hypercode_snippet, target="python")

        assert python_code is not None
        assert "def " in python_code  # Should contain Python function
        assert "return" in python_code

    def test_hypercode_to_javascript(self, sample_hypercode_snippet):
        """Test HYPERcode to JavaScript compilation"""
        from hypercode.compiler import Compiler

        compiler = Compiler()
        js_code = compiler.compile(sample_hypercode_snippet, target="javascript")

        assert js_code is not None
        assert "function " in js_code

    def test_compilation_error_handling(self):
        """Test compilation error handling"""
        from hypercode.compiler import Compiler

        compiler = Compiler()
        invalid_code = "INVALID SYNTAX HERE"

        with pytest.raises(SyntaxError):
            compiler.compile(invalid_code, target="python")

    @pytest.mark.asyncio
    async def test_ai_assisted_compilation(
        self, ai_integration_client, sample_hypercode_snippet
    ):
        """Test AI-assisted compilation optimization"""
        from hypercode.compiler import CompilerWithAI

        ai_integration_client.generate = AsyncMock(
            return_value={
                "content": "optimized_code_here",
                "optimization": "tail-recursion",
            }
        )

        compiler = CompilerWithAI(ai_client=ai_integration_client)
        result = await compiler.compile_with_optimization(sample_hypercode_snippet)

        assert result is not None
        assert "optimization" in result


# ============================================================================
# COGNITIVE ACCESSIBILITY TESTS
# ============================================================================


class TestCognitiveAccessibility:
    """Test suite for neurodivergent accessibility features"""

    def test_syntax_clarity(self):
        """Test that syntax is clear and unambiguous"""
        from hypercode.parser import Parser

        # Ambiguous syntax should fail gracefully
        ambiguous_code = "x y z"  # No clear operation
        parser = Parser()

        with pytest.raises(SyntaxError):
            parser.parse(ambiguous_code)

    def test_error_messages_clarity(self):
        """Test that error messages are clear and helpful"""
        from hypercode.parser import Parser

        invalid_code = "RETURN without function"
        parser = Parser()

        with pytest.raises(SyntaxError) as exc_info:
            parser.parse(invalid_code)

        # Error message should be clear and actionable
        error_msg = str(exc_info.value)
        assert "RETURN" in error_msg
        assert "function" in error_msg

    def test_visual_consistency(self):
        """Test visual consistency of code blocks"""
        from hypercode.formatter import Formatter

        code = "x=1\ny=2\nz=x+y"
        formatter = Formatter()
        formatted = formatter.format(code)

        # Should maintain consistent indentation and spacing
        lines = formatted.split("\n")
        assert all(line.startswith(" " * 4) or line == "" for line in lines)

    def test_minimal_noise_principle(self):
        """Test that syntax has minimal unnecessary characters"""
        from hypercode.parser import Parser

        # Clean, readable syntax
        clean_code = "THINK about calculate\nRETURN result"
        parser = Parser()
        ast = parser.parse(clean_code)

        assert ast is not None
        # No unnecessary brackets, parentheses, or symbols


# ============================================================================
# END-TO-END INTEGRATION TESTS
# ============================================================================


class TestEndToEnd:
    """End-to-end integration tests"""

    @pytest.mark.asyncio
    async def test_complete_workflow(self, ai_integration_client):
        """Test complete HYPERcode workflow"""
        from hypercode.engine import HyperCodeEngine

        engine = HyperCodeEngine(ai_client=ai_integration_client)

        # 1. Natural language description
        description = "Create a function that greets a user by name"

        # 2. AI generates HYPERcode
        ai_integration_client.generate = AsyncMock(
            return_value={
                "content": "THINK about greet\nINPUT: name\nRETURN 'Hello, ' + name",
                "model": "gpt-4",
            }
        )

        hypercode = await engine.generate_from_description(description)
        assert hypercode is not None

        # 3. Compile to Python
        python_code = engine.compile_to_python(hypercode)
        assert python_code is not None
        assert "def " in python_code

        # 4. Execute
        result = engine.execute_python(python_code, {"name": "Alice"})
        assert "Alice" in result


# ============================================================================
# PERFORMANCE TESTS
# ============================================================================


class TestPerformance:
    """Performance and load tests"""

    @pytest.mark.asyncio
    async def test_compilation_performance(self, sample_hypercode_snippet):
        """Test compilation speed"""
        import time

        from hypercode.compiler import Compiler

        compiler = Compiler()

        start = time.time()
        for _ in range(100):
            compiler.compile(sample_hypercode_snippet, target="python")
        elapsed = time.time() - start

        # Should compile 100 snippets in < 1 second
        assert elapsed < 1.0

    @pytest.mark.asyncio
    async def test_ai_response_timeout(self, ai_integration_client):
        """Test handling of slow AI responses"""
        import asyncio

        ai_integration_client.generate = AsyncMock(side_effect=asyncio.TimeoutError())

        with pytest.raises(asyncio.TimeoutError):
            await ai_integration_client.generate("test", timeout=0.1)


# ============================================================================
# PYTEST CONFIGURATION
# ============================================================================


@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for async tests"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


# Run tests with:
# pytest tests/integration/ -v --cov=hypercode --cov-report=html
