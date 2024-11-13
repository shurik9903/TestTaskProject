from datetime import datetime
from typing import Annotated, Optional
from bson import ObjectId
from pydantic import BaseModel
from database.model.user_model import UserModel
from utils.annotation import ObjectIdAnnotation


class MessageModel(BaseModel):
    _id: Optional[Annotated[ObjectId, ObjectIdAnnotation]] = None
    user_id_fk: Optional[Annotated[ObjectId, ObjectIdAnnotation]] = None
    timestamp: datetime = None
    message: str
    
class MessageUserModel(BaseModel):
    _id: Optional[Annotated[ObjectId, ObjectIdAnnotation]] = None
    timestamp: datetime = None
    message: str
    user: Optional[UserModel] = None