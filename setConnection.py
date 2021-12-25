#setConnection.py
import config, pymongo

def call(collection):
    myclient = pymongo.MongoClient(config.kdict['MONGODB_URI'])
    mongodb = myclient["multimedia"]
    mongocol = mongodb[collection]

    return mongocol