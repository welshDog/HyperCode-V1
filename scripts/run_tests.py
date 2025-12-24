#!/usr/bin/env python3
"""
Test runner script for Hypercode.

This script runs the test suite with coverage reporting.
"""

import sys
from pathlib import Path

import coverage
import pytest


def run_tests():
    """Run the test suite with coverage reporting."""
    # Get the project root directory
    project_root = Path(__file__).parent.absolute()

    # Configure coverage
    cov = coverage.Coverage(
        source=["hypercode"],
        omit=[
            "*/tests/*",
            "*/__pycache__/*",
            "*/venv/*",
            "*/site-packages/*",
        ],
    )

    # Start coverage
    cov.start()

    # Run pytest
    test_args = [
        "--verbose",
        "--color=yes",
        "--cov=hypercode",
        "--cov-report=term-missing",
        "--cov-report=xml:coverage.xml",
        "--cov-report=html:htmlcov",
        "tests/",
    ]

    exit_code = pytest.main(test_args)

    # Stop coverage and save the data
    cov.stop()
    cov.save()

    # Generate reports
    cov.report()
    cov.html_report(directory="htmlcov")
    cov.xml_report(outfile="coverage.xml")

    sys.exit(exit_code)


if __name__ == "__main__":
    run_tests()
