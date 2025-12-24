.PHONY: test test-cov lint format typecheck clean help

# Development
install:
	@echo "Installing dependencies..."
	pip install -e ".[dev]"

# Testing
test:
	@echo "Running tests..."
	python -m pytest tests/ -v

test-cov:
	@echo "Running tests with coverage..."
	python -m pytest tests/ --cov=hypercode --cov-report=term-missing --cov-report=xml:coverage.xml --cov-report=html:htmlcov

# Linting and Formatting
lint:
	@echo "Running linters..."
	flake8 hypercode/ tests/
	black --check hypercode/ tests/
	isort --check-only hypercode/ tests/

format:
	@echo "Formatting code..."
	black hypercode/ tests/
	isort hypercode/ tests/

# Type Checking
typecheck:
	@echo "Running type checking..."
	mypy hypercode/ tests/

# Benchmarking
benchmark:
	@echo "Running HyperCode Benchmarks..."
	python core/src/ci_pipeline.py

# Cleaning
clean:
	@echo "Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	dirs_to_clean="build dist .pytest_cache .mypy_cache htmlcov .coverage coverage.xml"
	for dir in $$dirs_to_clean; do \
		rm -rf $$dir; \
	done

# Help
dev-setup: install test-cov lint typecheck

help:
	@echo "Available commands:"
	@echo "  make install    - Install development dependencies"
	@echo "  make test       - Run unit tests"
	@echo "  make test-cov   - Run tests with coverage reporting"
	@echo "  make lint       - Run code linters"
	@echo "  make format     - Format code"
	@echo "  make typecheck  - Run type checking"
	@echo "  make benchmark  - Run performance benchmarks"
	@echo "  make clean      - Clean temporary files"
	@echo "  make dev-setup  - Set up development environment (install + test + lint + typecheck)"
