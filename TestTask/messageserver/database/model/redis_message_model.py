from datetime import datetime
from pydantic import BaseModel


class RedisMessageModel(BaseModel):
    user: str
    timestamp: str
    message: str