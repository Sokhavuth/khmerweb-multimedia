#models/postdb/searchdb.py
import setConnection

def call(amount,q):
    mycol = setConnection.call("posts")
    querry = { "title": { "$regex": q } }
    posts = mycol.find(querry).sort([("datetime", -1), ("_id", -1)]).limit(amount)
    items = [post for post in posts]

    return items