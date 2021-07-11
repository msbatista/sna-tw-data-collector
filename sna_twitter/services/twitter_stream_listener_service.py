from numbers import Number

from tweepy import Stream, StreamListener, OAuthHandler
from typing import List


class TwitterStreamListenerService:
    def __init__(self, auth: OAuthHandler, stream_handler: StreamListener, timeout: Number):
        self.stream = Stream(auth=auth,
                             listener=stream_handler,
                             timeout=timeout)

    def stream_tweets(self, track_terms: List[str], languages: List[str] = None):
        if languages is None:
            languages = ["en"]
            try:
                self.stream.filter(languages=languages, track=track_terms)
            except Exception as e:
                print(e)
