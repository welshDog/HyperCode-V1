"""
HyperCode: Neurodivergent-First Programming Language
with AI Compatibility & Forgotten Language Resurrection

Setup configuration for pip installation
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read version from __init__.py
version = "0.1.0"  # Beta: Week 1 - Lexer + Parser

setup(
    name="hypercode",
    version=version,
    author="welshDog (Lyndz Williams)",
    author_email="hello@hypercode.dev",
    description="Neurodivergent-first programming language with universal AI compatibility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/welshDog/hypercode",
    project_urls={
        "Bug Tracker": "https://github.com/welshDog/hypercode/issues",
        "Documentation": "https://github.com/welshDog/hypercode/tree/main/docs",
        "Source Code": "https://github.com/welshDog/hypercode",
        "Changelog": "https://github.com/welshDog/hypercode/blob/main/CHANGELOG.md",
    },
    license="MIT",
    packages=find_packages(exclude=["tests", "docs", "examples"]),
    python_requires=">=3.10",
    
    # Production dependencies
    install_requires=[
        # Core language & compilation
        "antlr4-python3-runtime==4.13.1",
        "pydantic==2.5.0",
        
        # AI & LLM
        "openai==1.3.5",
        "anthropic==0.7.1",
        "mistralai==0.0.11",
        "ollama==0.1.0",
        
        # Vector databases & RAG
        "langchain==0.1.3",
        "pinecone-client==3.0.0",
        
        # Web scraping
        "requests==2.31.0",
        "beautifulsoup4==4.12.2",
        "aiohttp==3.9.1",
        
        # Semantic web
        "rdflib==7.0.0",
        
        # Utilities
        "python-dotenv==1.0.0",
        "click==8.1.7",
        "rich==13.7.0",
        "pyyaml==6.0.1",
    ],
    
    # Development dependencies (for `pip install -e ".[dev]"`)
    extras_require={
        "dev": [
            # Testing
            "pytest==7.4.3",
            "pytest-cov==4.1.0",
            "pytest-asyncio==0.21.1",
            
            # Code quality
            "black==23.12.1",
            "flake8==6.1.0",
            "mypy==1.7.1",
            "pylint==3.0.3",
            "isort==5.13.2",
            
            # Pre-commit
            "pre-commit==3.5.0",
            
            # Documentation
            "sphinx==7.2.6",
            "sphinx-rtd-theme==2.0.0",
            
            # Dev tools
            "ipython==8.17.2",
            "jupyter==1.0.0",
        ],
        "docs": [
            "sphinx==7.2.6",
            "sphinx-rtd-theme==2.0.0",
            "myst-parser==2.0.0",
        ],
    },
    
    # Entry points (CLI commands)
    entry_points={
        "console_scripts": [
            "hypercode=core.cli:main",
        ],
    },
    
    # Metadata
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Languages",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Environment :: Console",
    ],
    
    keywords=[
        "programming-language",
        "compiler",
        "interpreter",
        "neurodivergent",
        "accessibility",
        "ai",
        "machine-learning",
        "esoteric-language",
        "brainfuck",
        "befunge",
    ],
    
    # Package data
    package_data={
        "hypercode": [
            "*.yml",
            "*.yaml",
            "*.json",
        ],
    },
    
    # Include non-Python files
    include_package_data=True,
    
    # Zip safe (can be installed in a zip file)
    zip_safe=False,
)
