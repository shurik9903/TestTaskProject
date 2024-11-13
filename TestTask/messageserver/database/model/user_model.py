from typing import Annotated, List, Optional
from bson import ObjectId
from pydantic import  BaseModel
from utils.annotation import ObjectIdAnnotation


class UserModel(BaseModel):
    _id: Optional[Annotated[ObjectId, ObjectIdAnnotation]] = None
    userId: str
    first_name: str
    last_name: Optional[str] = None
    username: Optional[str] = None
    messages: List[Annotated[ObjectId, ObjectIdAnnotation]] = []