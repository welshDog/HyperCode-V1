#!/usr/bin/env python3
"""
Test script for Perplexity API integration with HyperCode AI Research
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))


from hypercode.perplexity_client import PerplexityClient


def test_perplexity_connection():
    """Test Perplexity API with detailed logging"""
    print("Testing Perplexity API Connection...")
    print("=" * 50)

    try:
        # Initialize client
        client = PerplexityClient()
        print("Client initialized")
        print(f"API Key: {client.api_key[:10]}...{client.api_key[-10:]}")
        print(f"Base URL: {client.base_url}")

        # Test query related to AI Research
        test_prompt = """
        Based on the HyperCode AI Research document, what are the key features
        of the neurodivergent-first programming language design?
        """

        print("\nSending test query...")
        print(f"Prompt: {test_prompt[:100]}...")

        response = client.query(test_prompt)

        if "error" in response:
            print(f"API Error: {response}")
            return False

        print("API Response received!")
        print(f"Response type: {type(response)}")

        # Extract content
        if "choices" in response and response["choices"]:
            content = response["choices"][0]["message"]["content"]
            print("\nResponse Content:")
            print("-" * 40)
            print(content)
            print("-" * 40)
            return True
        else:
            print(f"Unexpected response format: {response}")
            return False

    except Exception as e:
        print(f"Exception occurred: {e}")
        import traceback

        traceback.print_exc()
        return False


def test_ai_research_integration():
    """Test integration with AI Research document content"""
    print("\nTesting AI Research Integration...")
    print("=" * 50)

    try:
        client = PerplexityClient()

        # Test queries based on AI Research document
        queries = [
            "What is HyperCode's approach to neurodivergent-first design?",
            "How does HyperCode support multiple AI backends?",
            "What are the key phases in HyperCode's implementation roadmap?",
        ]

        for i, query in enumerate(queries, 1):
            print(f"Query {i}: {query}")
            response = client.query(query)

            if "error" in response:
                print(f"[ERROR] Error: {response['error']}")
                continue

            if "choices" in response and response["choices"]:
                content = response["choices"][0]["message"]["content"]
                print(f"[OK] Response: {content[:200]}...")
            else:
                print(f"[ERROR] Unexpected format: {response}")

    except Exception as e:
        print(f"[ERROR] Integration test failed: {e}")


if __name__ == "__main__":
    print("HyperCode + Perplexity AI Test Suite")
    print("=" * 60)

    # Test basic connection
    success = test_perplexity_connection()

    if success:
        # Test AI Research integration
        test_ai_research_integration()
        print("\n[SUCCESS] All tests completed!")
    else:
        print("\n[FAILED] Basic connection failed - skipping integration tests")
