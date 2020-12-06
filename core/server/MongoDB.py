from pymongo import MongoClient
from . import credential


class MongoDB:

    def __init__(self):
        client = MongoClient(credential.mongodb_url)
        self.db = client.fabiticks

    def write_historical_data(self, data):
        self.db["historical_data"].insert_many(data)

    def write_instrument_data(self, symbol, data):
        self.db["instruments"].update({"symbol": symbol}, data, True)

    def write_financial_data(self, data):
        self.db["financial_data"].insert_many(data)

    def delete(self, query):
        self.db["historical_data"].delete_many(query)

    def delete1(self, query):
        self.db["financial_data"].delete_many(query)


