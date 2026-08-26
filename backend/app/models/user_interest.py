from sqlalchemy import Column, String, Integer, ForeignKey
from app.db.database import Base
from app.models.user import User
from app.models.category import Category

class UserInterest(Base):
    __tablename__ = "user_interests"

    user_id = Column(
                    Integer, 
                    ForeignKey("users.id") ,
                    primary_key = True
                    )
    category_id = Column(
                    Integer,
                    ForeignKey("categories.id"),
                    primary_key=True
                    )