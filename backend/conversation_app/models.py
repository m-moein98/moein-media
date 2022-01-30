from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from bson.objectid import ObjectId


class Conversation(BaseModel):
    usersId: list[ObjectId]
    messages: list[str]
