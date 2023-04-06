from pymongo import MongoClient

from bot.config import config


def get_db():
    client = MongoClient(config.db.url)
    db = client.sampleDB
    return db
