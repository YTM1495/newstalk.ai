from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship

class NewsArticle(Base):
    __tablename__ = "news_articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    category_id = Column(Integer,
                         ForeignKey("categories.id"),
                           nullable=False)
    category = relationship("Category")
    source = Column(String, nullable=False)
    published_at = Column(DateTime, nullable=False)
    summary = Column(Text, nullable=True)
    url = Column(Text, nullable=False)
    description = Column(Text, nullable=False)

    