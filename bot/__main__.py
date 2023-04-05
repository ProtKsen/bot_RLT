import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command

from bot.config import config
from bot.validators import is_input_valid

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.token)

dp = Dispatcher(bot)


@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message_handler()
async def get_data(message: types.Message):

    if is_input_valid(message.text):
        await message.answer(message.text)
    else:
        await message.answer('Not valid input')


async def main():
    logger.info('start app')
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
