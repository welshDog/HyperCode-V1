#!/usr/bin/env python3
"""
Automated Testing Suite for DuelCode Framework
Tests tutorials against validation rules and checks framework integrity.
"""

import json
import subprocess
import sys
from dataclasses import asdict, dataclass
from enum import Enum
from pathlib import Path
from subprocess import CompletedProcess
from typing import Dict, List


class TestResult(Enum):
    PASSED = "PASSED"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


@dataclass
class TestCase:
    name: str
    file_path: str
    expected_errors: int = 0
    expected_warnings: int = 0
    expected_info: int = 0
    description: str = ""


@dataclass
class TestRun:
    test_case: TestCase
    result: TestResult
    actual_errors: int
    actual_warnings: int
    actual_info: int
    output: str
    duration: float


class DuelCodeTestSuite:
    def __init__(self, duelcode_dir: str = "DuelCode"):
        self.duelcode_dir = Path(duelcode_dir)
        self.test_results: List[TestRun] = []

    def discover_tutorials(self) -> List[Path]:
        """Find all tutorial markdown files."""
        tutorials: List[Path] = []
        for pattern in ["tutorial-*.md", "*tutorial*.md"]:
            tutorials.extend(self.duelcode_dir.glob(pattern))
        return sorted(tutorials)

    def run_validator(self, file_path: Path) -> CompletedProcess[str]:
        """Run the ultra validator on a file."""
        validator_path = self.duelcode_dir / "ultra_validator.py"
        cmd = [sys.executable, str(validator_path), str(file_path)]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return result
        except subprocess.TimeoutExpired:
            return subprocess.CompletedProcess(cmd, -1, "", "Validator timed out")
        except Exception as e:
            return subprocess.CompletedProcess(
                cmd, -1, "", f"Error running validator: {e}"
            )

    def parse_validator_output(self, output: str) -> Dict[str, int]:
        """Parse validator output to count issues by severity."""
        counts = {"errors": 0, "warnings": 0, "info": 0}

        for line in output.split("\n"):
            line = line.strip().upper()
            if "ERROR" in line and "ERRORS" in line:
                # Extract number from "ERRORS (X):"
                import re

                match = re.search(r"ERRORS\s*\((\d+)\)", line)
                if match:
                    counts["errors"] = int(match.group(1))
            elif "WARNING" in line and "WARNINGS" in line:
                import re

                match = re.search(r"WARNINGS\s*\((\d+)\)", line)
                if match:
                    counts["warnings"] = int(match.group(1))
            elif "INFO" in line and "INFO" in line:
                import re

                match = re.search(r"INFO\s*\((\d+)\)", line)
                if match:
                    counts["info"] = int(match.group(1))

        return counts

    def test_tutorial(self, tutorial_path: Path) -> TestRun:
        """Test a single tutorial file."""
        test_case = TestCase(
            name=tutorial_path.name,
            file_path=str(tutorial_path),
            description=f"Testing {tutorial_path.name}",
        )

        print(f"Testing: {test_case.name}...", end=" ")

        # Run validator
        import time

        start_time = time.time()
        result = self.run_validator(tutorial_path)
        duration = time.time() - start_time

        # Parse output
        counts = self.parse_validator_output(result.stdout)

        # Determine if test passed (no errors)
        test_result = TestResult.PASSED if counts["errors"] == 0 else TestResult.FAILED

        test_run = TestRun(
            test_case=test_case,
            result=test_result,
            actual_errors=counts["errors"],
            actual_warnings=counts["warnings"],
            actual_info=counts["info"],
            output=result.stdout,
            duration=duration,
        )

        print(f"{test_result.value} ({duration:.2f}s)")
        return test_run

    def test_validator_integrity(self) -> TestRun:
        """Test that validator itself is working correctly."""
        test_case = TestCase(
            name="Validator Integrity Test",
            file_path="self_test",
            description="Test validator can run without errors",
        )

        print("Testing validator integrity...", end=" ")

        try:
            # Test with a known good file
            good_file = self.duelcode_dir / "tutorial-01-hello-world.md"
            if not good_file.exists():
                test_result = TestResult.SKIPPED
                output = "No test file available"
            else:
                result = self.run_validator(good_file)
                if result.returncode == 0:
                    test_result = TestResult.PASSED
                    output = "Validator runs successfully"
                else:
                    test_result = TestResult.FAILED
                    output = result.stderr
        except Exception as e:
            test_result = TestResult.FAILED
            output = str(e)

        test_run = TestRun(
            test_case=test_case,
            result=test_result,
            actual_errors=0,
            actual_warnings=0,
            actual_info=0,
            output=output,
            duration=0,
        )

        print(test_result.value)
        return test_run

    def test_template_validity(self) -> List[TestRun]:
        """Test that templates pass validation."""
        template_runs = []
        templates = [
            self.duelcode_dir / "TEMPLATE-TUTORIAL-ADVANCED.md",
            self.duelcode_dir / "TEMPLATE-TUTORIAL-QUICK.md",
            self.duelcode_dir / "TEMPLATE-REFERENCE.md",
        ]

        for template in templates:
            if not template.exists():
                continue

            test_case = TestCase(
                name=f"Template Test: {template.name}",
                file_path=str(template),
                description=f"Testing template {template.name}",
            )

            print(f"Testing template: {template.name}...", end=" ")

            # Templates should have minimal issues (mostly info/suggestions)
            result = self.run_validator(template)
            counts = self.parse_validator_output(result.stdout)

            # Templates pass if no errors (warnings/info are OK for templates)
            test_result = (
                TestResult.PASSED if counts["errors"] == 0 else TestResult.FAILED
            )

            test_run = TestRun(
                test_case=test_case,
                result=test_result,
                actual_errors=counts["errors"],
                actual_warnings=counts["warnings"],
                actual_info=counts["info"],
                output=result.stdout,
                duration=0,
            )

            print(test_result.value)
            template_runs.append(test_run)

        return template_runs

    def run_all_tests(self) -> None:
        """Run the complete test suite."""
        print("=" * 60)
        print("DuelCode Framework Test Suite")
        print("=" * 60)

        # Test validator integrity
        self.test_results.append(self.test_validator_integrity())

        # Test templates
        self.test_results.extend(self.test_template_validity())

        # Test all tutorials
        tutorials = self.discover_tutorials()
        if not tutorials:
            print("No tutorial files found!")
            return

        print(f"\nFound {len(tutorials)} tutorial(s)")
        print("-" * 40)

        for tutorial in tutorials:
            self.test_results.append(self.test_tutorial(tutorial))

        # Generate report
        self.generate_report()

    def generate_report(self) -> None:
        """Generate a detailed test report."""
        print("\n" + "=" * 60)
        print("TEST REPORT")
        print("=" * 60)

        passed = sum(1 for r in self.test_results if r.result == TestResult.PASSED)
        failed = sum(1 for r in self.test_results if r.result == TestResult.FAILED)
        skipped = sum(1 for r in self.test_results if r.result == TestResult.SKIPPED)
        total = len(self.test_results)

        print(f"Total Tests: {total}")
        print(f"Passed: {passed} ✅")
        print(f"Failed: {failed} ❌")
        print(f"Skipped: {skipped} ⏭️")
        print(f"Success Rate: {(passed/total*100):.1f}%")

        if failed > 0:
            print("\nFAILED TESTS:")
            print("-" * 40)
            for result in self.test_results:
                if result.result == TestResult.FAILED:
                    print(f"❌ {result.test_case.name}")
                    print(f"   Errors: {result.actual_errors}")
                    print(f"   Warnings: {result.actual_warnings}")
                    if result.output:
                        print(f"   Details: {result.output[:100]}...")

        # Save detailed report
        report_data = {
            "summary": {
                "total": total,
                "passed": passed,
                "failed": failed,
                "skipped": skipped,
                "success_rate": passed / total * 100,
            },
            "tests": [asdict(r) for r in self.test_results],
        }

        report_file = self.duelcode_dir / "test-report.json"
        with Path(report_file).open("w", encoding="utf-8") as f:
            json.dump(report_data, f, indent=2, default=str)

        print(f"\nDetailed report saved to: {report_file}")


def main() -> None:
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="DuelCode Framework Test Suite")
    parser.add_argument(
        "--duelcode-dir", default="DuelCode", help="Path to DuelCode directory"
    )
    parser.add_argument("--file", help="Test specific file only")

    args = parser.parse_args()

    suite = DuelCodeTestSuite(args.duelcode_dir)

    if args.file:
        # Test single file
        file_path = Path(args.file)
        if file_path.exists():
            result = suite.test_tutorial(file_path)
            suite.test_results = [result]
            suite.generate_report()
        else:
            print(f"File not found: {args.file}")
            sys.exit(1)
    else:
        # Run full suite
        suite.run_all_tests()

    # Exit with error code if any tests failed
    failed_count = sum(1 for r in suite.test_results if r.result == TestResult.FAILED)
    sys.exit(1 if failed_count > 0 else 0)


if __name__ == "__main__":
    main()
