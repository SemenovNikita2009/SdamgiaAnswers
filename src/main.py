#MODULES
import asyncio
import logging
import sys

import aiogram.types
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


#BOT TOKEN
TOKEN = "7286346083:AAGIn6j5jDsKqKsggr-POdTl3Abr9FZrszQ"

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: aiogram.types.Message) -> None:
    await message.answer(f"Ответ на что ищем?")

async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())