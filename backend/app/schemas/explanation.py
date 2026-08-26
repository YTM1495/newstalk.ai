from pydantic import BaseModel

class ExplanationRequest(BaseModel):
    audience:str