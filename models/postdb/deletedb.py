#models/postdb/deletedb.py
import setConnection,  config
from bottle import request

def call(id):
    mycol = setConnection.call("posts")

    userRole = request.get_cookie('userRole', secret=config.kdict['SECRET_KEY'])
    userID = request.get_cookie('userID', secret=config.kdict['SECRET_KEY'])
    post = mycol.find_one({"id": id})

    if(post["authorID"] == userID) or (userRole == "Admin"):
        myquery = { "id": id }
        mycol.delete_one(myquery)