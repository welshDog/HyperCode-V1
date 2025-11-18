#!/usr/bin/env python3
"""
HyperCode AI Research + Perplexity Integration Demo
Demonstrates how the Perplexity API can be used to enhance the AI Research document
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from hypercode.perplexity_client import PerplexityClient


def demo_ai_research_queries():
    """Demonstrate AI Research integration with Perplexity"""
    print("🧠 HyperCode AI Research + Perplexity Integration Demo")
    print("=" * 60)

    # Initialize the client
    client = PerplexityClient()

    # AI Research related queries
    queries = [
        {
            "title": "Neurodivergent-First Design",
            "query": "What are the key principles of neurodivergent-first programming language design?",
            "context": "Focus on accessibility features for ADHD, autism, and dyslexia",
        },
        {
            "title": "Multi-Backend Architecture",
            "query": "How can a programming language support multiple AI backends simultaneously?",
            "context": "Consider GPT-4, Claude, local models, and quantum computing",
        },
        {
            "title": "Spatial Programming Paradigms",
            "query": "What are the benefits of 2D spatial code execution like Befunge?",
            "context": "Focus on visual thinking and neurodivergent cognitive patterns",
        },
        {
            "title": "Living Documentation",
            "query": "How can technical documentation be automated and kept up-to-date?",
            "context": "Consider AI-powered research synthesis and knowledge graphs",
        },
    ]

    for i, query_info in enumerate(queries, 1):
        print(f"\n🔍 Query {i}: {query_info['title']}")
        print(f"Context: {query_info['context']}")
        print("-" * 50)

        # Build the full prompt
        full_prompt = f"""
        Based on current AI and programming language research, please answer:

        {query_info['query']}

        Context: {query_info['context']}

        Please provide a concise but comprehensive response that would be useful
        for the HyperCode AI Research document.
        """

        try:
            response = client.query(full_prompt)

            if "error" in response:
                print(f"❌ Error: {response['error']}")
                continue

            if "choices" in response and response["choices"]:
                content = response["choices"][0]["message"]["content"]
                print("✅ Response:")
                print(content[:400] + "..." if len(content) > 400 else content)
            else:
                print("❌ Unexpected response format")

        except Exception as e:
            print(f"❌ Exception: {e}")

    print("\n🎉 Demo completed!")
    print("\n💡 Next Steps:")
    print("   - Integrate these responses into the AI Research document")
    print("   - Set up automated daily research updates")
    print("   - Create knowledge graph from responses")
    print("   - Generate markdown sections automatically")


def test_document_specific_queries():
    """Test queries specific to the HyperCode AI Research document"""
    print("\n📚 Document-Specific Query Testing")
    print("=" * 40)

    client = PerplexityClient()

    # Test specific sections of the AI Research document
    document_queries = [
        "What should be included in the HyperCode Language Specification v0.1?",
        "How can we implement multi-backend compilation for HyperCode?",
        "What are the key phases for implementing neurodivergent-first design?",
        "How can HyperCode support both quantum and DNA computing backends?",
    ]

    for query in document_queries:
        print(f"\n📝 Query: {query}")
        try:
            response = client.query(query)
            if "choices" in response and response["choices"]:
                content = response["choices"][0]["message"]["content"]
                print(f"✅ {content[:200]}...")
        except Exception as e:
            print(f"❌ Error: {e}")


if __name__ == "__main__":
    demo_ai_research_queries()
    test_document_specific_queries()
