
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException

from automapper import mapper

from database.model.message_model import MessageModel
from database.model.user_model import UserModel

from service.messenger_service import MessengerService
import web.api.request.messages_requests as request
import web.api.response.messages_response as response
from web.dto.message_dto import MessagesUserDTO
from web.exception.http_error import HTTPError

from web.api.description import api_get_messages, api_post_message

router = APIRouter(
    prefix="/api/v1",
    tags=["messages"],
    responses={404: {"messages": "Not found"}}
)

messenger_service: MessengerService = MessengerService()

@router.get("/messages", responses={
        200: {
            "model": MessagesUserDTO
            
            },
        500: {
            "model": HTTPError,
            "description": "Internal Server Error",
            },
        
        }, description=api_get_messages)
def get_all_messages(request: Annotated[request.GetMessagesRangeRequest, Depends()]):
    
    try:
        return messenger_service.get_messages(request.start, request.range)
    except HTTPException as http_error:
        print(http_error)
        raise http_error
    except Exception as error:
        print(error)
        raise HTTPException(500, detail="Ошибка при отправке сообщения!")


@router.post("/message", status_code=200, 
             responses={
        500: {
            "model": HTTPError,
            "description": "Internal Server Error",
            },
        },
        description=api_post_message)
def send_messages(request: request.PostMessagesRequest):

    user = mapper.to(UserModel).map(request.user)
    message = mapper.to(MessageModel).map(request.message)
    
    try:
        messenger_service.send_message(user, message)
    except Exception as error:
        print(error)
        raise HTTPException(500, detail="Ошибка при отправке сообщения!")
        
        
    return None
