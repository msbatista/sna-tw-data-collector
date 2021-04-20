from tweepy import Stream


class StreamListener:
    def __init__(self, auth, stream_handler, timeout):
        self.stream = Stream(auth=auth, listener=stream_handler, timeout=timeout)

    def stream_tweets(self, track, languages=None):
        if languages is None:
            languages = ["en"]
            try:
                self.stream.filter(languages=languages, track=track)
            except Exception as e:
                print(e)