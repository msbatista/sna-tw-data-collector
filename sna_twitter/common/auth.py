from tweepy import OAuthHandler

from settings import Settings


class TwitterAuth:
    def __init__(self):
        self._consumer_key = Settings.TWITTER_AUTH_KEYS["CONSUMER_KEY"]
        self._consumer_secret = Settings.TWITTER_AUTH_KEYS["CONSUMER_SECRET"]
        self._access_token = Settings.TWITTER_AUTH_KEYS["ACCESS_TOKEN"]
        self._access_token_secret = Settings.TWITTER_AUTH_KEYS["ACCESS_TOKEN_SECRET"]

    def get_twitter_auth(self):
        auth = OAuthHandler(consumer_key=self._consumer_key,
                            consumer_secret=self._consumer_secret)
        auth.set_access_token(key=self._access_token,
                              secret=self._access_token_secret)
        return auth
