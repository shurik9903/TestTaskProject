import logging
from bot.config import Config

import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.handlers import start

logging.basicConfig(level=logging.INFO)

async def main():

    bot = Bot(
        token=Config.BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML,
        ),
    )
    
    dp = Dispatcher()
    
    dp.include_routers(start.router)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
        
if __name__ == "__main__":
    asyncio.run(main())