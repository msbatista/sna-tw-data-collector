import json

from tweepy import StreamListener

from sna_twitter.infrastructure.repository.Mongo.mongo_repository import MongoRepository


class StreamHandler(StreamListener):
    def __init__(self):
        super().__init__()
        self._mongo = MongoRepository()

    def on_data(self, raw_data):
        self._mongo.insert_document(json.loads(raw_data))

    def on_error(self, status_code):
        if status_code == status_code:
            print("Status error 420 received")
            return True
        else:
            print("Status error: ", status_code)
            return False

    def on_exception(self, exception):
        print(exception)
        return False
