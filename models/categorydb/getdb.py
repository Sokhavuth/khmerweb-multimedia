#models/categorydb/getdb.py
import setConnection

def call(amount):
    mycol = setConnection.call("categories")

    categories = mycol.find().sort([("datetime", -1), ("_id", -1)]).limit(amount)
    count = mycol.count_documents({})

    return categories, count