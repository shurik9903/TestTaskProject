from os import getenv

from utils.singleton import Singleton

class Config(metaclass=Singleton):
    
    BOT_TOKEN = getenv('BOT_TOKEN', default="")
    
    SERVER_HOST = getenv('SERVER_HOST', default='127.0.0.1:8000')

