import asyncio
import json
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command

from bot.config import config
from bot.db import get_db
from bot.validators import is_input_valid
from datetime import datetime
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.token)

dp = Dispatcher(bot)

db = get_db()


@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message_handler()
async def get_data(message: types.Message):

    if is_input_valid(message.text):
        request = json.loads(message.text)
        start = datetime.fromisoformat(request['dt_from'])
        stop = datetime.fromisoformat(request['dt_upto'])

        if request['group_type'] == 'month':
            format = "%Y-%m-01T00:00:00"
        elif request['group_type'] == 'day':
            format = "%Y-%m-%dT00:00:00"
        elif request['group_type'] == 'hour':
            format = "%Y-%m-%dT%H:00:00"

        query = db.sample_collection.aggregate([
            {'$match': {'dt': {'$gte': start, '$lt': stop}}},
            {'$densify': {
                'field': 'dt',
                'range': {
                    'step': 1,
                    'unit': request['group_type'],
                    'bounds': [start, stop]}}
            },
            {'$fill': {
                'sortBy': {'dt': 1},
                'output': {
                    'value': {'value': 0}}}
            },
            {'$group': {
                '_id': {'$dateToString': {'date': '$dt', 'format': format}},
                'value': {'$sum': '$value'}}
            },
            {'$sort': {'_id': 1}}
        ])

        answer = {'dataset': [], 'labels': []}

        for entity in query:
            answer['dataset'].append(entity['value'])
            answer['labels'].append(entity['_id'])

        await message.answer(answer)
    else:
        await message.answer('Not valid input')


async def main():
    logger.info('start app')
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
