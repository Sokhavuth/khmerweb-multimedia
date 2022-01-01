#models/categorydb/createdb.py
import setConnection, config
from bottle import request

def call(name, link, datetime, id, edit):
    mycol = setConnection.call("categories")

    userRole = request.get_cookie('userRole', secret=config.kdict['SECRET_KEY'])

    if (not edit) and (userRole == "Admin"):
        category = {
            "id":id,
            "title":name,
            "thumb":link,
            "datetime":datetime
        }
        
        mycol.insert_one(category)
    else:
        if userRole == "Admin":
            myquery = {"id": edit}
            newvalues = {"$set": {
                    "title":name,
                    "thumb":link,
                    "datetime":datetime
                }
            }

            mycol.update_one(myquery, newvalues)