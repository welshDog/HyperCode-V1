#!/usr/bin/env python3
"""
Project Organizer for HyperCode

A unified tool to organize both project files and documentation into a structured layout.
"""

import argparse
import logging
import shutil
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("project_organizer.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


class ProjectOrganizer:
    def __init__(self, dry_run: bool = False):
        self.base_dir = Path(__file__).parent.parent
        self.dry_run = dry_run
        self.setup_paths()

    def setup_paths(self):
        """Initialize all necessary directory paths."""
        self.dirs = {
            "src": self.base_dir / "src",
            "docs": self.base_dir / "docs",
            "tests": self.base_dir / "tests",
            "examples": self.base_dir / "examples",
            "config": self.base_dir / "config",
            "scripts": self.base_dir / "scripts",
            "ai_gateway": self.base_dir / "src" / "ai_gateway",
            "duelcode": self.base_dir / "src" / "duelcode",
            "spatial_visualizer": self.base_dir / "src" / "spatial_visualizer",
            "unit_tests": self.base_dir / "tests" / "unit",
            "integration_tests": self.base_dir / "tests" / "integration",
        }

        # Documentation categories
        self.docs_structure = {
            "getting-started": [
                "QUICK_START.md",
                "START-HERE.md",
                "INSTALL.md",
                "Dev-Setup-Guide.md",
                "Developer-Quickstart.md",
                "quickstart-checklist.md",
                "Week1-Sprint-Guide.md",
                "Week-1-Daily-Checklist.md",
                "Daily-Checklist.md",
                "LAUNCH_GUIDE.md",
                "LAUNCH-EXECUTION-PLAN.md",
                "LAUNCH_STRATEGY_V1.md",
                "PHASE1_LAUNCH_CHECKLIST.md",
            ],
            "guides": [
                "AI_INTEGRATION_GUIDE.md",
                "BETA_TESTER_GUIDE.md",
                "LINTER_FIX_GUIDE.md",
                "TROUBLESHOOTING.md",
                "TUTORIAL.md",
                "VIDEO_SCRIPTS.md",
                "GitHub-Setup-Guide.md",
                "HyperCode-Build-Guide.md",
                "PERPLEXITY_SPACE_QUICKSTART.md",
                "RECIPES.md",
                "windsurf-pro-hacks.md",
            ],
            "reference": ["API_REFERENCE.md", "LANGUAGE_REFERENCE.md"],
        }

        # File type mappings
        self.file_mappings = {
            "test_*.py": self.dirs["unit_tests"],
            "*.md": self.dirs["docs"],
            "*.txt": self.dirs["docs"],
            "*.yaml": self.dirs["config"],
            "*.yml": self.dirs["config"],
            "*.json": self.dirs["config"],
            "*.toml": self.dirs["config"],
        }

        # Files to exclude from moving
        self.exclude_files = {
            "README.md",
            "CONTRIBUTING.md",
            "CODE_OF_CONDUCT.md",
            "LICENSE",
            "pyproject.toml",
            "pytest.ini",
            "setup.cfg",
        }

    def ensure_directories_exist(self):
        """Create all necessary directories if they don't exist."""
        for dir_path in self.dirs.values():
            try:
                dir_path.mkdir(parents=True, exist_ok=True)
                logger.info(f"Ensured directory exists: {dir_path}")
            except Exception as e:
                logger.error(f"Failed to create directory {dir_path}: {e}")

    def organize_files(self):
        """Organize project files into their respective directories."""
        moved_files = {}
        skipped_files = []

        # Move files based on patterns
        for pattern, target_dir in self.file_mappings.items():
            for file_path in self.base_dir.glob(pattern):
                if (
                    file_path.name in self.exclude_files
                    or file_path.parent == target_dir
                ):
                    continue

                target_path = target_dir / file_path.name
                moved_files[str(file_path)] = str(target_path)

                if not self.dry_run:
                    try:
                        shutil.move(str(file_path), str(target_path))
                        logger.info(f"Moved: {file_path} -> {target_path}")
                    except Exception as e:
                        logger.error(f"Failed to move {file_path}: {e}")
                        skipped_files.append((str(file_path), str(e)))

        return moved_files, skipped_files

    def organize_docs(self):
        """Organize documentation files into categorized directories."""
        moved_docs = {}
        skipped_docs = []

        for category, files in self.docs_structure.items():
            category_dir = self.dirs["docs"] / category
            category_dir.mkdir(exist_ok=True)

            for doc_file in files:
                src_path = self.base_dir / doc_file
                if not src_path.exists():
                    continue

                target_path = category_dir / doc_file
                moved_docs[str(src_path)] = str(target_path)

                if not self.dry_run:
                    try:
                        shutil.move(str(src_path), str(target_path))
                        logger.info(f"Moved doc: {src_path} -> {target_path}")
                    except Exception as e:
                        logger.error(f"Failed to move {src_path}: {e}")
                        skipped_docs.append((str(src_path), str(e)))

        return moved_docs, skipped_docs

    def generate_report(
        self,
        moved_files: Dict[str, str],
        skipped_files: List[Tuple[str, str]],
        moved_docs: Dict[str, str],
        skipped_docs: List[Tuple[str, str]],
    ):
        """Generate a report of the organization process."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report = [
            "=" * 80,
            f"HyperCode Project Organization Report - {timestamp}",
            "=" * 80,
            "\n[SUMMARY]",
        ]

        # Add files summary
        report.extend(
            [
                f"\nFiles Moved: {len(moved_files)}",
                f"Files Skipped: {len(skipped_files)}",
                f"Documentation Files Moved: {len(moved_docs)}",
                f"Documentation Files Skipped: {len(skipped_docs)}",
                "\n[DETAILS]",
            ]
        )

        # Add moved files details
        if moved_files:
            report.append("\nMOVED FILES:")
            for src, dest in moved_files.items():
                report.append(f"  {src} -> {dest}")

        # Add moved docs details
        if moved_docs:
            report.append("\nMOVED DOCUMENTATION:")
            for src, dest in moved_docs.items():
                report.append(f"  {src} -> {dest}")

        # Add skipped items
        if skipped_files:
            report.append("\nSKIPPED FILES:")
            for src, error in skipped_files:
                report.append(f"  {src}: {error}")

        if skipped_docs:
            report.append("\nSKIPPED DOCUMENTATION:")
            for src, error in skipped_docs:
                report.append(f"  {src}: {error}")

        # Write report to file and console
        report_path = self.base_dir / "organization_report.txt"
        if not self.dry_run:
            with open(report_path, "w", encoding="utf-8") as f:
                f.write("\n".join(report))
            logger.info(f"Organization report saved to: {report_path}")

        print("\n".join(report))


def main():
    parser = argparse.ArgumentParser(
        description="Organize HyperCode project files and documentation."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate the organization without making changes",
    )
    parser.add_argument(
        "--skip-files", action="store_true", help="Skip file organization"
    )
    parser.add_argument(
        "--skip-docs", action="store_true", help="Skip documentation organization"
    )

    args = parser.parse_args()

    organizer = ProjectOrganizer(dry_run=args.dry_run)

    if args.dry_run:
        logger.info("Running in dry-run mode. No changes will be made.")

    try:
        organizer.ensure_directories_exist()

        moved_files = {}
        skipped_files = []
        moved_docs = {}
        skipped_docs = []

        if not args.skip_files:
            logger.info("Starting file organization...")
            moved_files, skipped_files = organizer.organize_files()

        if not args.skip_docs:
            logger.info("Starting documentation organization...")
            moved_docs, skipped_docs = organizer.organize_docs()

        organizer.generate_report(moved_files, skipped_files, moved_docs, skipped_docs)

        if not args.dry_run:
            logger.info("Organization completed successfully!")
        else:
            logger.info("Dry run completed. No changes were made.")

    except Exception as e:
        logger.error(f"An error occurred during organization: {e}", exc_info=True)
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
