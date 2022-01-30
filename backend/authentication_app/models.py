from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    userId: str


class User(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    username: str
    password: str
    firstName: Optional[str]
    lastName: Optional[str]
    email: str
    contactsId: Optional[list]
    createdAt: datetime = datetime.utcnow()
    lastSeen: datetime = datetime.utcnow()

class UpdateUser(BaseModel):
    class Config:
        arbitrary_types_allowed = True

    firstName: Optional[str]
    lastName: Optional[str]
    email: str