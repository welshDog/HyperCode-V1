#!/usr/bin/env python3
"""
HyperCode Project Scaffolder
Automatically creates the complete project structure cross-platform

Usage: python scaffold.py

This script creates:
- All required directories
- All necessary files with proper structure
- Starter content for key files
"""

import os
import stat
import sys
from datetime import datetime
from pathlib import Path

# Project metadata
PROJECT_NAME = "hypercode"
AUTHOR = "welshDog (Lyndz Williams)"
AUTHOR_EMAIL = "hello@hypercode.dev"
VERSION = "0.1.0"
LICENSE = "MIT"
DESCRIPTION = (
    "HyperCode: Neurodivergent-First Programming Language with AI Compatibility"
)

# Define the complete project structure
PROJECT_STRUCTURE = {
    # Core language modules
    "core": {
        "files": [
            "__init__.py",
            "lexer.py",
            "parser.py",
            "semantic_analyzer.py",
            "optimizer.py",
            "cli.py",
        ],
        "description": "Core HyperCode language implementation",
    },
    # Compilation backends
    "backends": {
        "files": [
            "__init__.py",
            "javascript.py",
            "python.py",
            "wasm.py",
            "quantum.py",
            "dna.py",
        ],
        "description": "Multi-backend compilation targets",
    },
    # AI model integration
    "ai_gateway": {
        "files": [
            "__init__.py",
            "base_gateway.py",
            "openai_adapter.py",
            "claude_adapter.py",
            "mistral_adapter.py",
            "ollama_adapter.py",
            "prompt_normalizer.py",
            "rag_engine.py",
        ],
        "description": "AI model compatibility layer",
    },
    # Accessibility features
    "accessibility": {
        "files": [
            "__init__.py",
            "wcag_auditor.py",
            "dyslexia_formatter.py",
            "adhd_optimizer.py",
            "autism_preset.py",
            "sensory_customizer.py",
        ],
        "description": "Neurodivergent-first accessibility tools",
    },
    # Knowledge graphs
    "knowledge_graph": {
        "files": [
            "__init__.py",
            "graph_builder.py",
            "sparql_query.py",
            "update_agent.py",
        ],
        "description": "Semantic knowledge graph management",
    },
    # Research automation
    "live_research": {
        "files": [
            "__init__.py",
            "research_crawler.py",
            "paper_indexer.py",
            "synthesis_engine.py",
            "doc_generator.py",
            "github_publisher.py",
        ],
        "description": "Automated research paper collection and synthesis",
    },
    # Test suite
    "tests": {
        "files": [
            "__init__.py",
            "test_lexer.py",
            "test_parser.py",
            "test_backends.py",
            "test_ai_gateway.py",
            "test_accessibility.py",
            "test_integration.py",
        ],
        "description": "Comprehensive test suite",
    },
    # Example programs
    "examples": {
        "files": ["hello_world.hc", "fibonacci.hc", "game_loop.hc", "quantum_demo.hc"],
        "description": "Example HyperCode programs",
    },
    # Documentation
    "docs": {
        "files": [
            "LANGUAGE_SPEC.md",
            "AI_COMPAT.md",
            "ACCESSIBILITY.md",
            "ARCHITECTURE.md",
            "CONTRIBUTING.md",
        ],
        "description": "Complete documentation",
    },
    # GitHub workflows
    ".github/workflows": {
        "files": ["ci.yml", "cd.yml", "research.yml", "security.yml"],
        "description": "GitHub Actions CI/CD workflows",
    },
}

# Root-level files to create
ROOT_FILES = [
    "Dockerfile",
    "docker-compose.yml",
    "requirements.txt",
    "requirements-dev.txt",
    ".releaserc",
    "setup.py",
    ".pre-commit-config.yaml",
    "healthcheck.sh",
]


def create_directories():
    """Create all required directories."""
    print("📁 Creating directory structure...")

    # Create main package directories
    for directory in PROJECT_STRUCTURE:
        path = Path(directory)
        path.mkdir(parents=True, exist_ok=True)
        (path / "__init__.py").touch()  # Ensure each directory is a Python package

    # Additional directories
    directories = [
        "tests",
        "examples",
        "docs",
        ".github/workflows",
        "scripts",
        "templates",
        "notebooks/research",
    ]

    for directory in directories:
        path = Path(directory)
        path.mkdir(parents=True, exist_ok=True)

    # Create README and other root files
    create_root_files()

    print("✅ Directory structure created")


def create_python_files():
    """Create all Python files with proper docstrings and structure."""
    print("📝 Generating Python files...")

    # Current year for license headers
    current_year = datetime.now().year

    # License header template
    license_header = f"""# Copyright {current_year} {AUTHOR}
#
# Licensed under the {LICENSE} License (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://opensource.org/licenses/{LICENSE}
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""

    # Create package files
    for directory, config in PROJECT_STRUCTURE.items():
        for filename in config["files"]:
            filepath = Path(directory) / filename

            # Skip if file exists
            if filepath.exists():
                continue

            # Create file with appropriate content
            with open(filepath, "w", encoding="utf-8") as f:
                # Add license header
                f.write(license_header)

                # Add module docstring
                if filename != "__init__.py":
                    f.write(
                        f'"""\n{config["description"]}\n\nFile: {filepath}\n"""\n\n'
                    )

                    # Add basic class/function template for non-empty files
                    if filename not in ["__init__.py"]:
                        module_name = filename[:-3]  # Remove .py
                        class_name = "".join(
                            word.capitalize() for word in module_name.split("_")
                        )

                        if filename in ["lexer.py", "parser.py"]:
                            f.write(
                                f'class {class_name}:\n    """{config["description"]}"""\n\n    def __init__(self):\n        pass\n'
                            )
                        elif filename.endswith("_adapter.py"):
                            f.write(
                                f'class {class_name}Adapter:\n    """Adapter for {module_name.replace("_", " ").title()} AI model."""\n\n    def __init__(self, api_key=None):\n        self.api_key = api_key\n'
                            )
                        elif filename.endswith("_preset.py"):
                            f.write(
                                '"""Preset configurations for different neurotypes."""\n\n'
                            )
                            f.write(
                                'NEURO_PRESETS = {\n    "dyslexia": {\n        "font": "opendyslexic",\n        "spacing": 1.2,\n        "colors": "dark_theme"\n    },\n    "adhd": {\n        "minimal_ui": True,\n        "focus_mode": True,\n        "distraction_free": True\n    }\n}\n'
                            )

    print("✅ Python files created with appropriate structure")


def create_example_files():
    """Create example HyperCode files."""
    print("\n📚 Creating example programs...")

    examples = {
        "examples/hello_world.hc": """; HyperCode: Hello World
; Print 'H' (ASCII 72)
++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
++++++++++
++
.
""",
        "examples/fibonacci.hc": """; HyperCode: Fibonacci Sequence
; Demonstrates loops and memory operations

; Initialize
>++++++++++
[
    <+++++++++++
    >-
]
<.
""",
    }

    for file_path, content in examples.items():
        path = Path(file_path)
        if not path.exists():
            path.write_text(content)
            print(f"   ✓ {file_path}")


def create_root_files():
    """Create root-level configuration files with appropriate content."""
    print("📄 Creating root configuration files...")

    # Create README.md
    readme_content = f"""# 🚀 {PROJECT_NAME}

{DESCRIPTION}

## ✨ Features

- **Neurodivergent-First Design**: Built with accessibility in mind
- **AI Compatibility**: Seamless integration with LLMs
- **Multi-Backend**: Compile to various targets (Python, JavaScript, WebAssembly, etc.)
- **Extensible**: Easy to add new language features and backends

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/welshDog/{PROJECT_NAME}.git
cd {PROJECT_NAME}

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the HyperCode REPL
python -m hypercode
```

## 📚 Documentation

Check out our [documentation](docs/README.md) for detailed usage instructions.

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the {LICENSE} License - see the [LICENSE](LICENSE) file for details.
"""

    # Create requirements.txt
    requirements_content = """# Core Dependencies
antlr4-python3-runtime>=4.13.1,<5.0.0
pydantic>=2.5.0,<3.0.0

# AI & LLM Integrations
openai>=1.3.5,<2.0.0
anthropic>=0.7.1,<1.0.0
mistralai>=0.0.11,<1.0.0
ollama>=0.1.0,<1.0.0

# Development
pytest>=7.4.0,<8.0.0
black>=23.7.0,<24.0.0
isort>=5.12.0,<6.0.0
mypy>=1.5.0,<2.0.0
flake8>=6.1.0,<7.0.0
"""

    # Create .gitignore
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
ENV/

# IDE
.idea/
.vscode/
*.swp
*.swo

# Logs
logs/
*.log

# Local development
.env
.env.local

# Build artifacts
build/
dist/
"""

    # Create setup.py
    setup_content = """\"\"\"
HyperCode: Neurodivergent-First Programming Language
with AI Compatibility & Forgotten Language Resurrection

Setup configuration for pip installation
\"\"\"

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="{PROJECT_NAME}",
    version="{VERSION}",
    author="{AUTHOR}",
    author_email="{AUTHOR_EMAIL}",
    description=(
        "A neurodivergent-first programming language "
        "with AI compatibility features"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/welshDog/{PROJECT_NAME}",
    packages=find_packages(exclude=["tests*"]),
    package_data={{"{PROJECT_NAME}": ["py.typed"]}},
    include_package_data=True,
    python_requires=">=3.10",
    install_requires=[
        "antlr4-python3-runtime>=4.13.1,<5.0.0",
        "pydantic>=2.5.0,<3.0.0",
    ],
    extras_require={{
        "dev": [
            "pytest>=7.4.0",
            "black>=23.7.0",
            "isort>=5.12.0",
            "mypy>=1.5.0",
            "flake8>=6.1.0",
        ],
        "ai": [
            "openai>=1.3.5",
            "anthropic>=0.7.1",
            "mistralai>=0.0.11",
            "ollama>=0.1.0",
        ],
    }},
    entry_points={{
        "console_scripts": [
            f"{PROJECT_NAME}={PROJECT_NAME}.cli:main",
        ],
    }},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Interpreters",
        "Typing :: Typed",
    ],
)
"""

    # Create files with content
    files_to_create = {
        "README.md": readme_content,
        "requirements.txt": requirements_content,
        ".gitignore": gitignore_content,
        "setup.py": setup_content,
        "LICENSE": f"""MIT License

Copyright (c) {datetime.now().year} {AUTHOR}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""",
        "pyproject.toml": r"""[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'

[tool.isort]
profile = "black"
line_length = 88

[tool.mypy]
python_version = "3.10"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
check_untyped_defs = true
no_implicit_optional = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
addopts = "-v --cov=hypercode --cov-report=term-missing"
""",
    }

    # Create each file with its content
    for filename, content in files_to_create.items():
        if not Path(filename).exists():
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)

    # Make setup.py executable
    if os.name != "nt":  # Not needed on Windows
        os.chmod("setup.py", os.stat("setup.py").st_mode | stat.S_IEXEC)

    print("✅ Root configuration files created")


def create_healthcheck():
    """Create the healthcheck script for Docker."""
    print("🔍 Creating healthcheck script...")

    scripts_dir = Path("scripts")
    scripts_dir.mkdir(exist_ok=True)

    healthcheck_path = scripts_dir / "healthcheck.sh"

    if not healthcheck_path.exists():
        healthcheck_content = """#!/bin/sh
# Health check for HyperCode services

# Exit immediately if a command exits with a non-zero status
set -e

# Check if the API server is running
if ! curl -sSf http://localhost:8000/health > /dev/null; then
    echo "Health check failed: API server is not responding"
    exit 1
fi

# Check if required services are running
# Example: Check if Redis is accessible
# if ! redis-cli ping > /dev/null; then
#     echo "Health check failed: Redis is not accessible"
#     exit 1
# fi

echo "All services are healthy"
exit 0
"""
        with open(healthcheck_path, "w", encoding="utf-8") as f:
            f.write(healthcheck_content)

        # Make the script executable (Unix-like systems)
        if os.name != "nt":
            healthcheck_path.chmod(0o755)

    print("✅ Healthcheck script created")


def print_summary():
    """Print summary of created structure."""
    print("\n✨ Project scaffolding complete! 🎉\n")

    # Project structure summary
    print("📁 Project Structure:")
    print("├── hypercode/               # Main package")
    for directory, config in PROJECT_STRUCTURE.items():
        print(f"│   ├── {directory.ljust(18)} # {config['description']}")

    # Additional directories
    print("├── tests/                  # Test suite")
    print("├── examples/               # Example HyperCode programs")
    print("├── docs/                   # Documentation")
    print("├── scripts/                # Utility scripts")
    print("└── .github/workflows/      # GitHub Actions workflows\n")

    # Next steps
    print("🚀 Next Steps:")
    print("1. Set up your development environment:")
    print("   python -m venv venv")
    print("   source venv/bin/activate  # On Windows: venv\\Scripts\\activate")
    print(
        "   pip install -e '.[dev,ai]'  # Install in development mode with all extras\n"
    )

    print("2. Run the tests:")
    print("   pytest -v\n")

    print("3. Start the development server:")
    print("   python -m hypercode.cli\n")

    print("4. Open your browser to http://localhost:8000\n")

    print("💡 Tip: Run 'make help' to see available development commands")
    print("🔧 Happy coding! 🚀\n")


def main():
    """Main scaffolding function."""
    try:
        print("🚀 Starting HyperCode project setup...\n")

        # Create the project structure
        create_directories()
        create_python_files()
        create_example_files()
        create_healthcheck()

        # Print success message and next steps
        print("\n" + "=" * 50)
        print("✅ Project setup completed successfully!")
        print("=" * 50 + "\n")

        print_summary()

        return 0
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled by user")
        return 1
    except Exception as e:
        print(f"\n❌ Error during setup: {str(e)}", file=sys.stderr)
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
