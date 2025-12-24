"""
Configuration module for HyperCode.
Handles environment variables and API keys securely.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file
env_path = Path(".env")
load_dotenv(dotenv_path=env_path)


class Config:
    """Configuration class for HyperCode"""

    # API Keys
    PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

    # API Endpoints
    PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"

    # Headers
    @classmethod
    def get_headers(cls):
        """Get headers for API requests"""
        return {
            "Authorization": f"Bearer {cls.PERPLEXITY_API_KEY}",
            "Content-Type": "application/json",
        }
