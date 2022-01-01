#models/categorydb/deletedb.py
import setConnection,  config
from bottle import request

def call(id):
    mycol = setConnection.call("categories")

    userRole = request.get_cookie('userRole', secret=config.kdict['SECRET_KEY'])

    if(userRole == "Admin"):
        myquery = { "id": id }
        mycol.delete_one(myquery)