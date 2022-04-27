#models/postdb/getdb.py
import setConnection

def call(amount):
    mycol = setConnection.call("posts")

    posts = mycol.find().sort([("datetime", -1), ("_id", -1)]).limit(amount)
    count = mycol.count_documents({})

    mycol = setConnection.call("categories")
    categories = mycol.find().sort('title', 1)

    return posts, count, categories