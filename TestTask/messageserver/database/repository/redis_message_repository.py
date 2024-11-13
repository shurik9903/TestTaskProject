import json
from typing import List
from database.model.redis_message_model import RedisMessageModel
from database.redis_db import client
from automapper import mapper

class RedisMessageRepository:
    
    def clear(self):
        client.flushdb()
        
    def messages_exixsts(self):
        return client.exists("messages")
    
    def get_count_messages(self):
        return client.llen("messages")
        
    def insert_message(self, message: RedisMessageModel):
        client.lpush("messages", message)
        
    def insert_messages(self, messages: List[RedisMessageModel]):
        client.lpush("messages",  *[json.dumps(z.__dict__) for z in messages])

        
    def get_all(self) -> List[RedisMessageModel]:
        messages = json.loads(client.lrange("messages", 0, -1)[0].decode())
        return [mapper.to(RedisMessageModel).map(message) for message in messages]
    
    def get_range(self, start: int = 0, end: int = -1, range: int = 0) -> List[RedisMessageModel]:
        
        range = range - 1
        messages =client.lrange("messages", start, start + range if range > 0 else end)

        return [mapper.to(RedisMessageModel).map(json.loads(message)) for message in messages]