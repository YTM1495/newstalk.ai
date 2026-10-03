from sqlalchemy.orm import Session
from app.models.user_interest import UserInterest
from app.models.news_article import NewsArticle

def get_personalized_news(
        db:Session,
        user_id:int,
):
    category_ids = (
                db.query(UserInterest.category_id)
                .filter(UserInterest.user_id == user_id)
                .all()
            )
    category_ids = [category[0] for category in category_ids]
    print("Category Ids:",category_ids)
    if not category_ids:
        return []
    news = (
        db.query(NewsArticle)
        .filter(NewsArticle.category_id.in_(category_ids))
        .order_by(NewsArticle.published_at.desc())
        .all()
    )
    print("MATCHING ARTICLES:",len(news))
    for article in news:
        print(article.id, article.title, article.category_id)
    return news