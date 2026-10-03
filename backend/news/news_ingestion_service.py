from sqlalchemy.orm import Session
from datetime import datetime

from app. models.news_article import NewsArticle
from news.news_api_client import NewsAPIClient

class NewsIngestionService:

    def __init__(self):
        self.news_client = NewsAPIClient()

    def ingest_articles(
            self,
            db: Session,
            query:str,
            category:str,
            page_size: int = 20,

    ):
        data = self.news_client.search_articles(
            query=query,
            page_size=page_size,
        )
        articles = data.get("articles",[])
        print("Number of articles:", len(articles))
        added_articles = []
        dp = 0
        for article in articles:
            url = article.get("url")

            if not url:
                continue
            existing_article = (
                db.query(NewsArticle)
                .filter(NewsArticle.url == url)
                .first()
            )

            if existing_article:
                dp = dp+1
                continue
            news_article = NewsArticle(
                title = article.get("title"),
                description = article.get("description"),
                content = article.get("content"),
                url = url,
                category = category,
                source = article["source"]["name"],
                published_at = datetime.fromisoformat(
                    article["publishedAt"].replace("Z","+00:00")
                ),
                
            )
            db.add(news_article)
            added_articles.append(news_article)

            db.commit()
        print("Number of duplicates:",dp)
        return added_articles
       