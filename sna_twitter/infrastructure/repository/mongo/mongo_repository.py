from datetime import datetime as dt

from pymongo import MongoClient
from sna_twitter.settings import Settings


class MongoRepository:
    def __init__(self, connection_string: str, database: str, collection: str):
        self._client = MongoClient(connection_string)
        self._db = database
        self._collection = collection

    def bulk_import(self, collection):
        try:
            return self._client[self._db][self._collection].insert_many(documents=collection)
        except Exception as e:
            print(e)

    def insert_document(self, document):
        try:
            print("[{0}]: Id={1}".format(dt.now(), document["id"]))
            return self._client[self._db][self._collection].insert_one(document=document)
        except Exception as e:
            print(e)
