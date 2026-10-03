from sqlalchemy.orm import Session
from app.models.user import User
from app.models.category import Category
from app.models.user_interest import UserInterest

def set_user_interests(
        db:Session,
        user_id: int,
        category_ids: list[int]
):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return None
    categories = (
        db.query(Category)
        .filter(Category.id.in_(category_ids))
        .all()
)
   
    if len(categories) != len(set(category_ids)):
        raise ValueError("Some categories do not exist")

    db.query(UserInterest).filter(
        UserInterest.user_id == user_id
    ).delete()

    for ct_id in category_ids:
        db.add(
            UserInterest(
                user_id = user_id,
                category_id = ct_id,
            )
        )
    db.commit()
    return categories
def get_user_interests_crud(
        db: Session,
        user_id: int,
):
    user = db.query(User).filter(User.id == user_id).first()

    if user is None:
        return None

    categories = (
        db.query(Category)
        .join(
            UserInterest,
            UserInterest.category_id == Category.id
        )
        .filter(UserInterest.user_id == user_id)
        .all()
    )
    return categories