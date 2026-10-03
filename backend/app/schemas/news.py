from pydantic import BaseModel
from datetime import datetime

class NewsCreate(BaseModel):
    title:str
    content:str
    category_id: int
    source:str
    url: str
    description: str

class NewsUpdate(BaseModel):
        title:str
        content:str
        category_id: int
        source:str
        summary: str | None = None

class NewsResponse(BaseModel):
      id: int
      title: str
      content: str | None
      category: str
      published_at: datetime
      summary: str| None
      url: str
      description:str
      
def article_to_response(article):
    return NewsResponse(
        id=article.id,
        title=article.title,
        content=article.content,
        category=article.category.name,
        source=article.source,
        published_at=article.published_at,
        summary=article.summary,
        url=article.url,
        description=article.description,
    )
