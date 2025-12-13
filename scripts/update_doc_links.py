#!/usr/bin/env python3
"""
Update internal documentation links after reorganization.
"""

import re
from pathlib import Path

# Define the old to new path mappings
PATH_MAPPINGS = {
    # Old path: New path (relative to docs/)
    "AI_INTEGRATION_GUIDE.md": "guides/AI_INTEGRATION_GUIDE.md",
    "API_REFERENCE.md": "reference/API_REFERENCE.md",
    "ARCHITECTURE.md": "architecture/ARCHITECTURE.md",
    "BEST_PRACTICES.md": "reference/BEST_PRACTICES.md",
    "CHANGELOG.md": "community/CHANGELOG.md",
    "CONTRIBUTING.md": "community/CONTRIBUTING.md",
    "DESIGN_PRINCIPLES.md": "reference/DESIGN_PRINCIPLES.md",
    "FAQ.md": "community/FAQ.md",
    "LANGUAGE_REFERENCE.md": "reference/LANGUAGE_REFERENCE.md",
    "ROADMAP.md": "roadmaps/ROADMAP.md",
    "TUTORIAL.md": "guides/TUTORIAL.md",
    # Add more mappings as needed
}


def update_links_in_file(file_path):
    """Update links in a single file."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        updated = False

        # Update markdown links [text](path)
        for old_path, new_path in PATH_MAPPINGS.items():
            pattern = rf"\[([^\]]*)\]\(([^)]*{re.escape(old_path)}[^)]*)\)"

            def replace_link(match):
                nonlocal updated
                text = match.group(1)
                old_link = match.group(2)
                # Only update if it's a direct filename match
                if old_path in old_link.split("/")[-1]:
                    updated = True
                    return f"[{text}]({new_path})"
                return match.group(0)

            content = re.sub(pattern, replace_link, content)

        # Save if changes were made
        if updated:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return True

    except Exception as e:
        print(f"⚠️  Error processing {file_path}: {e}")

    return False


def main():
    print("🔗 Updating internal documentation links...")

    docs_dir = Path(__file__).parent.parent / "docs"
    updated_count = 0

    # Process all markdown files in the docs directory
    for md_file in docs_dir.rglob("*.md"):
        if update_links_in_file(md_file):
            print(f"✅ Updated links in: {md_file.relative_to(docs_dir.parent)}")
            updated_count += 1

    print(f"\n✨ Updated {updated_count} files with new links")
    print(
        "\nNote: Some links might need manual verification. Please review the changes."
    )


if __name__ == "__main__":
    main()
