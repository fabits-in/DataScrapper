
# def save_instrument_data(symbol):
#     from pymongo import MongoClient
#     client = MongoClient(
#         "mongodb://fabiticks:fabiticks@ec2-13-232-83-23.ap-south-1.compute.amazonaws.com:27017/fabiticks?authSource=fabiticks")
#     db = client.fabiticks
#     data = symbol_info(symbol)
#     result = db.instruments.insert_one(data)
#     print('One post: {0}'.format(result.inserted_id))


