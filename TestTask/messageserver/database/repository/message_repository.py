from typing import List

from bson import ObjectId
from database.model.message_model import MessageModel, MessageUserModel
from utils.singleton import Singleton

from database.mongo_db import message_collection

from automapper import mapper

class MessageRepository(metaclass=Singleton):
    
    def insert(self, message: MessageModel) -> MessageModel:
        
        result = message_collection.insert_one(dict(message))
        message = message_collection.find_one({"_id": result.inserted_id})

        map_message = mapper.to(MessageModel).map(message)
        map_message._id = message["_id"]

        return map_message
    
    def find_all(self) -> List[MessageModel]:
        messages = message_collection.find({})
        
        map_messages = [mapper.to(MessageModel).map(message) for message in messages]
        
        return map_messages
    
    def find_all_user_messages(self, user_id: str) -> List[MessageModel]:
        messages = message_collection.find({"_id": ObjectId(user_id)})
        
        map_messages = [mapper.to(MessageModel).map(message) for message in messages]
        
        return map_messages
    
    def find_all_messages_user(self, start: int = 0, range: int = 0) -> List[MessageUserModel]:
        
        aggregate = [{
                "$lookup":
                    {
                        "from": "user",
                        "localField": "user_id_fk",
                        "foreignField": "_id",
                        "pipeline": [
                            {"$project": {"_id": 1, "userId":1,  "first_name": 1, "last_name": 1, "username":1}}
                            ],
                        "as": "user"
                    }
            }]
        
        if (range > 0 and start > 0):
            aggregate.append({"$limit": start + range})
            aggregate.append({"$skip": start},)
        
        aggregate.append({"$project": {"_id": 1, "message": 1, "timestamp": 1, "user": { "$arrayElemAt": [ "$user", 0 ] }}})
        
        result = message_collection.aggregate(aggregate)
        
        if result == None:
            return []
        
        
        messages = [mapper.to(MessageUserModel).map(message) for message in list(result)]

        return messages