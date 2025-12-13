#!/usr/bin/env python3
"""
Perplexity Space Data Collector
Makes it easy to copy-paste and organize your research data
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from hypercode.enhanced_perplexity_client import EnhancedPerplexityClient


def quick_copy_paste_collector():
    """Quick collector for copy-paste workflow"""
    print("🚀 Quick Copy-Paste Collector")
    print("=" * 40)
    print("Go to your Perplexity Space and copy research content!")
    print("https://www.perplexity.ai/spaces/hypercode-8B7p3SNcRcWhtGCk5ZGzjQ")
    print()

    client = EnhancedPerplexityClient()
    collected = 0

    while True:
        print(f"\n📄 Research Item {collected + 1}")
        print("-" * 30)

        # Get title (optional - can auto-generate)
        title = input("📝 Title (or press Enter for auto-title): ").strip()
        if not title:
            title = (
                f"Research Item {collected + 1} - {datetime.now().strftime('%Y-%m-%d')}"
            )

        print("📋 Paste your research content below:")
        print("(Press Enter on empty line to finish)")

        content_lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            content_lines.append(line)

        content = "\n".join(content_lines)

        if not content:
            print("⚠️ No content provided, skipping...")
            continue

        # Auto-suggest tags based on content
        content_lower = content.lower()
        suggested_tags = []

        tag_keywords = {
            "neurodivergent": [
                "neurodivergent",
                "adhd",
                "autism",
                "dyslexia",
                "accessibility",
            ],
            "ai": [
                "ai",
                "artificial intelligence",
                "machine learning",
                "gpt",
                "claude",
            ],
            "language": ["language", "syntax", "programming", "code"],
            "research": ["research", "study", "findings", "data", "analysis"],
            "design": ["design", "ux", "interface", "user experience"],
            "quantum": ["quantum", "quantum computing", "qubit"],
            "spatial": ["spatial", "2d", "visual", "diagram"],
            "backend": ["backend", "compilation", "architecture"],
        }

        for tag, keywords in tag_keywords.items():
            if any(keyword in content_lower for keyword in keywords):
                suggested_tags.append(tag)

        # Show suggested tags
        if suggested_tags:
            print(f"🏷️ Suggested tags: {', '.join(suggested_tags)}")

        tags_input = input(
            "🏷️ Tags (comma-separated, or press Enter for suggestions): "
        ).strip()
        if tags_input:
            tags = [tag.strip() for tag in tags_input.split(",")]
        else:
            tags = suggested_tags

        # Add to knowledge base
        try:
            doc_id = client.add_research_data(title, content, None, tags)
            print(f"✅ Saved: {doc_id}")
            collected += 1
        except Exception as e:
            print(f"❌ Error: {e}")

        # Continue?
        if collected >= 1:
            continue_input = input("\n📝 Add another? (y/n): ").strip().lower()
            if continue_input != "y":
                break

    print(f"\n🎉 Collected {collected} research items!")
    return collected


def create_structured_template():
    """Create a structured JSON template for bulk import"""
    template = {
        "import_info": {
            "source": "Perplexity Space - HyperCode Research",
            "export_date": datetime.now().isoformat(),
            "instructions": "Fill in the documents array with your research data",
        },
        "documents": [
            {
                "title": "Example: HyperCode Core Concepts",
                "content": "Paste your research content here about HyperCode's core concepts...",
                "url": "https://www.perplexity.ai/spaces/hypercode-8B7p3SNcRcWhtGCk5ZGzjQ",
                "tags": ["hypercode", "concepts", "overview"],
                "category": "core-concepts",
                "date": "2025-11-18",
            },
            {
                "title": "Example: Neurodivergent Design Research",
                "content": "Paste findings about neurodivergent-first design principles...",
                "url": "https://www.perplexity.ai/spaces/hypercode-8B7p3SNcRcWhtGCk5ZGzjQ",
                "tags": ["neurodivergent", "design", "accessibility", "adhd", "autism"],
                "category": "accessibility",
                "date": "2025-11-18",
            },
            {
                "title": "Example: Multi-Backend Architecture",
                "content": "Paste research about compilation backends and architecture...",
                "url": "https://www.perplexity.ai/spaces/hypercode-8B7p3SNcRcWhtGCk5ZGzjQ",
                "tags": ["architecture", "backend", "compilation", "quantum"],
                "category": "technical",
                "date": "2025-11-18",
            },
        ],
    }

    filename = (
        f"perplexity_space_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    )

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(template, f, indent=2, ensure_ascii=False)

    print(f"📄 Created template: {filename}")
    print("📝 Edit this file with your actual research data")
    print("🚀 Then run: python import_perplexity_space.py (option 3)")

    return filename


def show_bro_hacks():
    """Show BROski's pro tips"""
    print(
        """
    🏁 BROski's Pro Hacks for Perplexity Space Collection
    ====================================================

    🎯 ORGANIZATION TIPS:
    - Group by topic: "Language Design", "Accessibility", "Architecture"
    - Add dates to track research evolution
    - Use consistent tags for easy search

    📋 CONTENT CHUNKING:
    - Break long threads into focused mini-documents
    - One main idea per document for better context matching
    - Keep titles descriptive and searchable

    🏷️ SMART TAGGING:
    - Always include "hypercode" as a base tag
    - Add specific tags: "neurodivergent", "ai", "quantum", "spatial"
    - Use category tags: "research", "design", "technical", "implementation"

    💾 BACKUP STRATEGY:
    - Keep a copy in Markdown for human reading
    - JSON version for automated imports
    - Version your exports with dates

    🔍 SEARCH OPTIMIZATION:
    - Include key terms in both title and content
    - Use synonyms for better matching
    - Add context like "study shows", "research indicates"

    🚀 AUTOMATION READY:
    - Follow the JSON structure exactly
    - Use consistent date format: YYYY-MM-DD
    - URLs help with source tracking
    """
    )


def main_menu():
    """Main menu for the collector"""
    print("🤙 Perplexity Space Data Collector - BROski Edition!")
    print("=" * 55)
    print("Source: https://www.perplexity.ai/spaces/hypercode-8B7p3SNcRcWhtGCk5ZGzjQ")
    print()

    while True:
        print("🎯 Choose your collection method:")
        print("1️⃣ Quick Copy-Paste (Live collection)")
        print("2️⃣ Create JSON Template (Bulk import)")
        print("3️⃣ Import Existing JSON File")
        print("4️⃣ Show BROski's Pro Hacks")
        print("5️⃣ Test Current Knowledge Base")
        print("6️⃣ Exit")

        choice = input("\n👉 Enter choice (1-6): ").strip()

        if choice == "1":
            quick_copy_paste_collector()
        elif choice == "2":
            create_structured_template()
        elif choice == "3":
            from import_perplexity_space import import_from_json, test_imported_data

            if import_from_json():
                test_imported_data()
        elif choice == "4":
            show_bro_hacks()
        elif choice == "5":
            from demo_enhanced_client import demo_knowledge_base_integration

            demo_knowledge_base_integration()
        elif choice == "6":
            print("🤙 Later BROski! Keep crushing it!")
            break
        else:
            print("❌ Invalid choice, try again!")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main_menu()
