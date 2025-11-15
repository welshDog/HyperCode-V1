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
import sys
from pathlib import Path

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
    print("📁 Creating directories...")

    for dir_name in PROJECT_STRUCTURE:
        path = Path(dir_name)
        path.mkdir(parents=True, exist_ok=True)
        print(f"   ✓ {dir_name}/")


def create_python_files():
    """Create all Python files with proper __init__.py structure."""
    print("\n📝 Creating Python files...")

    for dir_name, info in PROJECT_STRUCTURE.items():
        for file_name in info["files"]:
            file_path = Path(dir_name) / file_name

            # Only create if it doesn't exist
            if not file_path.exists():
                file_path.write_text("")
                print(f"   ✓ {file_path}")


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
    """Create root-level configuration files as empty placeholders."""
    print("\n⚙️  Creating root configuration files...")

    for file_name in ROOT_FILES:
        file_path = Path(file_name)
        if not file_path.exists():
            file_path.write_text("")
            print(f"   ✓ {file_name}")


def create_healthcheck():
    """Create the healthcheck script for Docker."""
    print("\n🏥 Creating healthcheck script...")

    healthcheck_content = """#!/bin/bash
# HyperCode Docker Healthcheck
# Verifies that the HyperCode CLI is responsive

python -c "from core.cli import main; print('OK')" && exit 0 || exit 1
"""

    healthcheck_path = Path("healthcheck.sh")
    healthcheck_path.write_text(healthcheck_content)

    # Make executable on Unix systems
    if sys.platform != "win32":
        os.chmod(healthcheck_path, 0o755)

    print("   ✓ healthcheck.sh")


def print_summary():
    """Print summary of created structure."""
    print("\n" + "=" * 60)
    print("✅ PROJECT STRUCTURE CREATED SUCCESSFULLY!")
    print("=" * 60)

    print("\n📦 Created directories:")
    for dir_name, info in PROJECT_STRUCTURE.items():
        print(f"   • {dir_name}/ - {info['description']}")

    print("\n📄 Root configuration files:")
    for file_name in ROOT_FILES:
        print(f"   • {file_name}")

    print("\n🚀 Next steps:")
    print("   1. python -m venv .venv")
    print(
        "   2. source .venv/bin/activate  (or .venv\\\\Scripts\\\\activate on Windows)"
    )
    print("   3. pip install -r requirements-dev.txt")
    print("   4. pre-commit install")
    print("   5. python scaffold_content.py  (to fill in file content)")
    print("\n" + "=" * 60)


def main():
    """Main scaffolding function."""
    print("🚀 HyperCode Project Scaffolder")
    print("=" * 60)
    print()

    try:
        create_directories()
        create_python_files()
        create_example_files()
        create_root_files()
        create_healthcheck()
        print_summary()

        print("\n✨ Your HyperCode project is ready!")
        print("💪 Now go build something LEGENDARY! 👊")

        return 0

    except Exception as e:
        print(f"\n❌ Error during scaffolding: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
