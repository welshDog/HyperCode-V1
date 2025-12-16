#!/usr/bin/env python3

"""
Project Organizer for HyperCode

A unified tool to organize both project files and documentation into a structured layout.
Features: Dry-run mode, file conflict handling, backup creation, validation, and colored output.
"""

import argparse
import logging
import shutil
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
    HAS_RICH = True
except ImportError:
    HAS_RICH = False

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("project_organizer.log"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)
console = Console() if HAS_RICH else None


class ProjectOrganizer:
    def __init__(self, dry_run: bool = False, create_backup: bool = False):
        self.base_dir = Path(__file__).parent.parent
        self.dry_run = dry_run
        self.create_backup = create_backup
        self.backup_dir = None
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
                "Github-Setup-Guide.md",
                "HyperCode-Build-Guide.md",
                "PERPLEXITY_SPACE_QUICKSTART.md",
                "RECIPES.md",
                "windsurf-pro-hacks.md",
            ],
            "reference": [
                "API_REFERENCE.md",
                "LANGUAGE_REFERENCE.md",
            ],
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

    def _log_colored(self, message: str, color: str = "white"):
        """Log with color support if rich is available."""
        if HAS_RICH and console:
            color_map = {
                "success": "green",
                "warning": "yellow",
                "error": "red",
                "info": "cyan",
            }
            console.print(f"[{color_map.get(color, color)}]{message}[/{color_map.get(color, color)}]")
        else:
            logger.info(message)

    def create_backup_of_files(self):
        """Create a timestamped backup before organization."""
        if self.dry_run or not self.create_backup:
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = self.base_dir / f"backups/org_backup_{timestamp}"

        try:
            backup_dir.mkdir(parents=True, exist_ok=True)
            self.backup_dir = backup_dir

            # Backup files that will be moved
            backed_up = 0
            for pattern, target_dir in self.file_mappings.items():
                for file_path in self.base_dir.glob(pattern):
                    if file_path.name not in self.exclude_files and file_path.parent != target_dir:
                        backup_path = backup_dir / file_path.name
                        shutil.copy2(file_path, backup_path)
                        backed_up += 1

            # Backup doc files
            for category, files in self.docs_structure.items():
                for doc_file in files:
                    src_path = self.base_dir / doc_file
                    if src_path.exists():
                        backup_path = backup_dir / doc_file
                        shutil.copy2(src_path, backup_path)
                        backed_up += 1

            self._log_colored(f"✓ Created backup with {backed_up} files: {backup_dir}", "success")
            logger.info(f"Backup created at: {backup_dir}")
        except Exception as e:
            self._log_colored(f"✗ Failed to create backup: {e}", "error")
            logger.error(f"Backup creation failed: {e}", exc_info=True)

    def _handle_conflict(self, target_path: Path) -> Path:
        """Handle file conflict by renaming with suffix."""
        if not target_path.exists():
            return target_path

        stem = target_path.stem
        suffix = target_path.suffix
        parent = target_path.parent
        counter = 1

        while True:
            new_name = f"{stem}_{counter}{suffix}"
            new_path = parent / new_name
            if not new_path.exists():
                self._log_colored(
                    f"⚠ File conflict: {target_path.name} already exists. Renaming to {new_name}",
                    "warning",
                )
                logger.warning(f"File conflict handled: {target_path} -> {new_path}")
                return new_path
            counter += 1

    def ensure_directories_exist(self):
        """Create all necessary directories if they don't exist."""
        for dir_path in self.dirs.values():
            try:
                dir_path.mkdir(parents=True, exist_ok=True)
                logger.info(f"Ensured directory exists: {dir_path}")
            except Exception as e:
                self._log_colored(f"✗ Failed to create directory {dir_path}: {e}", "error")
                logger.error(f"Failed to create directory {dir_path}: {e}")

    def organize_files(self):
        """Organize project files into their respective directories."""
        moved_files = {}
        skipped_files = []

        # Move files based on patterns
        for pattern, target_dir in self.file_mappings.items():
            for file_path in self.base_dir.glob(pattern):
                if file_path.name in self.exclude_files or file_path.parent == target_dir:
                    continue

                target_path = self._handle_conflict(target_dir / file_path.name)
                moved_files[str(file_path)] = str(target_path)

                if not self.dry_run:
                    try:
                        shutil.move(str(file_path), str(target_path))
                        self._log_colored(f"✓ Moved: {file_path.name} -> {target_path.name}", "success")
                        logger.info(f"Moved: {file_path} -> {target_path}")
                    except Exception as e:
                        self._log_colored(f"✗ Failed to move {file_path.name}: {e}", "error")
                        logger.error(f"Failed to move {file_path}: {e}")
                        skipped_files.append((str(file_path), str(e)))

        return moved_files, skipped_files

    def organize_docs(self):
        """Organize documentation files into categorized directories."""
        moved_docs = {}
        skipped_docs = []

        for category, files in self.docs_structure.items():
            category_dir = self.dirs["docs"] / category
            category_dir.mkdir(parents=True, exist_ok=True)

            for doc_file in files:
                src_path = self.base_dir / doc_file

                if not src_path.exists():
                    continue

                target_path = self._handle_conflict(category_dir / doc_file)
                moved_docs[str(src_path)] = str(target_path)

                if not self.dry_run:
                    try:
                        shutil.move(str(src_path), str(target_path))
                        self._log_colored(f"✓ Moved doc: {doc_file} -> {category}/", "success")
                        logger.info(f"Moved doc: {src_path} -> {target_path}")
                    except Exception as e:
                        self._log_colored(f"✗ Failed to move {doc_file}: {e}", "error")
                        logger.error(f"Failed to move {src_path}: {e}")
                        skipped_docs.append((str(src_path), str(e)))

        return moved_docs, skipped_docs

    def validate_structure(self) -> Dict[str, List[str]]:
        """Check which expected files are missing from docs structure."""
        missing_docs = {}

        for category, files in self.docs_structure.items():
            missing_in_category = []
            for doc_file in files:
                doc_path = self.base_dir / doc_file
                if not doc_path.exists():
                    missing_in_category.append(doc_file)
            if missing_in_category:
                missing_docs[category] = missing_in_category

        return missing_docs

    def generate_report(
        self,
        moved_files: Dict[str, str],
        skipped_files: List[Tuple[str, str]],
        moved_docs: Dict[str, str],
        skipped_docs: List[Tuple[str, str]],
        missing_docs: Optional[Dict[str, List[str]]] = None,
    ):
        """Generate a report of the organization process."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report = [
            "=" * 80,
            f"HyperCode Project Organization Report - {timestamp}",
            "=" * 80,
            "\n[SUMMARY]",
            f"\nFiles Moved: {len(moved_files)}",
            f"Files Skipped: {len(skipped_files)}",
            f"Documentation Files Moved: {len(moved_docs)}",
            f"Documentation Files Skipped: {len(skipped_docs)}",
        ]

        if missing_docs:
            total_missing = sum(len(docs) for docs in missing_docs.values())
            report.append(f"Missing Documentation Files: {total_missing}")

        report.append("\n[DETAILS]")

        # Add moved files details
        if moved_files:
            report.append("\nMOVED FILES:")
            for src, dest in moved_files.items():
                src_name = Path(src).name
                dest_name = Path(dest).name
                report.append(f"  {src_name} -> {dest_name}")

        # Add moved docs details
        if moved_docs:
            report.append("\nMOVED DOCUMENTATION:")
            for src, dest in moved_docs.items():
                src_name = Path(src).name
                dest_rel = Path(dest).relative_to(self.base_dir)
                report.append(f"  {src_name} -> docs/{dest_rel}")

        # Add skipped items
        if skipped_files:
            report.append("\nSKIPPED FILES:")
            for src, error in skipped_files:
                report.append(f"  {Path(src).name}: {error}")

        if skipped_docs:
            report.append("\nSKIPPED DOCUMENTATION:")
            for src, error in skipped_docs:
                report.append(f"  {Path(src).name}: {error}")

        # Add missing docs
        if missing_docs:
            report.append("\nMISSING DOCUMENTATION:")
            for category, files in missing_docs.items():
                report.append(f"  [{category}]")
                for file in files:
                    report.append(f"    - {file}")

        # Write report to file and console
        report_path = self.base_dir / "organization_report.txt"

        if not self.dry_run:
            with open(report_path, "w", encoding="utf-8") as f:
                f.write("\n".join(report))
            self._log_colored(f"✓ Report saved to: organization_report.txt", "success")
            logger.info(f"Organization report saved to: {report_path}")

        # Print report
        report_text = "\n".join(report)
        if HAS_RICH and console:
            console.print(Panel(report_text, title="[bold cyan]Organization Report[/bold cyan]"))
        else:
            print(report_text)


def main():
    parser = argparse.ArgumentParser(
        description="Organize HyperCode project files and documentation.",
        epilog="Examples:\n"
               "  python scripts/project_organizer.py              # Full organization\n"
               "  python scripts/project_organizer.py --dry-run    # Preview changes\n"
               "  python scripts/project_organizer.py --validate   # Check missing docs\n"
               "  python scripts/project_organizer.py --backup     # Create backup before organizing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate the organization without making changes",
    )
    parser.add_argument(
        "--skip-files",
        action="store_true",
        help="Skip file organization",
    )
    parser.add_argument(
        "--skip-docs",
        action="store_true",
        help="Skip documentation organization",
    )
    parser.add_argument(
        "--validate",
        action="store_true",
        help="Only validate the documentation structure (no organization)",
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Create a backup before organization",
    )

    args = parser.parse_args()

    organizer = ProjectOrganizer(dry_run=args.dry_run, create_backup=args.backup)

    if HAS_RICH:
        console.print("[cyan]🚀 HyperCode Project Organizer[/cyan]")
    else:
        logger.info("🚀 HyperCode Project Organizer")

    if args.dry_run:
        if HAS_RICH:
            console.print("[yellow]⚠ Running in dry-run mode. No changes will be made.[/yellow]")
        else:
            logger.info("Running in dry-run mode. No changes will be made.")

    try:
        # Validate only
        if args.validate:
            logger.info("Validating documentation structure...")
            missing = organizer.validate_structure()

            if not missing:
                if HAS_RICH:
                    console.print("[green]✓ All expected documentation files are present![/green]")
                else:
                    logger.info("✓ All expected documentation files are present!")
            else:
                if HAS_RICH:
                    console.print("[yellow]⚠ Missing documentation files:[/yellow]")
                else:
                    logger.warning("Missing documentation files:")

                for category, files in missing.items():
                    logger.warning(f"\n[{category}]")
                    for file in files:
                        logger.warning(f"  - {file}")
            return 0

        # Full organization
        organizer.ensure_directories_exist()

        moved_files = {}
        skipped_files = []
        moved_docs = {}
        skipped_docs = []

        # Create backup if requested
        if args.backup and not args.dry_run:
            organizer.create_backup_of_files()

        if not args.skip_files:
            logger.info("Starting file organization...")
            moved_files, skipped_files = organizer.organize_files()

        if not args.skip_docs:
            logger.info("Starting documentation organization...")
            moved_docs, skipped_docs = organizer.organize_docs()

        # Validate after organization
        missing_docs = organizer.validate_structure()

        organizer.generate_report(
            moved_files,
            skipped_files,
            moved_docs,
            skipped_docs,
            missing_docs if missing_docs else None,
        )

        if not args.dry_run:
            if HAS_RICH:
                console.print("[green]✓ Organization completed successfully![/green]")
            else:
                logger.info("✓ Organization completed successfully!")
        else:
            if HAS_RICH:
                console.print("[cyan]✓ Dry run completed. No changes were made.[/cyan]")
            else:
                logger.info("✓ Dry run completed. No changes were made.")

        return 0

    except Exception as e:
        logger.error(f"An error occurred during organization: {e}", exc_info=True)
        if HAS_RICH:
            console.print(f"[red]✗ An error occurred: {e}[/red]")
        return 1


if __name__ == "__main__":
    sys.exit(main())
