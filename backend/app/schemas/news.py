from pydantic import BaseModel

class NewsCreate(BaseModel):
    title:str
    content:str
    category:str
    source:str

class NewsUpdate(BaseModel):
        title:str
        content:str
        category:str
        source:str