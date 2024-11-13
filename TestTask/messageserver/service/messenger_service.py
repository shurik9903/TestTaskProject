
from typing import List
from database.model.message_model import MessageModel, MessageUserModel
from database.model.redis_message_model import RedisMessageModel
from database.model.user_model import UserModel

from database.repository.message_repository import MessageRepository
from database.repository.redis_message_repository import RedisMessageRepository
from database.repository.user_repository import UserRepository

from utils.singleton import Singleton

from datetime import datetime, timezone

from web.dto.message_dto import MessageUserDTO, MessagesUserDTO

from automapper import mapper

class MessengerService(metaclass=Singleton):
    
    message_repository: MessageRepository = MessageRepository()
    user_repository: UserRepository = UserRepository()
    redis_message_repository: RedisMessageRepository = RedisMessageRepository()
    
    
    def send_message(self, user: UserModel, message: MessageModel):
        
        self.message_repository.find_all_messages_user()
        
        self.redis_message_repository.clear()
        
        if (message.timestamp == None):
            message.timestamp = datetime.now(timezone.utc)
        
        self.__update_user_insert_message(user, message)
        
        messages = self.message_repository.find_all_messages_user()
        
        self.__update_redis_cache(messages)
        
    def get_messages(self, start:int = 0, range:int = 0):
        
        if (self.redis_message_repository.messages_exixsts() != 1):
            messages = self.message_repository.find_all_messages_user()
            self.__update_redis_cache(messages)

        messages = self.redis_message_repository.get_range(start=start, range=range)
        count = self.redis_message_repository.get_count_messages()
        messages = [mapper.to(MessageUserDTO).map(message) for message in messages]
        return MessagesUserDTO(messages = messages, total_count = count)
        
    def __update_user_insert_message(self, user: UserModel, message: MessageModel):
        
        find_user = self.user_repository.find_user_id(user.userId)
        
        if (self.user_repository.find_user_id(user.userId) != None):
            user.messages = find_user.messages
        
        user = self.user_repository.update(user)
        
        if (user == None):
            raise Exception("Error create user")
        
        message.user_id_fk = user._id

        message = self.message_repository.insert(message)
        self.user_repository.add_message_id(user._id, message._id)
       
    def __update_redis_cache(self, messages = List[MessageUserModel]):
        
        redis_messages: List[RedisMessageModel] = [
            RedisMessageModel(
                user=message.user.first_name,
                message=message.message,
                timestamp=str(message.timestamp)
                )
            for message in messages
        ]
    
        self.redis_message_repository.insert_messages(redis_messages)
           