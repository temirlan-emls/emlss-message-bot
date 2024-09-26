import os
from dotenv import load_dotenv
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from core.handlers.base import base_router
from core.utils.commnads import set_commands

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

async def start_bot(bot: Bot) :
    await set_commands(bot)
    await bot.send_message(6736875187, 'Bot is started!')

async def stop_bot(bot: Bot) :
    await bot.send_message(6736875187, 'Bot is stopped!')

dp = Dispatcher()

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.include_router(base_router)

    try:
        await dp.start_polling(bot)
    finally: 
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())


