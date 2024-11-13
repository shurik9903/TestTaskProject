from typing import Optional
from pydantic import BaseModel


class UserData(BaseModel):
    
    userId: str
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
