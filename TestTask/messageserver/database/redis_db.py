import redis

from app.config import Config

client = redis.Redis(host=Config.REDIS_DB_HOST, port=Config.REDIS_DB_PORT, password=Config.REDIS_DB_PASSWORD)