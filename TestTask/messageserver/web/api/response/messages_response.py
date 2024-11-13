from typing import List
from pydantic import BaseModel

from web.dto.message_dto import MessageUserDTO        

class GetMessagesUserResponse(BaseModel):
    messages: List[MessageUserDTO]
    total_count: int