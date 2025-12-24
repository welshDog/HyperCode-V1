# Contributing to HyperCode

Thank you for your interest in contributing to HyperCode! We welcome contributions from developers of all experience levels, especially those interested in cognitive accessibility and innovative programming paradigms. This guide will help you get started with contributing to the project.

## 🌟 Project Status

### 🚧 Current Implementation Status

```text
🟢 Working: Basic syntax, function definitions, variable assignment
🟡 In Progress: Loop constructs, data structures, error handling
🔴 Planned: AI co-pilot integration, Visual IDE, Quantum syntax extensions
```

### 📅 Development Roadmap

#### Phase 1: Core Functionality (Weeks 1-2)

- [ ] Minimal parser implementation
- [ ] Basic AI integration test with Claude
- [ ] Onboard 3-5 neurodivergent beta testers

#### Phase 2: Community Engagement (Weeks 3-4)

- [ ] Weekly demo videos (2 min each)
- [ ] GitHub Discussions for syntax debates
- [ ] "Design with me" live coding sessions
- [ ] Beta tester feedback implementation

#### Phase 3: Expansion (Month 2+)

- [ ] Full IDE integration
- [ ] Advanced AI co-pilot features
- [ ] Quantum computing extensions

We believe in transparent development. Check our [REALITY.md](./REALITY.md) for the most current status and known issues.

## 🤝 How to Contribute

We value all types of contributions, not just code! Here are some ways you can help:

### 🧠 For Neurodivergent Developers

- Test the language and provide feedback on cognitive load
- Share your unique perspectives on syntax and tooling
- Help document your experience with the language

### 💻 For Developers

- Work on issues labeled `good first issue`
- Improve test coverage
- Help with documentation
- Report and fix bugs

### 🔍 For Researchers

- Help measure cognitive load improvements
- Contribute to our research on programming language accessibility
- Analyze AI-generated code quality

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

## 🧪 Experimental Features

We encourage experimentation! If you have an idea that aligns with our vision:

1. Create an issue to discuss the idea
2. Tag it with `experimental`
3. Follow our "document first" approach by updating REALITY.md
4. Create a draft PR early for feedback

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

## 📝 Pull Request Process

1. Fork the repository and create your branch from `main`
2. If you've added code that should be tested, add tests
3. Ensure the test suite passes
4. Update REALITY.md if your changes affect current capabilities
5. Add a clear description of:
   - The problem you're solving
   - How you solved it
   - Any cognitive accessibility considerations
6. Issue a pull request to the `main` branch

## 🌈 Neurodiversity Statement

HyperCode is being developed with neurodiversity in mind. We recognize that:

- Different people think and process information differently
- Traditional programming paradigms may not work for everyone
- Your unique perspective is valuable

We're particularly interested in contributions that help make programming more accessible to neurodivergent individuals. If you have specific needs or suggestions, please don't hesitate to share them.

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
