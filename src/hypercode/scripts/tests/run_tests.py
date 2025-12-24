#!/usr/bin/env python3
"""
HyperCode Test Runner

This script provides a unified interface for running tests with coverage reporting
and other useful features.
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path


def run_tests(args):
    """Run pytest with the given arguments and coverage reporting."""
    # Get the project root directory
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)

    # Build the command
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "--cov=hypercode",
        "--cov-report=term-missing",
        "--cov-report=html",
        "-v",
    ]

    # Add any additional arguments
    if args.test_path:
        cmd.append(str(args.test_path))
    else:
        cmd.append("tests/")

    if args.fail_fast:
        cmd.append("--exitfirst")

    if args.verbose:
        cmd.append("-v")

    # Run the command
    return subprocess.call(cmd)


def main():
    """Parse command line arguments and run tests."""
    parser = argparse.ArgumentParser(
        description="Run HyperCode tests with coverage reporting."
    )
    parser.add_argument(
        "test_path", nargs="?", default=None, help="Path to test file or directory"
    )
    parser.add_argument(
        "--fail-fast", "-x", action="store_true", help="Stop after first failure"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Increase verbosity"
    )

    args = parser.parse_args()

    # Ensure the tests directory exists
    tests_dir = Path("tests")
    if not tests_dir.exists():
        print(f"Error: {tests_dir} directory not found.")
        return 1

    # Run the tests
    return run_tests(args)


if __name__ == "__main__":
    sys.exit(main())
