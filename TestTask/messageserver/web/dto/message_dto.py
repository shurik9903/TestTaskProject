from datetime import datetime
from typing import List, Optional 
from pydantic import BaseModel


class MessageDTO(BaseModel):
    timestamp: Optional[datetime] = None
    message: str
    
class MessageUserDTO(BaseModel):
    user: str
    timestamp: str
    message: str
    

class MessagesUserDTO(BaseModel):
    messages: List[MessageUserDTO]
    total_count: int