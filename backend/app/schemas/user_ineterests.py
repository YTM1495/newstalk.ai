from pydantic import BaseModel

class UserInterestRequest(BaseModel):
    category_ids : list[int]
    
