from sqlalchemy.orm import Session
from ai.gemini_client import GeminiClient
from app.crud.news import get_news_by_id
from app.prompts.explanation_prompt import (
    BASE_PROMPT,
    AUDIENCE_PROMPTS,
)

class ExplainService:
    def __init__(self):
        self.ai_client = GeminiClient()
    def generate_explanation(
            self,
            db:Session,
            article_id:int,
            audience:str,
    ):
        article = get_news_by_id(db, article_id)
        if article is None:
            return None
        audience = audience.lower()
        if audience not in AUDIENCE_PROMPTS:
            raise ValueError("Invalid audience")
        
        prompt = f"""
    {BASE_PROMPT}
    Audience-specific instructions:
    {AUDIENCE_PROMPTS[audience]}
    Article:{article.content}
"""
        explanation = self.ai_client.generate(prompt)
        return explanation