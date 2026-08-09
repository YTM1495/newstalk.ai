from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.db.database import Base, engine
from fastapi import Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.crud.news import get_all_news,create_news,get_news_by_id,update_news,delete_news
from app.schemas.news import NewsCreate, NewsUpdate
from services.summary_service import SummaryService
Base.metadata.create_all(bind = engine)

app = FastAPI()
summary_service = SummaryService()

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
@app.get("/news")
def get_news(db: Session = Depends(get_db)):
   return get_all_news(db)
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
    
