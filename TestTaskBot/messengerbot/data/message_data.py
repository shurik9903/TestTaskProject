import datetime
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class MessageData(BaseModel):
    timestamp: Optional[datetime] = None
    message: str
    
class MessageUserDTO(BaseModel):
    user: str
    timestamp: str
    message: str 
    
class MessagesUserData(BaseModel):
    messages: List[MessageUserDTO]
    total_count: int