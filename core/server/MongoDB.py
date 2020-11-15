from pymongo import MongoClient


class MongoDB:

    def __init__(self):
        user_name = "fabiticks"
        password = "fabiticks"
        server = "ec2-13-232-83-23.ap-south-1.compute.amazonaws.com"
        port = "27017"
        client = MongoClient(f"mongodb://{user_name}:{password}@:{server}:{port}/fabiticks?authSource=fabiticks")
        self.db = client.fabiticks
