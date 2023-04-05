import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command

from bot.config import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.token)

dp = Dispatcher(bot)


@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
