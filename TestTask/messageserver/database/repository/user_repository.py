
from bson import ObjectId
from database.model.user_model import UserModel
from utils.singleton import Singleton

from database.mongo_db import user_collection, db

from automapper import mapper

class UserRepository(metaclass=Singleton):
    
    def insert(self, user: UserModel):
        return mapper.to(UserModel).map(user_collection.insert_one(dict(user)))
    
    def update(self, user: UserModel):
        
        user.messages = [ObjectId(message) for message in user.messages]
        
        result = user_collection.update_one({"userId": user.userId}, {"$set": dict(user)}, True)

        if ( result == None or result.raw_result.get('ok') != 1.0 ):
            return None
        
        user = user_collection.find_one({"userId": user.userId})
        
        if user == None:
            return None

        map_user = mapper.to(UserModel).map(user)

        if map_user != None:
            map_user._id = user["_id"]
        
        return map_user

    def add_message_id(self, id: str, messageId: str):
        result = user_collection.update_one({"_id": ObjectId(id)}, {'$push': {'messages': messageId}})
        
        if ( result == None or result.raw_result.get('ok') != 1.0 ):
            return None
        
        user = user_collection.find_one({"_id": ObjectId(id)})
        
        if user == None:
            return None
        
        map_user = mapper.to(UserModel).map(user)
        
        if map_user != None:
            map_user._id = user["_id"]
        
        return map_user
        
    def find_user_id(self, userId: str):
        
        user = user_collection.find_one({"userId": userId})
        
        if user == None:
            return None

        map_user = mapper.to(UserModel).map(user)
        
        if map_user != None:
            map_user._id = user["_id"]
        
        return map_user

    def find(self, id: str):
        
        user = user_collection.find_one({"_id": ObjectId(id)})

        if user == None:
            return None

        map_user = mapper.to(UserModel).map(user) if user != None else None
        
        if map_user != None:
            map_user._id = user["_id"]
        
        return map_user

