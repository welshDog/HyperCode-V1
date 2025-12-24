# Contributing to HyperCode

Welcome to HyperCode! We're excited you want to contribute to our neurodivergent-first programming language. This guide will help you get started.

## Table of Contents

- [Repository Structure](#repository-structure)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Style](#code-style)
- [AI Integration](#ai-integration)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)

## Repository Structure

```text
hypercode/
├── src/hypercode/
│   ├── core/               # Core language implementation
│   │   ├── lexer.py        # Tokenizes source code
│   │   ├── parser.py       # Converts tokens to AST
│   │   ├── interpreter.py  # Executes the AST
│   │   └── ast.py          # AST node definitions
│   ├── ai/                 # AI integration
│   │   ├── perplexity_client.py
│   │   └── enhanced_perplexity_client.py
│   └── cli/                # Command-line interface
├── tests/                  # Test suites
└── examples/               # Example projects
```

## Getting Started

1. **Fork and Clone**:

   ```bash
   git clone https://github.com/your-username/hypercode.git
   cd hypercode
   ```

2. **Set Up Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   pre-commit install
   ```

3. **Verify Installation**:

   ```bash
   python -m hypercode --version
   pytest
   ```

## Development Workflow

### Adding Language Features

1. **Update Lexer** (`lexer.py`):
   - Add new token types
   - Implement token recognition

2. **Update Parser** (`parser.py`):
   - Add grammar rules
   - Create AST nodes

3. **Update Interpreter** (`interpreter.py`):
   - Implement execution logic
   - Add built-in functions

### Example: Adding a New Operator

1. Add token type to `tokens.py`:

   ```python
   class TokenType(Enum):
       # Existing tokens...
       DOUBLE_PLUS = "++"
   ```

2. Update lexer to recognize the token:

   ```python
   def scan_token(self):
       if self.match('+'):
           if self.match('+'):
               self.add_token(TokenType.DOUBLE_PLUS)
   ```

## AI Integration

### Using AI Assistants

```python
from hypercode.ai import EnhancedPerplexityClient

client = EnhancedPerplexityClient()
response = client.generate_code(
    prompt="Implement a quicksort function",
    context=current_file_content
)
```

### Adding AI Features

1. Create a new client in `hypercode/ai/`
2. Implement the base interface
3. Add tests in `tests/ai/`

## Testing

Run tests with:

```bash
pytest tests/unit/        # Unit tests
pytest tests/integration/ # Integration tests
pytest tests/ai/          # AI-specific tests
```

## Code Style

- Follow PEP 8 with 4-space indentation
- Use type hints for all functions
- Document public APIs with docstrings
- Keep functions small and focused
- Write tests for new features

## Submitting Changes

1. Create a feature branch:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes with clear, atomic commits

3. Run tests and linters:

   ```bash
   black .
   isort .
   mypy .
   pytest
   ```

4. Push and create a pull request
