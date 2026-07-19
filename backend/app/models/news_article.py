from sqlalchemy import Column, Integer, String, Text, DateTime
from app.db.database import Base


class NewsArticle(Base):
    __tablename__ = "news_articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    category = Column(String, nullable=False)
    source = Column(String, nullable=False)
    published_at = Column(DateTime, nullable=False)