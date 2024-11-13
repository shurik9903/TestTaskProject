from os import getenv

from utils.singleton import Singleton

class Config(metaclass=Singleton):
    
    MONGO_DB_PORT = str(getenv('MONGO_DB_PORT', default=27017))
    MONGO_DB_HOST = getenv('MONGO_DB_HOST', default='localhost')
    MONGO_DB_NAME = getenv('DB_NAME', default='messages')
    MONGO_DB_USER = getenv('MONGO_DB_USER', default='admin')
    MONGO_DB_PASSWORD = getenv('MONGO_DB_PASSWORD', default='admin')
    
    REDIS_DB_HOST = getenv('REDIS_DB_HOST', default='localhost')
    REDIS_DB_PORT = str(getenv('REDIS_DB_PORT', default=6379))
    REDIS_DB_USER = getenv('REDIS_DB_USER', default='admin')
    REDIS_DB_PASSWORD = getenv('REDIS_DB_PASSWORD', default='admin')
