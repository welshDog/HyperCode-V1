# 🚀 HyperCode: Installation & Setup Guide

## Get Running in 5 Minutes! ⚡

**Last Updated**: November 11, 2025 **Status**: Production-Ready Configuration

---

## 📋 Prerequisites

Before you start, make sure you have:

- **Python 3.10+** → [Download](https://www.python.org/downloads/)
- **Git** → [Download](https://git-scm.com/)
- **Virtual environment** (built-in with Python)
- **pip** (comes with Python)

Verify:

```bash
python --version    # Should be 3.10+
git --version       # Should be 2.30+
pip --version       # Should be latest
```

---

## 🎯 Option 1: Clone from GitHub (Recommended)

### Step 1: Clone Repository

```bash
git clone https://github.com/welshDog/hypercode.git
cd hypercode
```

### Step 2: Create Virtual Environment

```bash
# Create venv
python3 -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
# Production dependencies only
pip install -r requirements.txt

# OR development + testing (recommended)
pip install -r requirements-dev.txt

# Verify installation
pip list | grep hypercode
```

### Step 4: Setup Pre-commit Hooks

```bash
# Install pre-commit framework
pip install pre-commit

# Install git hooks
pre-commit install

# (Optional) Test hooks on all files
pre-commit run --all-files
```

### Step 5: Configure Environment

```bash
# Copy example env file
cp .env.example .env

# Edit .env with your API keys (vi, nano, or your editor)
nano .env
```

### Step 6: Verify Installation

```bash
# Run tests
pytest tests/ -v

# Check code quality
black --check core/
flake8 core/
mypy core/

# All should pass! ✅
```

---

## 📦 Option 2: Install from PyPI (When Published)

```bash
# Simple install
pip install hypercode

# With development tools
pip install hypercode[dev]

# With documentation tools
pip install hypercode[docs]
```

---

## 🔧 Option 3: Development Installation (For Contributors)

```bash
# Clone repo
git clone https://github.com/welshDog/hypercode.git
cd hypercode

# Create venv
python3 -m venv venv
source venv/bin/activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install

# Create .env file
cp .env.example .env
nano .env  # Add your API keys

# Verify everything works
pytest tests/ -v --cov=core --cov-report=html

# Run linting
black core/
flake8 core/
mypy core/

# You're ready to code! 🔥
```

---

## 🧪 Running Tests

### All Tests

```bash
pytest tests/ -v
```

### Specific Test File

```bash
pytest tests/test_lexer.py -v
```

### With Coverage Report

```bash
pytest tests/ -v --cov=core --cov-report=html
# Open htmlcov/index.html in browser
```

### Watch Mode (Auto-run on changes)

```bash
pytest-watch tests/
```

---

## 🔍 Code Quality Checks

### Format Code (Black)

```bash
black core/ tests/
```

### Lint Code (Flake8)

```bash
flake8 core/ tests/
```

### Type Check (MyPy)

```bash
mypy core/
```

### Security Scan (Bandit)

```bash
bandit -r core/
```

### All Checks (Pre-commit)

```bash
pre-commit run --all-files
```

---

## 🚀 Running the Lexer

### Direct Execution

```bash
python core/lexer.py
```

### Import in Python

```python
from core.lexer import HyperCodeLexer

lexer = HyperCodeLexer()
tokens = lexer.tokenize("+++>.")
for token in tokens:
    print(token)
```

---

## 📚 Documentation

- **Language Spec**: [docs/LANGUAGE_SPEC.md](docs/LANGUAGE_SPEC.md)
- **AI Compatibility**: [docs/AI_COMPAT.md](docs/AI_COMPAT.md)
- **Accessibility**: [docs/ACCESSIBILITY.md](docs/ACCESSIBILITY.md)
- **Architecture**: [docs/ARCHITECTURE.md](architecture/ARCHITECTURE.md)
- **Contributing**: [CONTRIBUTING.md](community/CONTRIBUTING.md)

---

## 🐛 Troubleshooting

### Problem: `ModuleNotFoundError: No module named 'core'`

**Solution**: Make sure you're in the repo root and venv is activated

```bash
pwd  # Should show .../hypercode
which python  # Should show venv/bin/python
```

### Problem: `pip install` fails

**Solution**: Upgrade pip and try again

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Problem: Pre-commit hooks failing

**Solution**: Install dependencies and try again

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

### Problem: Tests failing

**Solution**: Check Python version and dependencies

```bash
python --version  # Must be 3.10+
pytest --version
pytest tests/test_lexer.py -v
```

---

## 🔗 Useful Commands Quick Reference

```bash
# Virtual environment
python3 -m venv venv          # Create venv
source venv/bin/activate      # Activate (Linux/Mac)
deactivate                     # Deactivate

# Installation
pip install -r requirements.txt
pip install -e ".[dev]"

# Testing
pytest tests/
pytest tests/test_lexer.py -v
pytest-watch tests/

# Code quality
black core/
flake8 core/
mypy core/
pre-commit run --all-files

# Git
git clone https://github.com/welshDog/hypercode.git
git add .
git commit -m "message"
git push origin main
```

---

## 🎯 Next Steps After Installation

1. **Read the docs**: Start with [LANGUAGE_SPEC.md](docs/LANGUAGE_SPEC.md)
2. **Run examples**: Try programs in `examples/`
3. **Write code**: Follow [CONTRIBUTING.md](community/CONTRIBUTING.md)
4. **Join community**: Discord link in README
5. **Build amazing things**: You're ready! 🚀

---

## 📞 Need Help?

- **GitHub Issues**: https://github.com/welshDog/hypercode/issues
- **Discussions**: https://github.com/welshDog/hypercode/discussions
- **Discord**: (link in README)
- **Email**: hello@hypercode.dev

---

## 🎉 You're All Set!

You now have HyperCode installed and ready to build!

**Next**: Check out [CONTRIBUTING.md](community/CONTRIBUTING.md) for development workflow.

**Happy coding, bro!** 👊💫

---

**Questions?** Open an issue on GitHub! We're here to help! 🤝
