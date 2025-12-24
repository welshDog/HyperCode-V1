#!/usr/bin/env python3
"""
HyperCode Research Auto-Updater

This script scrapes academic sources for new research on:
- Neurodivergent programming
- ADHD developer productivity
- Dyslexia code readability
- AI-assisted coding
- Forgotten programming languages
- Quantum/DNA computing

Runs daily via GitHub Actions.
"""

import os
import re
from datetime import datetime, timedelta
from pathlib import Path

import arxiv
import feedparser

# === CONFIGURATION ===

ARXIV_SEARCH_QUERIES = [
    "neurodivergent programming",
    "ADHD developer productivity",
    "dyslexia code readability",
    "autism software engineering",
    "AI assisted programming",
    "LLM code generation",
    "quantum programming languages",
    "DNA computing",
]

MAX_RESULTS_PER_QUERY = 5
DAYS_LOOKBACK = 7  # Only check papers from last week

REPO_ROOT = Path(__file__).parent.parent
REFERENCES_DIR = REPO_ROOT / "references" / "academic-papers"
CHANGELOG = REPO_ROOT / "CHANGELOG.md"

# === HELPER FUNCTIONS ===


def sanitize_filename(title: str) -> str:
    """Convert paper title to valid filename."""
    # Remove special characters, lowercase, replace spaces with hyphens
    clean = re.sub(r"[^a-zA-Z0-9\s-]", "", title)
    clean = clean.lower().strip().replace(" ", "-")
    # Limit length
    return clean[:60] + ".md"


def paper_exists(filename: str) -> bool:
    """Check if paper already documented."""
    return (REFERENCES_DIR / filename).exists()


def format_paper_markdown(paper) -> str:
    """Format arXiv paper as markdown."""
    md = f"""# {paper.title}

> **Authors:** {', '.join(author.name for author.name in paper.authors)}

> **Published:** {paper.published.strftime('%Y-%m-%d')}

> **arXiv ID:** {paper.entry_id.split('/')[-1]}

> **URL:** {paper.entry_id}

---

## Abstract

{paper.summary}

---

## Key Topics

{', '.join(paper.categories)}

---

## PDF Link

[Download PDF]({paper.pdf_url})

---

## BibTeX

```bibtex
@article{{{paper.entry_id.split('/')[-1].replace('.', '_')},
  title={{{paper.title}}},
  author={{{' and '.join(author.name for author in paper.authors)}}},
  journal={{arXiv preprint}},
  year={{{paper.published.year}}},
  url={{{paper.entry_id}}}
}}
```

---

**Auto-discovered:** {datetime.now().strftime('%Y-%m-%d')}
"""
    return md


def update_changelog(new_papers: list):
    """Add new papers to CHANGELOG."""
    if not new_papers:
        return

    today = datetime.now().strftime("%Y-%m-%d")
    entry = f"""\n## [{today}] - Auto-Update\n\n### New Research Papers\n\n"""

    for paper in new_papers:
        entry += f"- [{paper.title}](references/academic-papers/{sanitize_filename(paper.title)})\n"

    # Prepend to CHANGELOG
    if CHANGELOG.exists():
        existing = CHANGELOG.read_text()
        CHANGELOG.write_text(entry + existing)
    else:
        CHANGELOG.write_text(entry)


# === MAIN SCRAPER ===


def scrape_arxiv():
    """Scrape arXiv for new papers."""
    new_papers = []
    cutoff_date = datetime.now() - timedelta(days=DAYS_LOOKBACK)

    print(
        f"\n🔍 Scraping arXiv for papers published after {cutoff_date.strftime('%Y-%m-%d')}...\n"
    )

    for query in ARXIV_SEARCH_QUERIES:
        print(f"  • Searching: '{query}'")

        search = arxiv.Search(
            query=query,
            max_results=MAX_RESULTS_PER_QUERY,
            sort_by=arxiv.SortCriterion.SubmittedDate,
        )

        for paper in search.results():
            # Skip if too old
            if paper.published < cutoff_date:
                continue

            filename = sanitize_filename(paper.title)

            # Skip if already documented
            if paper_exists(filename):
                print(f"    ✓ Already documented: {paper.title[:50]}...")
                continue

            # Save new paper
            print(f"    ✓ NEW: {paper.title[:50]}...")
            (REFERENCES_DIR / filename).write_text(format_paper_markdown(paper))
            new_papers.append(paper)

    return new_papers


# === MAIN ===

if __name__ == "__main__":
    print("🤖 HyperCode Research Auto-Updater")
    print("=" * 50)

    # Ensure directories exist
    REFERENCES_DIR.mkdir(parents=True, exist_ok=True)

    # Scrape sources
    new_papers = scrape_arxiv()

    # Update changelog
    update_changelog(new_papers)

    # Summary
    print(f"\n✅ Done! Found {len(new_papers)} new papers.\n")

    if new_papers:
        print("New papers:")
        for paper in new_papers:
            print(f"  • {paper.title}")
    else:
        print("👀 No new papers found. Check back tomorrow!")
