from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from bson.objectid import ObjectId


class Conversation(BaseModel):
    class Config:
        arbitrary_types_allowed = True
    usersId: list[ObjectId]
    messages: list[str]
