.PHONY: help install dev test lint format typecheck docs clean build publish docker-build docker-run

# Default target
help:
	@echo "Available targets:"
	@echo "  install     : Install package in development mode with all dependencies"
	@echo "  dev         : Install development dependencies and setup pre-commit"
	@echo "  test        : Run tests with coverage"
	@echo "  lint        : Run code linters"
	@echo "  format      : Format code"
	@echo "  typecheck   : Run static type checking"
	@echo "  docs-serve  : Serve documentation locally"
	@echo "  docs-build  : Build documentation"
	@echo "  clean       : Clean build artifacts and caches"
	@echo "  build       : Build source and wheel packages"
	@echo "  publish     : Publish package to PyPI (requires PYPI_TOKEN)"
	@echo "  docker-build: Build Docker image"
	@echo "  docker-run  : Run Docker container"

# Development
install:
	@echo "Installing in development mode..."
	pip install -e ".[dev]"

# Development setup
dev: install
	@echo "Setting up development environment..."
	pre-commit install

# Testing
test:
	@echo "Running tests with coverage..."
	pytest --cov=hypercode --cov-report=term-missing tests/ -v

# Linting
lint:
	@echo "Running linters..."
	ruff check hypercode/ tests/
	black --check hypercode/ tests/

# Formatting
format:
	@echo "Formatting code..."
	black hypercode/ tests/
	ruff --fix hypercode/ tests/

# Type checking
typecheck:
	@echo "Running type checking..."
	mypy hypercode/ tests/

# Documentation
docs-serve:
	@echo "Serving documentation..."
	mkdocs serve

docs-build:
	@echo "Building documentation..."
	mkdocs build

# Building
build:
	@echo "Building package..."
	python -m build

# Publishing
publish: build
	@echo "Publishing to PyPI..."
	python -m twine upload --skip-existing dist/*

# Docker
docker-build:
	@echo "Building Docker image..."
	docker build -t hypercode:latest .

docker-run:
	@echo "Running Docker container..."
	docker run -p 8000:8000 hypercode:latest

# Cleanup
clean:
	@echo "Cleaning up..."
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name "*.egg-info" -exec rm -r {} +
	rm -rf build/ dist/ .mypy_cache/ .pytest_cache/ .ruff_cache/ .coverage htmlcov/

# Check if requirements are up to date
check-deps:
	@echo "Checking for outdated dependencies..."
	pip list --outdated
