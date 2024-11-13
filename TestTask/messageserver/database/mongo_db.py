import pymongo

from app.config import Config

client = pymongo.MongoClient(
    host= [ Config.MONGO_DB_HOST + ":" + Config.MONGO_DB_PORT], 
        serverSelectionTimeoutMS = 3000, # 3 second timeout
        username = Config.MONGO_DB_USER,
        password = Config.MONGO_DB_PASSWORD,)

db = client[Config.MONGO_DB_NAME]

user_collection = db["user"]
message_collection = db["message"]
