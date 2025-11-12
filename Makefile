.PHONY: test lint format typecheck docs clean

# Development
install:
	pip install -e ".[dev]"

test:
	pytest tests/ -v

lint:
	ruff check hypercode/ tests/
	black --check hypercode/ tests/

format:
	black hypercode/ tests/
	ruff --fix hypercode/ tests/

typecheck:
	mypy hypercode/ tests/

# Documentation
docs-serve:
	mkdocs serve

docs-build:
	mkdocs build

# Cleanup
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name "*.egg-info" -exec rm -r {} +
	rm -rf build/ dist/ .mypy_cache/ .pytest_cache/ .ruff_cache/
