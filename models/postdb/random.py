#models/postdb/random.py
import setConnection

def call(amount):
    mycol = setConnection.call("posts")

    pipeline = [{"$sample":{"size": amount}}]
    results = mycol.aggregate(pipeline)
    posts = [post for post in results]

    return posts