"""
Test script for Perplexity API integration.
"""

import json
import sys
from pathlib import Path

import requests

# Add the project root to the Python path
sys.path.append(str(Path(__file__).parent.parent))

from hypercode.perplexity_client import PerplexityClient


def main():
    """
    Test the Perplexity API connection and make a sample query.
    """
    print("Testing connection to Perplexity API...")

    try:
        # Initialize client
        client = PerplexityClient()

        # Make a test query
        print("\nSending test query to Perplexity API...")
        response = client.query("What are the key features of Python 3.11?")

        print("\nResponse from Perplexity API:")

        if isinstance(response, dict):
            if "error" in response:
                print(f"Error: {response['error']}")
            elif "choices" in response and len(response["choices"]) > 0:
                print(response["choices"][0]["message"]["content"])
            else:
                print("Unexpected response format:")
                print(json.dumps(response, indent=2))
        else:
            print(response)

    except requests.exceptions.RequestException as e:
        print(f"\nRequest failed: {str(e)}")
        if hasattr(e, "response") and e.response is not None:
            print(f"Status code: {e.response.status_code}")
            print(f"Response: {e.response.text}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
        import traceback

        traceback.print_exc()


if __name__ == "__main__":
    main()
