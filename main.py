import nse

instruments = ["SBIN", "RELIANCE", "ASHOKLEY", "BHARTIARTL", "PVR", "IRCTC", "ITC", "INFY", "POWERGRID", "ACC"]

import json


def symbol_info(symbol):
    instrument_info = json.loads(nse.equity_info(symbol))
    instrument_trade_info = json.loads(nse.equity_trade_info(symbol))
    return {**instrument_info, **instrument_trade_info}


def save_instrument_data(symbol):
    from pymongo import MongoClient
    client = MongoClient(
        "mongodb://fabiticks:fabiticks@ec2-13-232-83-23.ap-south-1.compute.amazonaws.com:27017/fabiticks?authSource=fabiticks")
    db = client.fabiticks
    data = symbol_info(symbol)
    result = db.instruments.insert_one(data)
    print('One post: {0}'.format(result.inserted_id))


for x in instruments:
    save_instrument_data(x)
