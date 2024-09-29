from aiogram import Bot, Router
from aiogram.types import Message 
from aiogram.filters import CommandStart, Command
from aiogram.exceptions import TelegramBadRequest
from aiogram import F
from core.services.gpt import get_data

base_router = Router()

@base_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {(message.from_user.full_name)}!")

@base_router.message(F.text == 'cls')
async def cmd_clear(message: Message, bot: Bot) -> None:
    try:
        for i in range(message.message_id, 0, -1):
            await bot.delete_message(message.from_user.id, i)
    except TelegramBadRequest as ex:
        if ex.message == "Bad Request: message to delete not found":
            print("Все сообщения удалены")

@base_router.message()
async def echo_handler(message: Message) -> None:
    if message.text != 'cls':
        try:
            r = await get_data(message.text)
            r = r['choices'][0]['message']['content']
            print(f'---------\nM:{message.text}\nA:{r}\n---------')
            await message.answer(r)
        except TypeError:
            await message.answer("Nice try!")