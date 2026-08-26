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
        prompt = f"""
        You are an experienced news editor.
        
        Your task is to summarize the following news article.
        
        Rules:
        - Keep the summary between 3 and 4 sentences.
        - Preserve only the most important facts.
        - Do not add information that is not present in the article.
        - Use clear and professional language.
        - Return only the summary.
        
        Article:
        {article.content}
        """    
        print("Calling Gemini...")
        summary = self.ai_client.generate(prompt)
        article.summary = summary
        db.commit()
        return summary