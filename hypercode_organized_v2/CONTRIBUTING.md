# Contributing to HyperCode

Thank you for your interest in contributing to HyperCode! We welcome contributions from developers of all experience levels. This guide will help you get started with contributing to the project.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Git
- pip (Python package manager)

### Setting Up Your Development Environment

1. **Fork the repository**

   Click the "Fork" button on the top right of the [repository page](https://github.com/welshDog/HYPERcode-V1).

2. **Clone your fork**

   ```bash
   git clone https://github.com/your-username/HYPERcode-V1.git
   cd HYPERcode-V1
   ```

3. **Set up a virtual environment**

   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

5. **Run tests**

   ```bash
   pytest
   ```

## 🛠 Development Workflow

1. **Create a new branch**

   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/issue-number-description
   ```

2. **Make your changes**

   - Follow the project's code style
   - Write tests for new features
   - Update documentation as needed

3. **Run tests and linters**

   ```bash
   # Run tests
   pytest

   # Run linter
   flake8 hypercode tests

   # Format code
   black .
   isort .
   ```

4. **Commit your changes**

   ```bash
   git add .
   # Format code
   black .
   isort .
   git commit -m "feat: add new feature"
   ```

   **Commit message format:**

   ```text
   type(scope): subject
   
   [optional body]
   
   [optional footer]
   ```
   
   **Types:**
   - feat: A new feature
   - fix: A bug fix
   - docs: Documentation changes
   - style: Code style changes
   - refactor: Code changes that neither fix bugs nor add features
   - test: Adding missing tests or correcting existing tests
   - chore: Changes to the build process or auxiliary tools

5. **Push your changes**

   ```bash
   git push origin your-branch-name
   ```

6. **Create a Pull Request**
   - Go to the repository: <https://github.com/welshDog/HYPERcode-V1>
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template
   - Submit the PR

## 🧪 Testing Guidelines

- Write tests for all new features and bug fixes
- Follow the existing test structure
- Use descriptive test names
- Test edge cases and error conditions
- Keep tests independent and isolated

## 📝 Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use type hints for all new code
- Keep functions small and focused
- Use clear, descriptive names for variables and functions
- Add docstrings to all public functions and classes

## 📚 Documentation

- Update relevant documentation when adding new features
- Follow the existing documentation style
- Add examples for new features
- Document any breaking changes

## 🔒 Security

- Report security vulnerabilities to security@hypercode.dev
- Follow security best practices
- Never commit sensitive information
- Keep dependencies up to date

## 🤝 Code of Conduct

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before contributing. We are committed to providing a friendly, safe, and welcoming environment for all contributors.

## 🙏 Thank You

Your contributions help make HyperCode better for everyone. Thank you for your time and effort!
