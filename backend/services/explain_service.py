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
        db: Session,
        article_id: int,
        audience: str,
    ):
        # 1. Retrieve the article from the database
        article = get_news_by_id(db, article_id)

        if article is None:
            return None

        # 2. Validate the requested audience
        audience = audience.strip().lower()

        if audience not in AUDIENCE_PROMPTS:
            raise ValueError("Invalid audience")

        # 3. Prepare usable article text
        article_text = (
            article.content
            or article.description
            or ""
        ).strip()

        if not article_text:
            raise ValueError("Article has no usable text")

        # 4. Construct the complete prompt
        prompt = f"""
        {BASE_PROMPT}

        Audience-specific instructions:
        {AUDIENCE_PROMPTS[audience]}

        News article:
        Title: {article.title}

        {article_text}
        """

        # 5. Generate the explanation
        explanation = self.ai_client.generate(prompt)

        if not explanation or not explanation.strip():
            raise RuntimeError(
                "The AI returned an empty explanation"
            )

        return explanation.strip()
