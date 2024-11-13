import logging
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters.command import Command

from aiogram.fsm.context import FSMContext

from bot.handlers.states.message import MessageForm
from bot.handlers.states.pagination import Pagination
from bot.keyboards.pagination_keyboard import get_inline_pagination_keyboard
from bot.keyboards.start_meny_keyboard import get_start_meny_keyboard
from data.message_data import MessageData
from data.user_data import UserData
from module.messenger import get_messages, send_message

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    
   
    
    await message.answer("Приветствую! С какой целью ты прибыл?", reply_markup=get_start_meny_keyboard())
    
    
@router.callback_query(F.data == 'get_messages')
async def message_callback(call: CallbackQuery):
    
    messages = await get_messages(0, 10)
    
    text_messages = [message.message for message in messages.messages]
    
    await call.message.answer("\n".join(text_messages), reply_markup=get_inline_pagination_keyboard(0, messages.total_count, 10))
    
    
# Для получения данных из CallbackData необходимо использовать ключевое слово callback_data, иное слово приведет к ошибке
@router.callback_query(Pagination.filter())
async def messages_pagination_callback(callback: CallbackQuery, callback_data: Pagination ):
   
    page = callback_data.page
    
    messages = await get_messages(page * 10, (page * 10) + 10)
    text_messages = [message.message for message in messages.messages]
    
    await callback.message.edit_text("\n".join(text_messages))
    await callback.message.edit_reply_markup(  
        reply_markup=get_inline_pagination_keyboard(page, messages.total_count, 10)  
    )

@router.callback_query(F.data == 'message_form')
async def message_callback(call: CallbackQuery, state: FSMContext):
    
    await state.set_state(MessageForm.message)
    
    await call.message.answer("Напишите ваше сообщение!")
    
    
@router.message(MessageForm.message)
async def process_message(message: Message) -> None:
    
    message_data = MessageData(message=message.text, timestamp=message.date)
    user_data = UserData(
        userId=str(message.from_user.id),
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        username=message.from_user.username
        )
    
    result:bool = await send_message(message_data, user_data)
    
    msg = "Сообщение отправлено!" if result else "Не удалось отправить это сообщение. Попробуйте отправить его позднее."
    
    await message.answer(msg, reply_markup=get_start_meny_keyboard())


    
@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:

    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info("Cancelling state %r", current_state)
    await state.clear()
    await message.answer(
        "Отменено.",
        reply_markup=ReplyKeyboardRemove(),
)