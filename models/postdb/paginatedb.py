#models/postdb/paginatedb.py
import setConnection

def call(page, amount):
    mycol = setConnection.call("posts")

    posts = mycol.find({},{"_id":0}).skip(page*amount).sort([("datetime", -1), ("_id", -1)]).limit(amount)

    return posts