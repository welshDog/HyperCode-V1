import os

from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("PERPLEXITY_API_KEY")
print(f"API Key: {'*' * (len(api_key) - 4) + api_key[-4:] if api_key else 'Not found'}")
