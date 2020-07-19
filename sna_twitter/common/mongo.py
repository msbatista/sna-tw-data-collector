from datetime import datetime as dt

from pymongo import MongoClient
from settings import Settings


class MongoCli:
    def __init__(self):
        self._client = MongoClient(Settings.Mongo.MONGO_CREDENTIALS["STRING_CONN"])
        self._db = Settings.Mongo.MONGO_CREDENTIALS["DATABASE"]
        self._collection = Settings.Mongo.MONGO_CREDENTIALS["COLLECTION"]

    def bulk_import(self, collection):
        try:
            return self._client[self._db][self._collection].insert_many(documents=collection)
        except Exception as e:
            print(e)

    def insert_document(self, document):
        try:
            print("Document Id: ", document["id"], " Created at: ", dt.now())
            return self._client[self._db][self._collection].insert_one(document=document)
        except Exception as e:
            print(e)
