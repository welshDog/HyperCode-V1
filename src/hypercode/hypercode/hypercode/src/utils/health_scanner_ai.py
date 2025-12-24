#!/usr/bin/env python3
"""
HyperCode Health Scanner with Perplexity AI Integration
Uses Perplexity API to analyze project health and provide intelligent recommendations
"""

import json
import sys
from pathlib import Path
from typing import Dict

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from hypercode.perplexity_client import PerplexityClient


class HealthScannerAI:
    """AI-powered health scanner for HyperCode project"""

    def __init__(self):
        self.perplexity = PerplexityClient()
        self.health_scan_results = {}

    def analyze_project_structure(self) -> Dict:
        """Analyze project structure and identify health issues"""
        print("Analyzing project structure...")

        base_path = Path(".")
        analysis = {
            "structure_score": 0,
            "issues": [],
            "recommendations": [],
            "files_analyzed": 0,
        }

        # Check for essential files
        essential_files = [
            "README.md",
            "pyproject.toml",
            "requirements.txt",
            ".gitignore",
            "LICENSE",
            "CONTRIBUTING.md",
        ]

        for file in essential_files:
            if (base_path / file).exists():
                analysis["structure_score"] += 10
            else:
                analysis["issues"].append(f"Missing essential file: {file}")
                analysis["recommendations"].append(f"Create {file}")

        # Analyze directory structure
        important_dirs = ["src", "tests", "docs", ".github"]
        for dir_name in important_dirs:
            if (base_path / dir_name).exists() and (base_path / dir_name).is_dir():
                analysis["structure_score"] += 5
            else:
                analysis["issues"].append(f"Missing important directory: {dir_name}")

        # Count Python files
        py_files = list(base_path.rglob("*.py"))
        analysis["files_analyzed"] = len(py_files)

        return analysis

    def analyze_dependencies(self) -> Dict:
        """Analyze dependency management"""
        print("Analyzing dependencies...")

        analysis = {
            "dependency_score": 0,
            "issues": [],
            "recommendations": [],
            "dependencies_found": [],
        }

        # Check pyproject.toml
        pyproject_path = Path("pyproject.toml")
        if pyproject_path.exists():
            try:
                with open(pyproject_path, "r") as f:
                    content = f.read()
                    if "dependencies = [" in content:
                        analysis["dependency_score"] += 20
                    else:
                        analysis["issues"].append(
                            "Dependencies not properly defined in pyproject.toml"
                        )
                        analysis["recommendations"].append(
                            "Add explicit dependencies to pyproject.toml"
                        )
            except Exception as e:
                analysis["issues"].append(f"Error reading pyproject.toml: {e}")
        else:
            analysis["issues"].append("No pyproject.toml found")
            analysis["recommendations"].append(
                "Create pyproject.toml with proper dependencies"
            )

        # Check requirements files
        req_files = ["requirements.txt", "requirements-dev.txt"]
        for req_file in req_files:
            if Path(req_file).exists():
                analysis["dependency_score"] += 10

        return analysis

    def analyze_security(self) -> Dict:
        """Analyze security configuration"""
        print("Analyzing security setup...")

        analysis = {"security_score": 0, "issues": [], "recommendations": []}

        # Check for security files
        security_files = [
            ".github/workflows/ci.yml",
            ".github/dependabot.yml",
            "SECURITY.md",
            ".env.example",
        ]

        for sec_file in security_files:
            if Path(sec_file).exists():
                analysis["security_score"] += 10
            else:
                analysis["issues"].append(f"Missing security configuration: {sec_file}")
                analysis["recommendations"].append(f"Create {sec_file}")

        # Check .env file is not committed
        if Path(".env").exists():
            with open(".gitignore", "r") as f:
                gitignore_content = f.read()
                if ".env" in gitignore_content:
                    analysis["security_score"] += 15
                else:
                    analysis["issues"].append(".env file not in .gitignore")
                    analysis["recommendations"].append("Add .env to .gitignore")

        return analysis

    def get_ai_recommendations(self, health_data: Dict) -> str:
        """Get AI-powered recommendations based on health scan"""
        print("Getting AI recommendations from Perplexity...")

        prompt = f"""
        You are an expert software development consultant analyzing the HyperCode project health.

        Based on this health scan data, provide specific, actionable recommendations:

        {json.dumps(health_data, indent=2)}

        Focus on:
        1. Critical issues that need immediate attention
        2. Medium-term improvements for project health
        3. Long-term strategic recommendations
        4. Prioritization of tasks based on impact vs effort

        Provide recommendations in a clear, structured format with specific file paths and actions.
        """

        response = self.perplexity.query(prompt)

        if "choices" in response and response["choices"]:
            return response["choices"][0]["message"]["content"]
        else:
            return "Failed to get AI recommendations"

    def run_full_scan(self) -> Dict:
        """Run complete health scan with AI analysis"""
        print("Starting HyperCode Health Scan with AI Analysis...")
        print("=" * 60)

        # Run analyses
        structure_analysis = self.analyze_project_structure()
        dependency_analysis = self.analyze_dependencies()
        security_analysis = self.analyze_security()

        # Compile results
        health_data = {
            "project_structure": structure_analysis,
            "dependencies": dependency_analysis,
            "security": security_analysis,
            "overall_score": (
                structure_analysis["structure_score"]
                + dependency_analysis["dependency_score"]
                + security_analysis["security_score"]
            ),
        }

        # Get AI recommendations
        ai_recommendations = self.get_ai_recommendations(health_data)

        # Final report
        report = {
            "scan_timestamp": str(Path.cwd()),
            "health_data": health_data,
            "ai_recommendations": ai_recommendations,
            "summary": {
                "overall_score": health_data["overall_score"],
                "total_issues": len(
                    structure_analysis["issues"]
                    + dependency_analysis["issues"]
                    + security_analysis["issues"]
                ),
                "critical_areas": [],
            },
        }

        # Identify critical areas
        if structure_analysis["structure_score"] < 30:
            report["summary"]["critical_areas"].append("Project Structure")
        if dependency_analysis["dependency_score"] < 20:
            report["summary"]["critical_areas"].append("Dependency Management")
        if security_analysis["security_score"] < 30:
            report["summary"]["critical_areas"].append("Security Configuration")

        return report

    def save_report(self, report: Dict, filename: str = "health_scan_report.json"):
        """Save health scan report to file"""
        with open(filename, "w") as f:
            json.dump(report, f, indent=2)
        print(f"Health scan report saved to {filename}")

    def print_summary(self, report: Dict):
        """Print a summary of the health scan"""
        print("\n" + "=" * 60)
        print("HYPERCODE HEALTH SCAN SUMMARY")
        print("=" * 60)

        summary = report["summary"]
        print(f"Overall Score: {summary['overall_score']}/100")
        print(f"Total Issues Found: {summary['total_issues']}")

        if summary["critical_areas"]:
            print(f"Critical Areas: {', '.join(summary['critical_areas'])}")
        else:
            print("Critical Areas: None - Good job!")

        print("\nAI RECOMMENDATIONS:")
        print("-" * 40)
        print(report["ai_recommendations"])


def main():
    """Main function to run the health scanner"""
    scanner = HealthScannerAI()

    # Run the scan
    report = scanner.run_full_scan()

    # Save and display results
    scanner.save_report(report)
    scanner.print_summary(report)

    print("\n[SUCCESS] Health scan completed!")


if __name__ == "__main__":
    main()
