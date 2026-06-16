from fastapi import FastAPI

app = FastAPI()

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
        "source": "Reuters"
    },
    {
        "id": 2,
        "title": "India wins cricket series",
        "category": "Sports",
        "source": "Reuters"
    },
    {
        "id": 3,
        "title": "New space mission announced",
        "category": "Science",
        "source": "Reuters"
    }
]