import os

from pydantic import BaseModel


class BotConfig(BaseModel):
    name: str
    token: str


def load_from_env() -> BotConfig:
    name = os.environ['BOT_NAME']
    token = os.environ['BOT_TOKEN']
    return BotConfig(name=name, token=token)


def get_config() -> BotConfig:
    return load_from_env()


config = get_config()
