#!/usr/bin/env python3
"""
Complete Import of HyperCode Space Data
"""

import json
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from hypercode.enhanced_perplexity_client import EnhancedPerplexityClient


def format_content(data, indent=0):
    """Recursively format nested data into readable text"""
    prefix = "  " * indent
    if isinstance(data, dict):
        result = []
        for key, value in data.items():
            result.append(f"{prefix}**{key}**:")
            if isinstance(value, (dict, list)):
                result.append(format_content(value, indent + 1))
            else:
                result.append(f"{prefix}  {value}")
        return "\n".join(result)
    elif isinstance(data, list):
        result = []
        for i, item in enumerate(data):
            result.append(f"{prefix}{i+1}.")
            if isinstance(item, (dict, list)):
                result.append(format_content(item, indent + 1))
            else:
                result.append(f"{prefix}  {item}")
        return "\n".join(result)
    else:
        return f"{prefix}{data}"


def import_all_hypercode_data():
    """Import all sections of your HyperCode Space data"""
    client = EnhancedPerplexityClient()

    print("🚀 Complete HyperCode Space Data Import")
    print("=" * 50)

    # Load the data
    try:
        with open("hypercode_space_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        print("✅ Loaded hypercode_space_data.json")
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return

    imported_count = 0

    # Import each major section
    sections_to_import = [
        ("space_metadata", "Space Metadata"),
        ("core_philosophy", "Core Philosophy"),
        ("research_findings", "Research Findings"),
        ("implementation_roadmap", "Implementation Roadmap"),
        ("technical_specifications", "Technical Specifications"),
        ("community_strategy", "Community Strategy"),
        ("ai_integration", "AI Integration Strategy"),
        ("neurodiversity_features", "Neurodiversity Features"),
    ]

    for section_key, section_name in sections_to_import:
        if section_key in data:
            section_data = data[section_key]
            content = format_content(section_data)

            client.knowledge_base.add_document(
                title=f"HyperCode Space - {section_name}",
                content=content,
                tags=["hypercode", section_key, "space-data"],
                url="https://www.perplexity.ai/spaces/hypercode-8B7p3SNcRcWhtGCk5ZGzjQ",
            )
            imported_count += 1
            print(f"✅ Imported: {section_name}")

    # Also import any other top-level sections
    for key, value in data.items():
        if key not in [s[0] for s in sections_to_import]:
            content = format_content(value)
            if len(content) > 50:  # Only import substantial content
                client.knowledge_base.add_document(
                    title=f"HyperCode Space - {key.replace('_', ' ').title()}",
                    content=content,
                    tags=["hypercode", key, "space-data"],
                    url="https://www.perplexity.ai/spaces/hypercode-8B7p3SNcRcWhtGCk5ZGzjQ",
                )
                imported_count += 1
                print(f"✅ Imported: {key}")

    print(f"\n🎉 Successfully imported {imported_count} documents!")
    print(f"📚 Total knowledge base: {len(client.list_research_documents())} documents")

    # Test the import with comprehensive queries
    print("\n🧪 Testing imported data:")
    test_queries = [
        "What is HyperCode's space metadata?",
        "What are the core philosophy principles?",
        "What research findings exist?",
        "What is the implementation roadmap?",
        "What technical specifications are defined?",
        "Tell me about the community strategy",
        "How does AI integration work?",
        "What neurodiversity features are included?",
    ]

    for query in test_queries:
        response = client.query_with_context(query, use_knowledge_base=True)
        if "choices" in response and response["choices"]:
            content = response["choices"][0]["message"]["content"]
            print(f'✅ Query: "{query[:40]}..." - Response: {len(content)} chars')
        else:
            print(f'⚠️ Query: "{query[:40]}..." - No response')

    # Show knowledge base summary
    print("\n📚 Knowledge Base Summary:")
    docs = client.list_research_documents()
    space_docs = [doc for doc in docs if "space-data" in doc.tags]
    other_docs = [doc for doc in docs if "space-data" not in doc.tags]

    print(f"  🚀 Space Data Documents: {len(space_docs)}")
    for doc in space_docs:
        print(f"    📄 {doc.title}")

    print(f"  📚 Other Documents: {len(other_docs)}")
    for doc in other_docs[:5]:  # Show first 5
        print(f"    📄 {doc.title}")
    if len(other_docs) > 5:
        print(f"    ... and {len(other_docs) - 5} more")


if __name__ == "__main__":
    import_all_hypercode_data()
