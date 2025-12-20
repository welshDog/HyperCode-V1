"""
Perplexity API Client for HyperCode

This module provides a basic client for interacting with the Perplexity API.
"""

import os
import time
from typing import Dict, List, Optional, Any, Union
import requests


class PerplexityClient:
    """Client for interacting with the Perplexity API."""

    BASE_URL = "https://api.perplexity.ai"

    def __init__(self, api_key: Optional[str] = None):
        """Initialize the PerplexityClient.

        Args:
            api_key: Optional API key. If not provided, will look for PERPLEXITY_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv("PERPLEXITY_API_KEY")
        if not self.api_key:
            raise ValueError(
                "API key must be provided either as an argument or through the PERPLEXITY_API_KEY environment variable"
            )

        self.session = requests.Session()
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            }
        )

    def complete(
        self,
        prompt: str,
        model: str = "pplx-7b-online",
        max_tokens: int = 100,
        temperature: float = 0.7,
        top_p: float = 1.0,
        **kwargs,
    ) -> Dict[str, Any]:
        """Generate text completion using the Perplexity API.

        Args:
            prompt: The prompt to send to the model
            model: The model to use for completion
            max_tokens: Maximum number of tokens to generate
            temperature: Controls randomness (0.0 to 1.0)
            top_p: Nucleus sampling parameter
            **kwargs: Additional parameters to pass to the API

        Returns:
            The API response as a dictionary
        """
        endpoint = f"{self.BASE_URL}/completions"

        data = {
            "model": model,
            "prompt": prompt,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "top_p": top_p,
            **kwargs,
        }

        try:
            response = self.session.post(endpoint, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making request to Perplexity API: {e}")
            if hasattr(e, "response") and e.response is not None:
                print(f"Response: {e.response.text}")
            raise

    def chat(
        self,
        messages: List[Dict[str, str]],
        model: str = "pplx-7b-chat",
        max_tokens: int = 1000,
        temperature: float = 0.7,
        **kwargs,
    ) -> Dict[str, Any]:
        """Generate chat completion using the Perplexity API.

        Args:
            messages: List of message dictionaries with 'role' and 'content' keys
            model: The model to use for chat completion
            max_tokens: Maximum number of tokens to generate
            temperature: Controls randomness (0.0 to 1.0)
            **kwargs: Additional parameters to pass to the API

        Returns:
            The API response as a dictionary
        """
        endpoint = f"{self.BASE_URL}/chat/completions"

        data = {
            "model": model,
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            **kwargs,
        }

        try:
            response = self.session.post(endpoint, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making request to Perplexity API: {e}")
            if hasattr(e, "response") and e.response is not None:
                print(f"Response: {e.response.text}")
            raise


# Example usage
if __name__ == "__main__":
    # Initialize the client with your API key
    client = PerplexityClient(api_key="your-api-key-here")

    # Example completion
    completion = client.complete(
        prompt="What is the capital of France?", model="pplx-7b-online", max_tokens=50
    )
    print("Completion:", completion)

    # Example chat
    chat_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
    ]
    chat_response = client.chat(messages=chat_messages, model="pplx-7b-chat")
    print("Chat Response:", chat_response)
