#models/postdb/editdb.py
import setConnection

def call(id, amount):
    mycol = setConnection.call("categories")

    categories = mycol.find().sort([("datetime", -1), ("_id", -1)]).limit(amount)
    count = mycol.count_documents({})

    category = mycol.find_one({"id": id})

    return categories, count, category