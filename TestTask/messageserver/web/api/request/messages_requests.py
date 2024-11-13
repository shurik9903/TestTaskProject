from typing import Optional
from pydantic import BaseModel

from web.dto.message_dto import MessageDTO
from web.dto.user_dto import UserDTO

from fastapi import Query

class PostMessagesRequest(BaseModel):
    user: UserDTO
    message: MessageDTO
    
class GetMessagesRangeRequest(BaseModel):
    
    start: Optional[int] = 0
    range: Optional[int] = 0
    
    def __init__(self,
                 start: Optional[int] = Query(0, description="Стартовая позиция получения сообщений"),
                 range: Optional[int] = Query(0, description="Количество сообщений начиная со стартовой позиции")
                 ):
        super().__init__(start=start, range=range)
        # self.start = start
        # self.range = range