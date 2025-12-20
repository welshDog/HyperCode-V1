import os

# Add the src directory to Python path for imports
import sys
from unittest.mock import Mock, patch

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from hypercode.perplexity_client import PerplexityClient


@pytest.fixture
def mock_perplexity_client():
    with patch("requests.post") as mock_post:
        mock_response = Mock()
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "Mocked response"}}]
        }
        mock_post.return_value = mock_response
        yield mock_post


@pytest.fixture
def mock_config():
    """Mock the Config class to provide a fake API key"""
    with patch("hypercode.perplexity_client.Config") as mock_config_class:
        mock_config_class.PERPLEXITY_API_KEY = "test_api_key_123"
        mock_config_class.PERPLEXITY_API_URL = "https://test.api.com"
        yield mock_config_class


def test_perplexity_client_initialization(mock_config):
    client = PerplexityClient()
    assert client is not None
    assert client.api_key == "test_api_key_123"
    assert client.base_url == "https://test.api.com"


def test_perplexity_query(mock_perplexity_client, mock_config):
    client = PerplexityClient()
    response = client.query("test query")
    assert response == {"choices": [{"message": {"content": "Mocked response"}}]}
    mock_perplexity_client.assert_called_once()


def test_perplexity_client_with_custom_api_key():
    """Test that custom API key overrides config"""
    client = PerplexityClient(api_key="custom_key_456")
    assert client.api_key == "custom_key_456"


def test_perplexity_client_no_api_key_error():
    """Test error when no API key is provided"""
    with patch("hypercode.perplexity_client.Config") as mock_config_class:
        mock_config_class.PERPLEXITY_API_KEY = None
        mock_config_class.PERPLEXITY_API_URL = "https://test.api.com"

        with pytest.raises(ValueError, match="Perplexity API key not found"):
            PerplexityClient()
