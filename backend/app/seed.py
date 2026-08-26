from sqlalchemy.orm import Session
from app.models.category import Category

DEFAULT_CATEGORIES = [
    "Technology",
    "AI & Machine Learning",
    "Science",
    "Finance",
    "Business",
    "Politics",
    "Sports",
    "Entertainment",
    "Health",
    "Education",
    "Environment",
    "World",
    "India",
    "Startups",
]

def seed_categories(db:Session):
    for category_name in DEFAULT_CATEGORIES:
        existing_category = (
            db.query(Category)
            .filter(Category.name == category_name)
            .first()
        )
        if existing_category is None:
            db.add(Category(name = category_name))
    db.commit()