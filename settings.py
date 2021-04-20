import os
import urllib.parse

from decouple import config

ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(ROOT)


class Settings:
    TWITTER_AUTH_KEYS = {
        "CONSUMER_KEY": config("CONSUMER_KEY"),
        "CONSUMER_SECRET": config("CONSUMER_SECRET"),
        "ACCESS_TOKEN": config("ACCESS_TOKEN"),
        "ACCESS_TOKEN_SECRET": config("ACCESS_TOKEN_SECRET")
    }

    MONGO_CREDENTIALS = {
        "STRING_CONN": config("MONGO_CONN_STRING").format(urllib.parse.quote_plus(config("MONGO_USERNAME")),
                                                          urllib.parse.quote_plus(config("MONGO_PASSWORD"))),
        "DATABASE": config("MONGO_DB"),
        "COLLECTION": config("MONGO_COLLECTION")
    }
