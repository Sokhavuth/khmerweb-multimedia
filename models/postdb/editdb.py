#models/postdb/editdb.py
import setConnection

def call(id, amount):
    mycol = setConnection.call("posts")

    posts = mycol.find().sort([("datetime", -1), ("_id", -1)]).limit(amount)
    count = mycol.count_documents({})

    post = mycol.find_one({"id": id})

    return posts, count, post