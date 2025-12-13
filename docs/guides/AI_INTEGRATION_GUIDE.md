# 🤖 AI Integration Guide for HyperCode

> **Making HyperCode AI-friendly: A complete guide for contributors**

## 🎯 Quick Navigation

- [Overview](#overview)
- [Adding AI Features: 4-Step Process](#adding-ai-features)
- [Existing AI Features](#existing-ai-features)
- [Provider Configuration](#provider-configuration)
- [Testing AI Features](#testing)
- [Best Practices](#best-practices)

---

## Overview

HyperCode is designed to be **AI-augmented from the ground up**. This means AI isn't bolted on—it's woven into the language's DNA.

### What Makes HyperCode AI-Friendly?

- **Clean, consistent syntax** - Easier for models to parse and generate
- **Explicit structure** - No hidden magic, everything is declarative
- **Natural language keywords** - Reads like English, not cryptic symbols
- **Predictable patterns** - AI can learn and suggest completions confidently

---

## Adding AI Features

### 4-Step Process to Add Any AI Feature

#### Step 1: Define the Intent
**What problem are you solving?**

Example intents:
- Code completion based on context
- Error explanation in plain English
- Code generation from natural language
- Refactoring suggestions
- Documentation generation

#### Step 2: Choose Your Provider
**Which AI service will power this?**

Supported providers:
- **OpenAI** (GPT-4, GPT-3.5) - Best for complex reasoning
- **Anthropic** (Claude) - Great for large contexts
- **Google** (Gemini) - Fast and cost-effective
- **Local models** (via Ollama) - Privacy-first option

#### Step 3: Implement the Feature
**Add code to the appropriate module**

```python
# Example: src/ai/completions.py

from src.ai.providers import get_provider

async def suggest_completion(code_context: str, cursor_position: int):
    """Generate code completion suggestions using AI."""
    
    provider = get_provider()  # Auto-selects from config
    
    prompt = f"""
    Given this HyperCode context:
    {code_context}
    
    Suggest the next line of code at position {cursor_position}.
    Follow HyperCode syntax rules: natural language, explicit structure.
    """
    
    response = await provider.complete(prompt)
    return parse_completion(response)
```

#### Step 4: Test & Document
**Ensure it works for neurodivergent developers**

- Test with ADHD-friendly flow (no friction)
- Verify dyslexia-friendly output (clear, minimal text)
- Check autism-friendly consistency (predictable behavior)
- Add examples to docs

---

## Existing AI Features

### 1. **AI-Powered Error Messages**
**Location:** `src/core/error_handler.py`

Transforms cryptic compiler errors into human-friendly explanations.

**Example:**
```
❌ Before: "SyntaxError: unexpected token at line 42"
✅ After:  "Hey! It looks like you forgot a 'then' keyword after your 'if' statement on line 42. Try adding it!"
```

### 2. **Code Completion**
**Location:** `src/ai/completions.py`

Real-time suggestions as you type.

**Features:**
- Context-aware (understands your project)
- Pattern-learning (adapts to your style)
- Multi-line suggestions

### 3. **Natural Language Code Generation**
**Location:** `src/ai/generation.py`

Write what you want in plain English, get HyperCode.

**Example:**
```
Input:  "create a function that adds two numbers"
Output: define add with x and y:
          return x plus y
```

### 4. **AI Code Review**
**Location:** `src/ai/review.py`

Get feedback on your code before committing.

**Checks for:**
- Readability (is it clear?)
- Neurodivergent-friendliness (chunked? visual?)
- Best practices (following HyperCode patterns?)

### 5. **Documentation Generation**
**Location:** `src/ai/docs.py`

Auto-generate docs from your code.

**Example:**
```hypercode
define calculate_score with points and multiplier:
  # AI generates: "Calculates final score by multiplying points by multiplier"
  return points times multiplier
```

---

## Provider Configuration

### Setup Your AI Provider

Create a `.env` file in the root:

```bash
# OpenAI
OPENAI_API_KEY=sk-your-key-here
HYPERCODE_AI_PROVIDER=openai
HYPERCODE_AI_MODEL=gpt-4

# OR Anthropic
ANTHROPIC_API_KEY=sk-ant-your-key
HYPERCODE_AI_PROVIDER=anthropic
HYPERCODE_AI_MODEL=claude-3-sonnet

# OR Google
GOOGLE_API_KEY=your-google-key
HYPERCODE_AI_PROVIDER=google
HYPERCODE_AI_MODEL=gemini-pro

# OR Local (Ollama)
HYPERCODE_AI_PROVIDER=ollama
HYPERCODE_AI_MODEL=codellama
OLLAMA_HOST=http://localhost:11434
```

### Provider Selection Logic

HyperCode auto-selects based on your config, with fallback chain:

1. Environment variable `HYPERCODE_AI_PROVIDER`
2. Config file `config/ai.yaml`
3. Default: OpenAI (if API key present)
4. Fallback: Local Ollama

---

## Testing AI Features

### Manual Testing

```bash
# Test AI completions
python -m src.ai.test_completions

# Test error explanations
python -m src.ai.test_errors

# Test code generation
python -m src.ai.test_generation
```

### Automated Tests

All AI features have unit tests in `/tests/ai/`

```bash
# Run all AI tests
pytest tests/ai/

# Run specific feature tests
pytest tests/ai/test_completions.py -v
```

### Neurodivergent-Friendly Testing Checklist

- [ ] **ADHD Test**: Can you use it without losing focus?
- [ ] **Dyslexia Test**: Is the output easy to read?
- [ ] **Autism Test**: Is the behavior predictable and consistent?
- [ ] **Hyperfocus Test**: Does it support flow state?

---

## Best Practices

### ✅ DO

- **Keep prompts simple** - AI works best with clear instructions
- **Provide context** - More context = better suggestions
- **Cache responses** - Don't spam the API
- **Handle errors gracefully** - AI can fail, show friendly fallbacks
- **Respect rate limits** - Don't overwhelm providers
- **Test with real users** - Especially neurodivergent developers

### ❌ DON'T

- **Over-rely on AI** - It's augmentation, not replacement
- **Expose API keys** - Use environment variables
- **Ignore privacy** - Let users choose local models
- **Make it required** - AI should enhance, not block
- **Forget accessibility** - Screen readers, keyboard nav, etc.

---

## Adding a New AI Provider

Want to add support for a new AI service? Follow this template:

```python
# src/ai/providers/your_provider.py

from src.ai.providers.base import AIProvider

class YourProviderAI(AIProvider):
    """
    Integration with YourProvider AI service.
    """
    
    def __init__(self, api_key: str, model: str = "default-model"):
        self.api_key = api_key
        self.model = model
        self.client = YourProviderClient(api_key)
    
    async def complete(self, prompt: str, max_tokens: int = 150):
        """Generate code completion."""
        response = await self.client.complete(
            prompt=prompt,
            model=self.model,
            max_tokens=max_tokens
        )
        return response.text
    
    async def explain(self, code: str, error: str):
        """Explain an error in friendly language."""
        prompt = f"Explain this error to a neurodivergent developer:\n\nCode: {code}\nError: {error}"
        return await self.complete(prompt)
```

Then register it in `src/ai/providers/__init__.py`:

```python
from src.ai.providers.your_provider import YourProviderAI

PROVIDERS = {
    'openai': OpenAIProvider,
    'anthropic': AnthropicProvider,
    'google': GoogleProvider,
    'ollama': OllamaProvider,
    'yourprovider': YourProviderAI,  # Add here
}
```

---

## 🎓 Learning Resources

- [OpenAI API Docs](https://platform.openai.com/docs)
- [Anthropic Claude Guide](https://docs.anthropic.com/claude/docs)
- [Google Gemini Docs](https://ai.google.dev/docs)
- [Ollama Local Models](https://ollama.ai/)

---

## 💬 Need Help?

- 🐛 [Report AI Feature Bugs](https://github.com/welshDog/hypercode/issues/new?labels=ai,bug)
- 💡 [Suggest AI Features](https://github.com/welshDog/hypercode/issues/new?labels=ai,enhancement)
- 🤔 [Ask Questions](https://github.com/welshDog/hypercode/discussions/new?category=q-a)

---

**Made with 💜 by neurodivergent developers, for neurodivergent developers**

[Back to Main Docs](README.md) | [Contributing Guide](community/CONTRIBUTING.md)
