.PHONY: benchmark test clean help

benchmark:
	@echo "Running HyperCode Benchmarks..."
	python core/src/ci_pipeline.py

test:
	@echo "Running Tests..."
	python -m pytest

clean:
	@echo "Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

help:
	@echo "Available commands:"
	@echo "  make benchmark  - Run performance benchmarks"
	@echo "  make test       - Run unit tests"
	@echo "  make clean      - Clean temporary files"
