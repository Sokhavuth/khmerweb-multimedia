#models/userdb/checkUserDB.py
import setConnection, pymongo, config

def call(email):
    myclient = pymongo.MongoClient(config.kdict['MONGODB_URI'])
    mydb = myclient["multimedia"]
    mycol = mydb["users"]

    myquery = {'email':email}
    user = mycol.find_one(myquery)
    
    return user