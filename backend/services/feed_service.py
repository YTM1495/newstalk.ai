from sqlalchemy.orm import Session
from app.models.category import Category
from app.models.user_interest import UserInterest
from app.models.news_article import NewsArticle

def get_personalized_news(
        db:Session,
        user_id:int,
):
    categories = (
        db.query(Category.name)
        .join(
            UserInterest,
            UserInterest.category_id == Category.id
        )
        .filter(UserInterest.user_id == user_id)
        .all()
    )
    category_names = [category[0] for category in categories]
    print(category_names)
    if not category_names:
        return []
    news = (
        db.query(NewsArticle)
        .filter(NewsArticle.category.in_(category_names))
        .order_by(NewsArticle.published_at.desc())
        .all()
    )
    for article in news:
        print(article.id, article.title, article.category)
    return news