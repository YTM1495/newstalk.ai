from pydantic import BaseModel

class CreateUserRequest(BaseModel):
    user_id: int;
    name: str;
    email:str;
