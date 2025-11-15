from unittest.mock import Mock, patch

import pytest

from hypercode.perplexity_client import PerplexityClient


@pytest.fixture
def mock_perplexity_client():
    with patch('requests.post') as mock_post:
        mock_response = Mock()
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "Mocked response"}}]
        }
        mock_post.return_value = mock_response
        yield mock_post

def test_perplexity_client_initialization():
    client = PerplexityClient()
    assert client is not None

def test_perplexity_query(mock_perplexity_client):
    client = PerplexityClient()
    response = client.query("test query")
    assert response == {"choices": [{"message": {"content": "Mocked response"}}]}
    mock_perplexity_client.assert_called_once()
