from fastapi import FastAPI,HTTPException,Depends
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, engine
from sqlalchemy import inspect 
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.crud.news import get_all_news,create_news,get_news_by_id,update_news,delete_news, get_for_you_news
from app.schemas.news import NewsCreate, NewsUpdate, NewsResponse, article_to_response
from services.summary_service import SummaryService
from app.schemas.explanation import ExplanationRequest
from services.explain_service import ExplainService
from app.models.user import User
from app.models.category import Category
from app.models.user_interest import UserInterest
from app.models.news_article import NewsArticle
from app.seed import seed_categories
from app.db.database import sessionLocal
from app.schemas.user_ineterests import UserInterestRequest
from app.schemas.user import CreateUserRequest
from services.feed_service import get_personalized_news
from news.news_ingestion_service import NewsIngestionService
from app.schemas.news_ingestion import NewsIngestionRequest
from app.crud.user_interest import set_user_interests, get_user_interests_crud
from app.schemas.user_ineterests import UserInterestRequest
from app.schemas.category import CategoryResponse
from app.schemas.common import MessageResponse 


Base.metadata.create_all(bind = engine)
inspector = inspect(engine)
print("tables:",inspector.get_table_names())
print("Columns:",
      [column["name"] for column in inspector.get_columns("news_articles")])

db = sessionLocal()
try:
    seed_categories(db)
finally:
    db.close()
app = FastAPI()
summary_service = SummaryService()

news_ingestion_service = NewsIngestionService()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return{
        "message" : "NewsTalk AI Backend Running..."
           }

@app.get("/news",
         response_model=list[NewsResponse])
def get_news(db: Session = Depends(get_db)):
   articles = get_all_news(db)
   return [
       article_to_response(article)
       for article in articles
   ]

@app.get("/news/{news_id}")
def get_by_id(news_id:int, db:Session = Depends(get_db)):
    article = get_news_by_id(db,news_id)
    if article is None:
        raise HTTPException(
                status_code = 404,
                detail = "The requested Article not Found"
                        )
    return article
    
        
@app.post("/news")
def create_news_endpoint(
    news:NewsCreate,
    db: Session =  Depends(get_db)
    ):
    return create_news(db,news)
@app.put("/news/{news_id}")
def update_news_endpoint(news:NewsUpdate, news_id:int, db:Session = Depends(get_db)):
   article =  update_news(db,news_id,news)
   if article is None:
       raise HTTPException(status_code= 404,
                           detail = "Article not found"
                           )
   return article
@app.delete("/news/{news_id}")
def delete_news_endpoint(news_id:int, db:Session = Depends(get_db)):
    article = delete_news(db,news_id)
    if article is None:
        raise HTTPException(status_code = 404,
                            detail = "Article Not Found"
                            )
    return {
        "message":"Article Deleted Successfully"
    }
@app.post("/news/{article_id}/summary")
def generate_summary_endpoint(
    article_id: int,
    db:Session = Depends(get_db)
):
    try:
        summary = summary_service.generate_summary(
        db,
        article_id
        )
        if summary is None:
            raise HTTPException(
            status_code = 404,
            detail = "article Not Found",
            )
        return {
            "summary":summary
        }
    except RuntimeError:
        raise HTTPException(
            status_code=500,
            detail="Unable to generate summary.",
        )
    
@app.post("/news/{article_id}/explanation")
def generate_explanation_endpoint(
    article_id:int,
    request: ExplanationRequest,
    db:Session = Depends(get_db), 
):
    service = ExplainService()
    try:
        explanation = service.generate_explanation(
            db,
            article_id,
            request.audience,
        )
    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=str(error),
        )
    if explanation is None:
        raise HTTPException(
            status_code=404,
            detail = "Artcile Not Found",
        )
    return {
        "explanation":explanation
    }
@app.get("/categories")
def get_categories(db:Session = Depends(get_db)):
    
    return db.query(Category).all()


@app.post("/user")
def create_user_endpoint(
    user: CreateUserRequest,
    db: Session = Depends(get_db),
):
    existing_user = (db.query(User)
            .filter(User.email == user.email)
            .first())
    if existing_user:
        raise HTTPException(
            status_code=400,
            detail = "User with this email is already registered",
        )
    new_user = User(
        name = user.name,
        email = user.email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@app.post("/news/ingest")
def ingest_news(
    request: NewsIngestionRequest,
    db: Session = Depends(get_db),
):
    articles = news_ingestion_service.ingest_articles(
        db = db,
        query = request.query,
        category=request.category,
        page_size=request.page_size,
    )

    return{
        "message":"News ingestion Completed",
        "articles_added":len(articles),
    }
@app.post("/users/{user_id}/interests",
          response_model=MessageResponse,
          )
def update_user_interests(
    user_id: int,
    request: UserInterestRequest,
    db: Session = Depends(get_db),
):
    try:
        categories = set_user_interests(
            db,
            user_id,
            request.category_ids,
        )
        print("Categories:",categories)
    except ValueError as error:
        raise HTTPException(
            status_code=400,
                   detail=str(error)
            )
    if categories is None:
        raise HTTPException(
            status_code=404,
            detail="User Not Found",
        )
    return {
        "message":"Interests updated Successfully"
    }
@app.get("/users/{user_id}/interests",
         response_model=list[CategoryResponse])
def get_user_interests(
    user_id: int,
    db: Session = Depends(get_db),
):
    categories = get_user_interests_crud(db,user_id)

    if categories is None:
        raise HTTPException(
            status_code=404,
            detail="User not Found",
        )
    return categories

@app.get("/feed/for-you",
         response_model=list[NewsResponse],
         )
def for_you_endpoint(
    user_id: int,
    db: Session = Depends(get_db),
): 
   articles = get_personalized_news(db,user_id)
   return [
       article_to_response(article)
       for article in articles
   ]