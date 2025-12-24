#!/usr/bin/env python3
"""
HyperCode Link Validator

Validates all URLs in markdown files to ensure they're not broken.

Usage:
    python scripts/link-validator.py
"""

import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import List, Set, Tuple

import requests


class LinkValidator:
    """Validate all links in markdown files."""

    def __init__(self, docs_dir: str = "docs"):
        self.docs_dir = Path(docs_dir)
        self.links: Set[str] = set()
        self.broken_links: List[Tuple[str, str, int]] = []
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "HyperCode-Research-Bot/1.0"})

    def extract_links(self, content: str, filepath: str):
        """Extract all URLs from markdown content."""
        # Match [text](url) and [text]: url patterns
        markdown_links = re.findall(r"\[([^\]]+)\]\(([^\)]+)\)", content)
        reference_links = re.findall(r"\[([^\]]+)\]:\s*(.+)$", content, re.MULTILINE)

        all_links = markdown_links + reference_links

        for text, url in all_links:
            if url.startswith("http"):
                self.links.add((url, filepath))

    def scan_files(self):
        """Scan all markdown files for links."""
        print("🔍 Scanning markdown files for links...")

        for md_file in self.docs_dir.rglob("*.md"):
            with open(md_file, "r", encoding="utf-8") as f:
                content = f.read()

            self.extract_links(content, str(md_file))

        print(f"   Found {len(self.links)} unique URLs\n")

    def check_url(self, url: str, filepath: str) -> Tuple[bool, str, str]:
        """Check if a URL is accessible."""
        try:
            response = self.session.head(url, timeout=10, allow_redirects=True)
            if response.status_code >= 400:
                return False, url, filepath
            return True, url, filepath
        except Exception as e:
            return False, url, filepath

    def validate_links(self, max_workers: int = 10):
        """Validate all links concurrently."""
        print("🔗 Validating links...\n")

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(self.check_url, url, filepath): (url, filepath)
                for url, filepath in self.links
            }

            completed = 0
            total = len(futures)

            for future in as_completed(futures):
                is_valid, url, filepath = future.result()
                completed += 1

                if not is_valid:
                    self.broken_links.append((url, filepath, 0))
                    print(f"   ❌ [{completed}/{total}] BROKEN: {url[:60]}")
                else:
                    print(f"   ✓ [{completed}/{total}] OK: {url[:60]}")

    def report(self):
        """Generate validation report."""
        print("\n" + "=" * 60)
        print("LINK VALIDATION REPORT")
        print("=" * 60)

        total = len(self.links)
        broken = len(self.broken_links)
        valid = total - broken

        print(f"\n📊 Summary:")
        print(f"   Total links: {total}")
        print(f"   Valid: {valid} ✓")
        print(f"   Broken: {broken} ❌")
        print(f"   Success rate: {(valid/total*100) if total > 0 else 0:.1f}%")

        if broken > 0:
            print(f"\n❌ Broken Links:")
            for url, filepath, _ in self.broken_links:
                print(f"   • {filepath}")
                print(f"     {url}\n")

        print("=" * 60)

        return broken == 0


def main():
    """
    Main entry point.
    """
    print("")
    print("╔═══════════════════════════════════════════════════════════╗")
    print("║         HyperCode Link Validator v1.0.0                   ║")
    print("║   Ensuring all research links are accessible              ║")
    print("╚═══════════════════════════════════════════════════════════╝")
    print("")

    validator = LinkValidator()

    try:
        validator.scan_files()
        validator.validate_links()
        success = validator.report()

        return 0 if success else 1

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
