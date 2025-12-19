"""
Enhanced Perplexity Client for HyperCode

This module provides an enhanced client for interacting with the Perplexity API,
with additional features like rate limiting, retries, and caching.
"""

from typing import Dict, List, Optional, Any, Union
import time
import json
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class EnhancedPerplexityClient:
    """Enhanced client for the Perplexity API with additional features."""
    
    def __init__(self, api_key: str, rate_limit: int = 60, cache_ttl: int = 3600):
        """Initialize the EnhancedPerplexityClient.
        
        Args:
            api_key: The Perplexity API key
            rate_limit: Maximum number of requests per minute
            cache_ttl: Time to live for cached responses in seconds
        """
        self.api_key = api_key
        self.rate_limit = rate_limit
        self.cache_ttl = cache_ttl
        self.last_request_time = 0
        self.request_count = 0
        self.cache: Dict[str, Dict] = {}
    
    def _rate_limit_delay(self):
        """Enforce rate limiting by adding delays between requests."""
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        
        if time_since_last < 60:  # Within the same minute
            if self.request_count >= self.rate_limit:
                # Calculate sleep time to stay within rate limit
                sleep_time = 60 - time_since_last
                time.sleep(sleep_time)
                self.request_count = 0
        else:
            self.request_count = 0
        
        self.last_request_time = time.time()
        self.request_count += 1
    
    def _get_cache_key(self, endpoint: str, params: Dict) -> str:
        """Generate a cache key from endpoint and parameters."""
        return f"{endpoint}:{json.dumps(params, sort_keys=True)}"
    
    def _get_cached(self, cache_key: str) -> Optional[Dict]:
        """Get a cached response if it exists and is not expired."""
        if cache_key in self.cache:
            cached = self.cache[cache_key]
            if datetime.now().timestamp() - cached['timestamp'] < self.cache_ttl:
                return cached['response']
            del self.cache[cache_key]  # Remove expired cache entry
        return None
    
    def _set_cache(self, cache_key: str, response: Dict):
        """Cache a response with the current timestamp."""
        self.cache[cache_key] = {
            'response': response,
            'timestamp': datetime.now().timestamp()
        }
    
    def query(self, prompt: str, model: str = "pplx-7b-online") -> Dict:
        """Send a query to the Perplexity API with rate limiting and caching.
        
        Args:
            prompt: The prompt to send to the API
            model: The model to use for the query
            
        Returns:
            The API response as a dictionary
        """
        # Enforce rate limiting
        self._rate_limit_delay()
        
        # Check cache first
        cache_key = self._get_cache_key("query", {"prompt": prompt, "model": model})
        cached = self._get_cached(cache_key)
        if cached is not None:
            return cached
        
        # Make the actual API request (placeholder - implement actual API call)
        # response = self._make_api_call("query", {"prompt": prompt, "model": model})
        response = {
            "id": "cmpl-1234567890",
            "object": "text_completion",
            "created": int(datetime.now().timestamp()),
            "model": model,
            "choices": [
                {
                    "text": f"This is a simulated response to: {prompt}",
                    "index": 0,
                    "logprobs": None,
                    "finish_reason": "length"
                }
            ],
            "usage": {
                "prompt_tokens": len(prompt.split()),
                "completion_tokens": 50,
                "total_tokens": len(prompt.split()) + 50
            }
        }
        
        # Cache the response
        self._set_cache(cache_key, response)
        
        return response

# Example usage
if __name__ == "__main__":
    client = EnhancedPerplexityClient(api_key="your-api-key-here")
    response = client.query("What is the capital of France?")
    print(response['choices'][0]['text'])
