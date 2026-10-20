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
        print("Article ID:", article.id if article else None)
        print("Title:", article.title if article else None)
        print("Content:", repr(article.content) if article else None)
        print("Description:", repr(article.description) if article else None)
        if article is None:
            return None
        if article.summary:
            return article.summary
        Title: {article.title or ""}
        Description: {article.description or ""}
        Content: {article.content or ""}
        article_text = (
        article.content
        or article.description
        or ""
            ).strip()
        if not article_text:
            raise ValueError("Article has no usable text to summarize")
        prompt = f"""
        You are an experienced news editor.

        Summarize the following news article in 3 to 4 sentences.
        Preserve the most important facts.
        Do not add information that is not present in the text.
        Use clear, professional language.
        Return only the summary.
        Article:
        {article_text}
                    """
        print(
            f"Calling Gemini for article {article_id}; "
            f"content length: {len(article.content or '')}; "
            f"description length: {len(article.description or '')}"
        )
        summary = self.ai_client.generate(prompt)
        article.summary = summary
        db.commit()
        return summary
