import os

from decouple import config

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(ROOT)


class Settings:
    class Twitter:
        TWITTER_AUTH_KEYS = {
            "CONSUMER_KEY": config("CONSUMER_KEY"),
            "CONSUMER_SECRET": config("CONSUMER_SECRET"),
            "ACCESS_TOKEN": config("ACCESS_TOKEN"),
            "ACCESS_TOKEN_SECRET": config("ACCESS_TOKEN_SECRET")
        }

    class Mongo:
        MONGO_CREDENTIALS = {
            "STRING_CONN": config("MONGO_CONN_STRING"),
            "DATABASE": config("MONGO_DB"),
            "COLLECTION": config("MONGO_COLLECTION")
        }
