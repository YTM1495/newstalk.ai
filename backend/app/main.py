from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

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
def news():
   return [
    {
        "id": 1,
        "title": "OpenAI launches new AI model",
        "category": "Technology",
        "source": "Reuters",
        "date": "2025-02-23"
    },
    {
        "id": 2,
        "title": "India wins cricket series",
        "category": "Sports",
        "source": "Reuters",
        "date": "2025-04-13"
    },
    {
        "id": 3,
        "title": "New space mission announced",
        "category": "Science",
        "source": "Reuters",
        "date" : "2025-06-12"
    }
]

@app.get("/instant-news/{minutes}")
def instant_news(minutes:int):
    return {
        "minutes":minutes,
        "articles":[
            "OpenAI launches new AI model",
        "India wins cricket series",
        "New space mission announced"
        ]
    }