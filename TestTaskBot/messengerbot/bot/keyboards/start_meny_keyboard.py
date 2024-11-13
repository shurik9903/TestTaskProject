from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, ReplyKeyboardRemove

def get_start_meny_keyboard():
    inline_kb = [
        [
            InlineKeyboardButton(text="Получить сообщения", callback_data="get_messages"),
            InlineKeyboardButton(text="Добавить сообщение", callback_data="message_form")
        ],
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=inline_kb)