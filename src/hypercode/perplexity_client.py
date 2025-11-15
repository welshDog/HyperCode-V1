"""
Perplexity AI API client for HyperCode.
Handles communication with the Perplexity API.
"""

from typing import Dict, Optional

import requests

from ..config import Config


class PerplexityClient:
    """Client for interacting with Perplexity AI API"""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the Perplexity client.

        Args:
            api_key: Optional API key. If not provided, will use the one from config.
        """
        self.api_key = api_key or Config.PERPLEXITY_API_KEY
        self.base_url = Config.PERPLEXITY_API_URL

        if not self.api_key:
            raise ValueError(
                "Perplexity API key not found. "
                "Please set the PERPLEXITY_API_KEY environment variable."
            )

    def query(self, prompt: str, model: str = "sonar-small-online") -> Dict:
        """Send a query to the Perplexity API.

        Args:
            prompt: The prompt to send to the API.
            model: The model to use for the query.

        Returns:
            The API response as a dictionary.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "accept": "application/json",
        }

        payload = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are an AI assistant that helps with programming tasks. Be concise and helpful.",
                },
                {"role": "user", "content": prompt},
            ],
            "max_tokens": 1000,
            "temperature": 0.7,
        }

        try:
            response = requests.post(
                self.base_url, headers=headers, json=payload, timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {
                "error": str(e),
                "status_code": getattr(e.response, "status_code", None),
            }


def test_connection():
    """Test the connection to the Perplexity API"""
    try:
        client = PerplexityClient()
        response = client.query("Test connection")
        if "error" in response:
            print(f"Error: {response['error']}")
            return False
        print("Successfully connected to Perplexity API!")
        return True
    except Exception as e:
        print(f"Error testing Perplexity API connection: {e}")
        return False


if __name__ == "__main__":
    test_connection()
