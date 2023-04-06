import os

from pydantic import BaseModel


class MongoConfig(BaseModel):
    url: str
    username: str
    password: str


class BotConfig(BaseModel):
    name: str
    token: str
    db: MongoConfig


def load_from_env() -> BotConfig:
    name = os.environ['BOT_NAME']
    token = os.environ['BOT_TOKEN']
    mongo_url = os.environ['ME_CONFIG_MONGODB_URL']
    mongo_username = os.environ['MONGO_INITDB_ROOT_USERNAME']
    mongo_password = os.environ['MONGO_INITDB_ROOT_PASSWORD']
    return BotConfig(
        name=name,
        token=token,
        db=MongoConfig(
            url=mongo_url,
            username=mongo_username,
            password=mongo_password
        )
    )


def get_config() -> BotConfig:
    return load_from_env()


config = get_config()
