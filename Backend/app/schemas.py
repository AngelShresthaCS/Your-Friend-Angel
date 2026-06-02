from pydantic import BaseModel
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class User(BaseModel):
    username: str
    name: Optional[str] = None
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)

    class Config:
        orm_mode = True

class ValidateUser(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=72)

class ValidateMessage(BaseModel):
    receiver: str
    content: str
    user: str
    password: str


