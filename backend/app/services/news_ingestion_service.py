import os
import httpx
from dotenv import  load_dotenv
from sqlalchemy.orm import Session
from app.models.category import Category
from app.db.database import sessionLocal
from datetime import datetime
from app.models.news_article import NewsArticle
load_dotenv()
GNEWS_API_KEY = os.getenv("GNEWS_API_KEY")
class NewsIngestionService:
    def fetch_news(self,category:str):
        url = "https://gnews.io/api/v4/top-headlines"
        params = {
        "apikey":GNEWS_API_KEY,
        "lang":"en",
        "country":"in",
        "max":10,
        "category":category,
        }
        response = httpx.get(url,params = params)
        response.raise_for_status()
        return response.json()
    def get_category_id(self,db:Session,category_name:str):
        category = (
            db.query(Category)
            .filter(Category.name == category_name)
            .first()
        )
        if category is None:
            raise ValueError(
                f"Category '{category_name}' not found"
            )
        return category.id
    def article_exists(self,db:Session,url:str):
        return (
            db.query(NewsArticle)
            .filter(NewsArticle.url == url)
            .first()
            is not None
        )
    def save_article(self,
                    db: Session,
                    article_data: dict,
                    category_id: int,
                    ):
        url = article_data["url"]
        if self.article_exists(db,url):
            print("Article already exists. Skipping")
            return None
        article = NewsArticle(
            title=article_data["title"],
            content=article_data.get("content"),
            category_id=category_id,
            source=article_data["source"]["name"],
            published_at=datetime.fromisoformat(
                article_data["publishedAt"].replace("Z", "+00:00")
            ),
            url = url,
            description=article_data.get("description"),
        )
        db.add(article)
        db.commit()
        db.refresh(article)
        return article
    CATEGORY_MAP = {
    "technology":"Technology",
    "science": "Science",
    "business": "Business",
    "sports": "Sports",
    "health": "Health",
    "entertainment": "Entertainment",
    }
    def ingest_category(self, db:Session,external_category:str):
        category_name = self.CATEGORY_MAP.get(external_category)
        if category_name is None:
            raise ValueError(
                f"Unsupported Category : {external_category}"
            )
        category_id = self.get_category_id(db,category_name)
        data  = self.fetch_news(external_category)
        saved_count  = 0;
        skipped_count = 0;
        for article_data in data["articles"]:
            article = self.save_article(
                db,
                article_data,
                category_id,
            )
            if article is None:
                skipped_count += 1
            else:
                saved_count += 1
        return {
            "category":category_name,
            "fetched": len(data["articles"]),
            "saved":saved_count,
            "skipped":skipped_count,
        }
if __name__ == "__main__":
    service = NewsIngestionService()
    data = service.fetch_news("technology")
    print("Number of articles:", len(data["articles"]))
    for article in data["articles"]:
            print(article["title"])
if __name__ == "__main__":
    service = NewsIngestionService()
    db = sessionLocal()
    try:
        category_name = service.CATEGORY_MAP["technology"]
        category_id = service.get_category_id(
            db,
            category_name
        )
        print("Category:", category_name)
        print("Category ID:", category_id)
    finally:
        db.close()
if __name__ == "__main__":
    db = sessionLocal()
    try:
        external_category = "technology"
        category_name = CATEGORY_MAP[external_category]
        category_id = service.get_category_id(
            db,
            category_name
        )
        data = service.fetch_news(external_category)
        article_data = data["articles"][0]
        article = service.save_article(
            db,
            article_data,
            category_id
        )
        if article is None:
            print("Article was skipped as it already exists...\n")
        else:
            print("Saved article:")
            print(article.id)
            print(article.title)
            print(article.category_id)

    finally:
        db.close()
