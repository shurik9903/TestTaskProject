import math
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.handlers.states.pagination import Pagination

def get_inline_pagination_keyboard(page:int, total:int, range:int):
    
    total_page = math.ceil(total / range)

    pagination_kb = [
        [
            InlineKeyboardButton(text = "←",      callback_data = Pagination(page=page - 1).pack() if page > 0 else '_'),
            InlineKeyboardButton(text = f"{str(page+1)}/{str(total_page)}", callback_data = '_'),
            InlineKeyboardButton(text = "→",      callback_data = Pagination(page=page + 1).pack() if total_page > page + 1 else '_'),
        ],
    ]
    
    return InlineKeyboardMarkup(inline_keyboard=pagination_kb)

