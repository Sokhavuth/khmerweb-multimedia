#models/postdb/getdb.py
import setConnection

def call(id):
    mycol = setConnection.call("posts")

    post = mycol.find_one({"id": id})

    return post