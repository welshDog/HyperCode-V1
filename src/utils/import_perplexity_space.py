#!/usr/bin/env python3
"""
Perplexity Space Data Importer
Helps import research data from your Perplexity Space into the HyperCode knowledge base
"""

import json
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from hypercode.enhanced_perplexity_client import EnhancedPerplexityClient


def create_manual_import_script():
    """Create a script for manual data entry from Perplexity Space"""
    print("📝 Manual Data Entry Script")
    print("=" * 40)

    client = EnhancedPerplexityClient()

    print(
        """
    To import your Perplexity Space data, you have several options:

    1. 📋 Manual Entry (Recommended for small amounts of data)
    2. 📄 JSON Import (For structured data)
    3. 🌐 Web Scraping (Advanced - requires access to the space)

    Let's start with manual entry...
    """
    )

    documents_added = 0

    while True:
        print(f"\n📄 Document {documents_added + 1}")
        print("-" * 30)

        title = input("Enter document title (or 'done' to finish): ").strip()

        if title.lower() == "done":
            break

        print("Enter document content (press Enter twice to finish):")
        content_lines = []
        empty_line_count = 0

        while True:
            line = input()
            if line.strip() == "":
                empty_line_count += 1
                if empty_line_count >= 2:
                    break
            else:
                empty_line_count = 0
            content_lines.append(line)

        content = "\n".join(content_lines)

        # Get tags
        tags_input = input("Enter tags (comma-separated, optional): ").strip()
        tags = [tag.strip() for tag in tags_input.split(",")] if tags_input else []

        # Get URL
        url = input("Enter URL (optional): ").strip() or None

        # Add to knowledge base
        try:
            doc_id = client.add_research_data(title, content, url, tags)
            print(f"✅ Added document: {doc_id}")
            documents_added += 1
        except Exception as e:
            print(f"❌ Error adding document: {e}")

        continue_input = input("Add another document? (y/n): ").strip().lower()
        if continue_input != "y":
            break

    print(f"\n🎉 Added {documents_added} documents to the knowledge base!")
    return documents_added


def create_json_import_template():
    """Create a JSON template for importing data"""
    template = {
        "import_instructions": """
        Fill in this template with your Perplexity Space data.
        Each document should have:
        - title: Document title
        - content: Full document content
        - url: Source URL (optional)
        - tags: List of relevant tags (optional)
        """,
        "documents": [
            {
                "title": "Example: Your Research Topic",
                "content": "Paste your research content here...",
                "url": "https://www.perplexity.ai/spaces/hypercode-8B7p3SNcRcWhtGCk5ZGzjQ",
                "tags": ["research", "hypercode", "example"],
            }
        ],
    }

    with open("perplexity_space_data.json", "w", encoding="utf-8") as f:
        json.dump(template, f, indent=2, ensure_ascii=False)

    print("📄 Created perplexity_space_data.json template")
    print("   Edit this file with your actual data, then run:")
    print("   python import_perplexity_space.py json")


def import_from_json():
    """Import data from JSON file"""
    client = EnhancedPerplexityClient()

    try:
        with open("perplexity_space_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        if "documents" not in data:
            print("❌ JSON file must contain a 'documents' array")
            return False

        imported_count = 0
        for doc in data["documents"]:
            try:
                client.add_research_data(
                    title=doc.get("title", "Untitled"),
                    content=doc.get("content", ""),
                    url=doc.get("url"),
                    tags=doc.get("tags", []),
                )
                imported_count += 1
                print(f"✅ Imported: {doc.get('title', 'Untitled')}")
            except Exception as e:
                print(f"❌ Error importing '{doc.get('title', 'Unknown')}': {e}")

        print(f"\n🎉 Successfully imported {imported_count} documents!")
        return True

    except FileNotFoundError:
        print("❌ File perplexity_space_data.json not found")
        print("   Run this script first to create the template")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON format: {e}")
        return False


def test_imported_data():
    """Test the imported data with context-aware queries"""
    print("\n🧪 Testing Imported Data")
    print("=" * 30)

    client = EnhancedPerplexityClient()

    # List all documents
    docs = client.list_research_documents()
    print(f"📚 Knowledge base contains {len(docs)} documents:")

    for doc in docs:
        print(f"  - {doc.title} ({len(doc.content)} chars)")

    # Test context-aware queries
    test_queries = [
        "What is HyperCode?",
        "Tell me about the research findings",
        "What are the main features?",
        "How does this relate to neurodiversity?",
    ]

    print("\n🔍 Testing context-aware queries:")

    for query in test_queries:
        print(f"\n❓ Query: {query}")
        response = client.query_with_context(query, use_knowledge_base=True)

        if "choices" in response and response["choices"]:
            content = response["choices"][0]["message"]["content"]
            print(f"✅ Response: {content[:200]}...")
        else:
            print(f"❌ Error: {response}")


def show_import_menu():
    """Show the import menu"""
    print("🚀 Perplexity Space Data Importer")
    print("=" * 40)
    print("\nChoose an import method:")
    print("1. 📋 Manual data entry")
    print("2. 📄 Create JSON template")
    print("3. 📥 Import from JSON file")
    print("4. 🧪 Test imported data")
    print("5. ❌ Exit")

    while True:
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            create_manual_import_script()
            break
        elif choice == "2":
            create_json_import_template()
            break
        elif choice == "3":
            if import_from_json():
                test_imported_data()
            break
        elif choice == "4":
            test_imported_data()
            break
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-5.")


if __name__ == "__main__":
    show_import_menu()
