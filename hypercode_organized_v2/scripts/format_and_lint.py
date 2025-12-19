#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path


def run_command(command, description):
    print(f"\n{description}...")
    print(f"Running: {command}")
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.stdout:
            print("Output:", result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)

        if result.returncode != 0:
            print(f"Warning during {description.lower()}, continuing...")
            return False
        return True
    except Exception as e:
        print(f"Error during {description.lower()}: {e}")
        return False


def main():
    success = True

    # Run black
    if not run_command(
        "python -m black --line-length=88 --target-version=py38 --exclude='.*\\.ipynb$' .",
        "Running Black",
    ):
        success = False

    # Run isort
    if not run_command(
        "python -m isort --profile=black --line-length=88 .", "Running isort"
    ):
        success = False

    # Run flake8, but don't fail the entire process if it finds issues
    if not run_command(
        "python -m flake8 --max-line-length=88 --extend-ignore=E203,W503 .",
        "Running flake8",
    ):
        print("Note: Flake8 found some issues that need attention")
        success = False

    if success:
        print("\n✅ All checks completed successfully!")
    else:
        print("\n⚠️  Some checks had issues. Please review the output above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
