#!/usr/bin/env python3
"""
Import HyperCode Space Data
"""

import json
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from hypercode.enhanced_perplexity_client import EnhancedPerplexityClient


def import_hypercode_space_data():
    """Import your actual HyperCode Space data"""
    client = EnhancedPerplexityClient()

    print("🚀 Importing HyperCode Space Data...")
    print("=" * 50)

    # Load the data
    try:
        with open("hypercode_space_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        print("✅ Loaded hypercode_space_data.json")
    except Exception as e:
        print(f"❌ Error loading file: {e}")
        return

    # Extract and import documents
    imported_count = 0

    # Check if it has the expected structure
    if "space_metadata" in data:
        print("📋 Found HyperCode Space metadata")

        # Import core philosophy
        if "core_philosophy" in data:
            philosophy = data["core_philosophy"]

            # Big idea
            if "big_idea" in philosophy:
                big_idea_data = philosophy["big_idea"]
                if isinstance(big_idea_data, list):
                    big_idea_content = []
                    for item in big_idea_data:
                        if isinstance(item, dict):
                            principle = item.get("principle", "Unknown Principle")
                            description = item.get("description", "")
                            big_idea_content.append(f"**{principle}**: {description}")
                        else:
                            big_idea_content.append(str(item))
                    big_idea_text = "\n\n".join(big_idea_content)
                else:
                    big_idea_text = str(big_idea_data)

                client.knowledge_base.add_document(
                    title="HyperCode Core Philosophy - Big Idea",
                    content=big_idea_text,
                    tags=["philosophy", "core", "big-idea"],
                    url="https://www.perplexity.ai/spaces/hypercode-8B7p3SNcRcWhtGCk5ZGzjQ",
                )
                imported_count += 1
                print("✅ Imported: Core Philosophy - Big Idea")

            # Neurodiversity first
            if "neurodiversity_first" in philosophy:
                neuro_content = philosophy["neurodiversity_first"]
                if isinstance(neuro_content, dict):
                    neuro_text = "\n".join(
                        [f"**{k}**: {v}" for k, v in neuro_content.items()]
                    )
                else:
                    neuro_text = str(neuro_content)

                client.knowledge_base.add_document(
                    title="Neurodiversity-First Design Principles",
                    content=neuro_text,
                    tags=["neurodiversity", "design", "principles"],
                    url="https://www.perplexity.ai/spaces/hypercode-8B7p3SNcRcWhtGCk5ZGzjQ",
                )
                imported_count += 1
                print("✅ Imported: Neurodiversity-First Principles")

            # Technical foundations
            if "technical_foundations" in philosophy:
                tech_content = philosophy["technical_foundations"]
                if isinstance(tech_content, dict):
                    tech_text = "\n".join(
                        [f"**{k}**: {v}" for k, v in tech_content.items()]
                    )
                else:
                    tech_text = str(tech_content)

                client.knowledge_base.add_document(
                    title="Technical Foundations",
                    content=tech_text,
                    tags=["technical", "foundations", "architecture"],
                    url="https://www.perplexity.ai/spaces/hypercode-8B7p3SNcRcWhtGCk5ZGzjQ",
                )
                imported_count += 1
                print("✅ Imported: Technical Foundations")

        # Import research findings
        if "research_findings" in data:
            research = data["research_findings"]

            for category, findings in research.items():
                if isinstance(findings, dict):
                    findings_text = "\n".join(
                        [f"**{k}**: {v}" for k, v in findings.items()]
                    )
                else:
                    findings_text = str(findings)

                client.knowledge_base.add_document(
                    title=f"Research Findings - {category.replace('_', ' ').title()}",
                    content=findings_text,
                    tags=["research", "findings", category],
                    url="https://www.perplexity.ai/spaces/hypercode-8B7p3SNcRcWhtGCk5ZGzjQ",
                )
                imported_count += 1
                print(f"✅ Imported: Research Findings - {category}")

        # Import implementation details
        if "implementation_roadmap" in data:
            roadmap = data["implementation_roadmap"]

            for phase, details in roadmap.items():
                if isinstance(details, dict):
                    phase_text = "\n".join(
                        [f"**{k}**: {v}" for k, v in details.items()]
                    )
                else:
                    phase_text = str(details)

                client.knowledge_base.add_document(
                    title=f"Implementation - {phase.replace('_', ' ').title()}",
                    content=phase_text,
                    tags=["implementation", "roadmap", phase],
                    url="https://www.perplexity.ai/spaces/hypercode-8B7p3SNcRcWhtGCk5ZGzjQ",
                )
                imported_count += 1
                print(f"✅ Imported: Implementation - {phase}")

    else:
        print("⚠️ Unexpected file structure. Trying to extract documents...")
        # Try to find any document-like structure
        for key, value in data.items():
            if isinstance(value, (str, dict, list)) and key not in [
                "import_info",
                "space_metadata",
            ]:
                content = str(value)
                if len(content) > 100:  # Only import substantial content
                    client.knowledge_base.add_document(
                        title=f"HyperCode Research - {key.replace('_', ' ').title()}",
                        content=content,
                        tags=["hypercode", "research", key],
                        url="https://www.perplexity.ai/spaces/hypercode-8B7p3SNcRcWhtGCk5ZGzjQ",
                    )
                    imported_count += 1
                    print(f"✅ Imported: {key}")

    print(f"\n🎉 Successfully imported {imported_count} documents!")
    print(f"📚 Total knowledge base: {len(client.list_research_documents())} documents")

    # Test the import
    print("\n🧪 Testing imported data:")
    test_queries = [
        "What is HyperCode's big idea?",
        "How does neurodiversity-first design work?",
        "What are the technical foundations?",
        "Tell me about the research findings",
    ]

    for query in test_queries:
        response = client.query_with_context(query, use_knowledge_base=True)
        if "choices" in response and response["choices"]:
            content = response["choices"][0]["message"]["content"]
            print(f'✅ Query: "{query[:30]}..." - Response: {len(content)} chars')
        else:
            print(f'⚠️ Query: "{query[:30]}..." - No response')


if __name__ == "__main__":
    import_hypercode_space_data()
