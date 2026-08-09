from sqlalchemy.orm import Session
from ai.gemini_client import GeminiClient
from app.crud.news import get_news_by_id

class SummaryService:
    def __init__(self):
        self.ai_client = GeminiClient()
    def generate_summary(
            self,
            db:Session,
            article_id: int,
    ):
        article = get_news_by_id(db, article_id)

        if article is None:
            return None
        if article.summary:
            return article.summary
        print("Calling Gemini...")
        summary = self.ai_client.generate_summary(article.content)
        article.summary = summary
        db.commit()
        return summary