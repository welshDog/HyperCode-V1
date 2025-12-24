# Contributing to HyperCode 🚀

First off, thank you for considering contributing to HyperCode! We're excited to have you on board. This guide will help you get started with contributing to our project.

## 🏁 Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork locally
   ```bash
   git clone https://github.com/your-username/hypercode.git
   cd hypercode
   ```
3. **Set up** the development environment (see [Development Setup](#-development-setup) below)
4. **Create a branch** for your changes
   ```bash
   git checkout -b feature/your-feature-name
   ```
5. **Commit** your changes with a descriptive message
6. **Push** to your fork and open a **Pull Request**

## 🛠 Development Setup

### Prerequisites
- Python 3.10+
- Node.js 16+ (for TypeScript/UI components)
- Git

### Installation

1. **Python Environment**
   ```bash
   # Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install development dependencies
   pip install -r requirements-dev.txt
   ```

2. **TypeScript/UI Setup** (if working on visual components)
   ```bash
   cd frontend
   npm install
   ```

## 🏗 Project Structure

```
hypercode/
├── core/               # Core language implementation (Python)
├── frontend/           # Visual tools and web interface (TypeScript/React)
├── docs/               # Documentation
├── examples/           # Example HyperCode programs
├── tests/              # Test suite
├── scripts/            # Utility scripts
└── archive/            # Archived/experimental code
```

## 🧪 Testing

Run the test suite:

```bash
# Run Python tests
pytest

# Run TypeScript tests (from frontend directory)
cd frontend
npm test
```

## 📝 Code Style

- Python: Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- TypeScript: Follow [TypeScript style guide](https://google.github.io/styleguide/tsguide.html)
- Commit messages: Use [Conventional Commits](https://www.conventionalcommits.org/)

## 🐛 Good First Issues

New to the project? Check out these good first issues:

1. [Add more example programs](https://github.com/welshDog/hypercode/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
2. [Improve documentation](https://github.com/welshDog/hypercode/issues?q=is%3Aissue+is%3Aopen+label%3Adocumentation)
3. [Enhance error messages](https://github.com/welshDog/hypercode/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)

## 🤝 Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project you agree to abide by its terms.

## 📬 Questions?

Feel free to open an issue or join our [Discussions](https://github.com/welshDog/hypercode/discussions) if you have any questions!
