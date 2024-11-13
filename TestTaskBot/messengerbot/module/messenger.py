import json
import requests
from bot.config import Config
from data.message_data import MessagesUserData
from data.user_data import UserData
from automapper import mapper

async def send_message(message: str, user: UserData):
    
    data = {"user": user.__dict__, "message": message.__dict__}
    
    response = requests.post(f"http://{Config.SERVER_HOST}/api/v1/message", data=json.dumps(data, default=str))
    
    if (response.status_code == 200):
        return True
    
    print(response)
    
    return False


async def get_messages(start: int, range:int):
    
    response = requests.get(f"http://{Config.SERVER_HOST}/api/v1/messages?start={start}&range={range}")

    if (response.status_code != 200):
        return None
    
    return mapper.to(MessagesUserData).map(json.loads(response.text))
    