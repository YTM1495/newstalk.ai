import os
import httpx
from dotenv import load_dotenv

load_dotenv()

class NewsAPIClient:

    BASE_URL = "https://newsapi.org/v2/top-headlines"

    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")

        if not self.api_key:
            raise RuntimeError("NEWS_API_KEY is not configured")
    def get_top_headlines(
            self,
            country: str = "us",
            page_size: int = 20,
    ):
        params = {
            "apikey": self.api_key,
            "country": country,
            "pageSize": page_size,
        }

        response = httpx.get(
            self.BASE_URL,
            params = params,
            timeout = 10,
        )

        response.raise_for_status()

        return response.json()
    def search_articles(
            self,
            query: str,
            page_size: int = 20,
    ):
        params = {
            "apikey": self.api_key,
            "q": query,
            "pageSize": page_size,
        }
        response = httpx.get(
            "https://newsapi.org/v2/everything",
            params = params,
            timeout=10,
        )
        response.raise_for_status()
        return response.json()