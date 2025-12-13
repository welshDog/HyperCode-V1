# 🛠️ HyperCode Development Guide

> **Complete setup guide for contributing to HyperCode core**

## 🎯 Quick Navigation

- [Development Environment Setup](#setup)
- [Project Structure](#structure)
- [Development Workflow](#workflow)
- [Running Tests](#testing)
- [Code Quality](#quality)
- [Debugging](#debugging)
- [Common Tasks](#tasks)

---

## Setup

### Prerequisites

- **Python 3.10+** - [Download here](https://www.python.org/downloads/)
- **Git** - [Install Git](https://git-scm.com/downloads)
- **pip** - Comes with Python
- **(Optional) VS Code** - [Recommended editor](https://code.visualstudio.com/)

### Clone the Repository

```bash
# Clone your fork (or the main repo)
git clone https://github.com/YOUR-USERNAME/hypercode.git
cd hypercode
```

### Install Dependencies

```bash
# Install core dependencies
pip install -r requirements.lock

# Install development dependencies
pip install -r docs/requirements-dev.txt

# OR use the Makefile
make install
```

### Verify Installation

```bash
# Check Python version
python --version  # Should be 3.10+

# Run HyperCode
python -m src.hypercode --version

# Run tests
pytest
```

**🟢 You're ready to develop!**

---

## Structure

### Project Layout

```
hypercode/
├── src/                    # Source code
│   ├── core/              # Language core (lexer, parser, interpreter)
│   ├── hypercode/         # Main package
│   ├── ai/                # AI integration modules
│   └── utils/             # Utility functions
├── tests/                 # Test suite
│   ├── unit/              # Unit tests
│   ├── integration/       # Integration tests
│   └── fixtures/          # Test data
├── examples/              # Example programs
├── docs/                  # Documentation
├── vscode-extension/      # VS Code extension
├── web-playground/        # Browser-based playground
└── scripts/               # Build and utility scripts
```

### Key Files

- `src/core/lexer.py` - Tokenizes HyperCode source
- `src/core/parser.py` - Builds abstract syntax tree (AST)
- `src/core/interpreter.py` - Executes the AST
- `src/hypercode/__main__.py` - CLI entry point
- `pyproject.toml` - Project metadata
- `pytest.ini` - Test configuration

---

## Workflow

### 1. Create a Feature Branch

```bash
# Update main
git checkout main
git pull origin main

# Create feature branch
git checkout -b feature/your-feature-name
```

### 2. Make Your Changes

Edit files in `src/`, add tests in `tests/`, update docs in `docs/`

### 3. Run Tests Locally

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/unit/test_lexer.py

# Run with coverage
pytest --cov=src
```

### 4. Format & Lint

```bash
# Auto-format code
black src/ tests/

# Check linting
flake8 src/ tests/

# OR use the Makefile
make format
make lint
```

### 5. Commit Your Changes

```bash
# Stage changes
git add .

# Commit with descriptive message
git commit -m "✨ Add feature: your feature description"

# Use conventional commits:
# ✨ feat: New feature
# 🐛 fix: Bug fix
# 📝 docs: Documentation
# ♻️ refactor: Code refactor
# ✅ test: Add tests
```

### 6. Push & Create PR

```bash
# Push to your fork
git push origin feature/your-feature-name

# Then create a Pull Request on GitHub
```

---

## Testing

### Running Tests

```bash
# All tests
pytest

# Specific category
pytest tests/unit/
pytest tests/integration/

# Specific file
pytest tests/unit/test_lexer.py

# Specific test
pytest tests/unit/test_lexer.py::test_tokenize_simple

# With verbose output
pytest -v

# With coverage report
pytest --cov=src --cov-report=html
```

### Writing Tests

Follow this pattern:

```python
# tests/unit/test_your_feature.py

import pytest
from src.your_module import your_function

def test_your_function_basic():
    """Test basic functionality."""
    result = your_function("input")
    assert result == "expected_output"

def test_your_function_edge_case():
    """Test edge case handling."""
    with pytest.raises(ValueError):
        your_function(None)
```

### Test Categories

- **Unit tests** - Test individual functions/classes
- **Integration tests** - Test multiple components together
- **End-to-end tests** - Test full programs from `.hc` files

---

## Quality

### Code Formatting

We use **Black** for consistent formatting:

```bash
# Format all code
black src/ tests/

# Check without modifying
black --check src/ tests/
```

### Linting

We use **Flake8** to catch issues:

```bash
# Run linter
flake8 src/ tests/

# With specific rules
flake8 src/ --max-line-length=100
```

### Type Checking

We use **mypy** for type hints:

```bash
# Check types
mypy src/
```

### Pre-commit Hooks

Automate quality checks:

```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Now every commit automatically runs:
# - Black (formatting)
# - Flake8 (linting)
# - Trailing whitespace removal
# - YAML validation
```

---

## Debugging

### Print Debugging

Add debug prints:

```python
print(f"DEBUG: variable value = {variable}")
```

### Python Debugger (pdb)

Set breakpoints:

```python
import pdb; pdb.set_trace()  # Execution pauses here
```

### VS Code Debugging

Create `.vscode/launch.json`:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Run HyperCode",
      "type": "python",
      "request": "launch",
      "module": "src.hypercode",
      "args": ["examples/demo_hello.hc"]
    },
    {
      "name": "Run Tests",
      "type": "python",
      "request": "launch",
      "module": "pytest"
    }
  ]
}
```

### Logging

Use Python's logging module:

```python
import logging

logger = logging.getLogger(__name__)
logger.debug("Detailed debug info")
logger.info("General info")
logger.warning("Warning message")
logger.error("Error occurred")
```

---

## Tasks

### Common Development Tasks

#### Add a New Language Feature

1. Update `src/core/lexer.py` (add tokens)
2. Update `src/core/parser.py` (add grammar rules)
3. Update `src/core/interpreter.py` (add execution logic)
4. Add tests in `tests/unit/`
5. Add example in `examples/`
6. Update `docs/LANGUAGE_REFERENCE.md`

#### Fix a Bug

1. Write a failing test that reproduces the bug
2. Fix the bug in `src/`
3. Verify the test now passes
4. Update docs if needed

#### Improve Performance

1. Add benchmark in `benchmarks/`
2. Profile with `cProfile`: `python -m cProfile -o output.prof script.py`
3. Optimize bottlenecks
4. Re-run benchmark to verify improvement

#### Add Documentation

1. Create/edit `.md` file in `docs/`
2. Follow existing style (headings, examples, tips)
3. Link from relevant pages
4. Preview with a Markdown viewer

---

## 📚 Additional Resources

- [Architecture Overview](architecture/ARCHITECTURE.md)
- [Code Style Guide](STYLE_GUIDE_DRAFT.md)
- [Testing Best Practices](reference/BEST_PRACTICES.md)
- [Contributing Guidelines](community/CONTRIBUTING.md)

---

## 💬 Need Help?

- 🐛 [Report Development Issues](https://github.com/welshDog/hypercode/issues/new?labels=development)
- 🤔 [Ask Questions](https://github.com/welshDog/hypercode/discussions/new?category=q-a)
- 💬 [Join the Community](https://github.com/welshDog/hypercode/discussions)

---

**Made with 💜 by neurodivergent developers, for neurodivergent developers**

[Back to Main Docs](README.md) | [Contributing Guide](community/CONTRIBUTING.md)
