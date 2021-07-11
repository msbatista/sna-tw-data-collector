from tweepy import OAuthHandler


class TwitterAuthFactory:
    def __init__(self, consumer_key: str, consumer_secret: str, access_token: str, access_token_secret: str):
        self._consumer_key = consumer_key
        self._consumer_secret = consumer_secret
        self._access_token = access_token
        self._access_token_secret = access_token_secret

    def get_twitter_auth(self) -> OAuthHandler:
        auth = OAuthHandler(consumer_key=self._consumer_key,
                            consumer_secret=self._consumer_secret)
        auth.set_access_token(key=self._access_token,
                              secret=self._access_token_secret)
        return auth
