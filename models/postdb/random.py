#models/postdb/random.py
import setConnection

def call(amount,id=''):
    mycol = setConnection.call("posts")

    pipeline = [{"$match":{'id': {"$ne": id}}},{"$sample":{"size": amount}}]
    results = mycol.aggregate(pipeline)
    posts = [post for post in results]

    return posts
    