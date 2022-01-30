from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from bson.objectid import ObjectId


class Conversation(BaseModel):
    users: list[ObjectId]
    messages: list[str]
