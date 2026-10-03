from sqlalchemy.orm import Session
from app.models.news_article import NewsArticle
from app.schemas.news import NewsCreate,NewsUpdate
from datetime import datetime
from app.models.user_interest import UserInterest

def get_all_news(db: Session):
    return db.query(NewsArticle).all()

def get_news_by_id(db: Session, news_id:int):
    return db.query(NewsArticle).filter(NewsArticle.id == news_id).first()
    
def get_for_you_news(db:Session,user_id: int):
    categories = (
        db.query(UserInterest.category_id)
        .filter(UserInterest.user_id == user_id)
        .subquery()
    )
    return (
        db.query(NewsArticle)
        .filter(NewsArticle.category_id.in_(categories))
        .all()
    )

def create_news(db:Session, news:NewsCreate):
    article = NewsArticle(
        title = news.title,
        content = news.content,
        category_id = news.category_id,
        source = news.source,
        published_at = datetime.now(),
        url = news.url,
        description = news.description

    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article
def update_news(db:Session,news_id:int, news:NewsUpdate):
    article = get_news_by_id(db, news_id)
    if article is None:
        return None
    article.title = news.title
    article.content = news.content
    article.category_id = news.category_id
    article.source = news.source

    db.commit()
    db.refresh(article)

    return article
def delete_news(db:Session, news_id:int):
    article = get_news_by_id(db,news_id)

    if article is None:
        return None
    db.delete(article)
    db.commit()
    return article