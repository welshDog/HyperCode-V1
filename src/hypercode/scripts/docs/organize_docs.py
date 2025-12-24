#!/usr/bin/env python3
"""
Documentation Organization Script for HyperCode

This script helps organize documentation files into a structured directory layout.
"""

import os
import shutil
from datetime import datetime
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent.parent
DOCS_DIR = BASE_DIR / "docs"
ROOT_DIR = BASE_DIR  # Directory where the files are currently located

# New documentation structure
NEW_STRUCTURE = {
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
    "reference": [
        "API_REFERENCE.md",
        "LANGUAGE_REFERENCE.md",
        "LANGUAGE_SPEC.md",
        "One_Page_Reference.md",
        "Design_Patterns_Examples.md",
        "DESIGN_PRINCIPLES.md",
        "BEST_PRACTICES.md",
        "STYLE_GUIDE_DRAFT.md",
        "hypercode_syntax.md",
        "hypercode_visual_syntax.md",
        "HyperCode_Design_Specs.md",
    ],
    "concepts": [
        "0-vision.md",
        "VISION.md",
        "HyperCode-Manifesto.md",
        "HyperCode_NeuroFirst_Design.md",
        "HyperCode-Visual-Manifesto.md",
        "HyperCode-Research-Foundation.md",
        "hypercode_research.md",
        "hypercode_ai_research.md",
        "HyperCode-AI-Research.md",
        "quantum_dna_research.md",
        "HyperCode_Esoteric_Study.md",
        "HyperCode-Esolang-Deep-Research.md",
    ],
    "roadmaps": [
        "1-roadmap.md",
        "ROADMAP.md",
        "2-backlog.md",
        "AI_OPTIMIZATION_ROADMAP.md",
        "implementation-roadmap.md",
        "HyperCode-90day.md",
        "HyperCode_V3_Build_Blueprint.md",
    ],
    "architecture": [
        "ARCHITECTURE.md",
        "hypercode_architecture.md",
        "hypercode-infrastructure.md",
        "hypercode-implementation-guide.md",
        "HyperCode_Implementation_Guide.md",
        "hypercode_impl.md",
        "hypercode-complete-system.md",
        "knowledge-base-architecture.md",
    ],
    "ai": [
        "AI_COMPAT.md",
        "AI_DUELCORE_DEEP_DIVE.md",
        "AI_UPGRADE_TASKS.md",
        "HyperCode-AI-Compat-Benchmark.md",
        "HyperCode-Plugin-Deep-Dive.md",
        "HyperCode_V3_Unified_Specification.md",
    ],
    "database": [
        "HYPER_DATABASE.md",
        "hyper-database-integration.md",
        "hyper-database-setup.md",
        "knowledge-base.md",
    ],
    "community": [
        "CONTRIBUTING.md",
        "BOUNTIES.md",
        "FAQ.md",
        "LAUNCH_ANNOUNCEMENT.md",
        "LAUNCH_TWEETS.md",
        "RELEASE_NOTES.md",
        "RELEASE-NOTES-v1.0.md",
        "RELEASE_NOTES_V1.0.md",
        "ANNOUNCEMENT-v1.0.md",
        "STATUS.md",
        "SPRINT_1_STATUS.md",
        "technical-status-report.md",
        "TECHNICAL_STATUS_REPORT.md",
        "dev-playtest-report.md",
        "RESEARCH-INTEGRATION.md",
        "RESEARCH-DRIVEN-IMPROVEMENT-ROADMAP.md",
        "GRANTS-AND-FUNDING.md",
        "HyperCode-Social-Impact-Strategy.md",
    ],
}


def setup_directories():
    """Create the new documentation directory structure."""
    for directory in NEW_STRUCTURE.keys():
        os.makedirs(DOCS_DIR / directory, exist_ok=True)
    print("✅ Created documentation directory structure")


def move_files():
    """Move files to their new locations based on the mapping."""
    moved_files = {}
    skipped_files = set()

    # First, collect all files that should be moved
    for target_dir, files in NEW_STRUCTURE.items():
        for file in files:
            src = ROOT_DIR / file
            if src.exists():
                dest_dir = DOCS_DIR / target_dir
                dest_dir.mkdir(
                    parents=True, exist_ok=True
                )  # Ensure target directory exists
                dest = dest_dir / file

                # Skip if source and destination are the same
                if str(src.resolve()) != str(dest.resolve()):
                    shutil.move(str(src), str(dest))
                    moved_files[str(dest)] = str(src)
                else:
                    skipped_files.add(f"{file} (already in correct location)")
            else:
                skipped_files.add(file)

    # Handle files that weren't in our mapping
    for item in DOCS_DIR.glob("*"):
        if item.is_file() and item.name not in [".gitkeep", "README.md"]:
            if item.name not in [f for files in NEW_STRUCTURE.values() for f in files]:
                skipped_files.add(item.name)

    return moved_files, sorted(skipped_files)


def generate_report(moved_files, skipped_files):
    """Generate a migration report."""
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = DOCS_DIR / f"docs_migration_report_{timestamp}.md"

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Documentation Migration Report\n\n")
        f.write(f"Generated on: {datetime.now().isoformat()}\n\n")

        f.write("## Moved Files\n\n")
        if moved_files:
            f.write("| New Location | Original Location |\n")
            f.write("|--------------|-------------------|\n")
            for dest, src in sorted(moved_files.items()):
                f.write(f"| `{dest}` | `{src}` |\n")
        else:
            f.write("No files were moved.\n")

        f.write("\n## Skipped Files\n\n")
        if skipped_files:
            f.write(
                "The following files were not moved and may need manual organization:\n\n"
            )
            for file in skipped_files:
                f.write(f"- `{file}`\n")
        else:
            f.write("All files were successfully moved.\n")

    print(f"📊 Generated migration report: {report_path}")
    return report_path


def main():
    print("\U0001f680 Starting documentation organization...")

    try:
        setup_directories()
        moved_files, skipped_files = move_files()
        generate_report(moved_files, skipped_files)
    except Exception as e:
        print(f"\U0001f6ab Error during documentation organization: {str(e)}")
        report_path = generate_report(moved_files, skipped_files)

    print("\n\U00002705 Documentation organization complete!")
    print(f"\U0001f4c4 {len(moved_files)} files were reorganized")
    if skipped_files:
        print(
            f"\U000026a0  {len(skipped_files)} files were not moved (see report for details)"
        )
    print(f"\U0001f4d2 Review the migration report: {report_path}")


if __name__ == "__main__":
    main()
