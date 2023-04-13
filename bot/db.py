from motor import motor_asyncio
from bot.config import config


def get_db():
    client = motor_asyncio.AsyncIOMotorClient(config.db.url)
    db = client.sampleDB
    return db
