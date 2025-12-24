#!/usr/bin/env python3
"""
Reorganize the HyperCode repository structure to be more maintainable.
This script helps move files to their appropriate locations.
"""

import shutil
from pathlib import Path

# Define the repository root
REPO_ROOT = Path(__file__).parent.parent

# Define the new directory structure
NEW_STRUCTURE = {
    "core/": ["src/", "tests/", "benchmarks/"],
    "frontend/": ["hypercode-visual/", "web-playground/", "vscode-extension/"],
    "archive/": [
        "hypercode-proto/",
        "HyperCode 2.0V/",
        "new files to check/",
        "interactive HyperCode Evolution Roadmap/",
    ],
    "docs/": ["documentation/"],
    "config/": ["config/"],
    "scripts/": ["scripts/"],
}


def create_directories():
    """Create the new directory structure."""
    print("🚀 Creating new directory structure...")
    for directory in NEW_STRUCTURE.keys():
        (REPO_ROOT / directory).mkdir(exist_ok=True)
        print(f"  - Created {directory}")


def move_files():
    """Move files to their new locations."""
    print("\n🔄 Moving files to new locations...")

    # Move core files
    print("\n📦 Core files:")
    for item in NEW_STRUCTURE["core/"]:
        src = REPO_ROOT / item
        if src.exists():
            dst = REPO_ROOT / "core" / Path(item).name
            print(f"  - Moving {src} to {dst}")
            shutil.move(str(src), str(dst))

    # Move frontend files
    print("\n💻 Frontend files:")
    for item in NEW_STRUCTURE["frontend/"]:
        src = REPO_ROOT / item
        if src.exists():
            dst = REPO_ROOT / "frontend" / Path(item).name
            print(f"  - Moving {src} to {dst}")
            shutil.move(str(src), str(dst))

    # Archive old/experimental files
    print("\n🗄 Archiving old/experimental files:")
    for item in NEW_STRUCTURE["archive/"]:
        src = REPO_ROOT / item
        if src.exists():
            # Replace spaces with hyphens in directory names
            new_name = item.replace(" ", "-")
            dst = REPO_ROOT / "archive" / new_name
            print(f"  - Moving {src} to {dst}")
            shutil.move(str(src), str(dst))


def update_gitignore():
    """Update .gitignore with new paths."""
    gitignore_path = REPO_ROOT / ".gitignore"
    if not gitignore_path.exists():
        return

    print("\n📝 Updating .gitignore...")
    with open(gitignore_path, "a") as f:
        f.write("\n# New structure paths\n/archive/\n")
    print("  - Updated .gitignore")


def main():
    print("🔄 Reorganizing HyperCode repository structure...")

    # Create new directories
    create_directories()

    # Move files
    move_files()

    # Update .gitignore
    update_gitignore()

    print("\n✅ Repository reorganization complete!")
    print("\nNext steps:")
    print("1. Review the changes")
    print("2. Test the codebase")
    print("3. Update any hardcoded paths in the code")
    print("4. Commit the changes")


if __name__ == "__main__":
    main()
