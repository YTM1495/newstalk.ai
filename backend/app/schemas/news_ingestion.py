from pydantic import BaseModel

class NewsIngestionRequest(BaseModel):
    query: str
    category: str
    page_size: int = 20