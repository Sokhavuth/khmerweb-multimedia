#models/categorydb/createdb.py
import setConnection

def call(name, link, datetime, id, edit):
    mycol = setConnection.call("categories")

    if not edit:
        category = {
            "id":id,
            "title":name,
            "thumb":link,
            "datetime":datetime
        }
        
        mycol.insert_one(category)
    else:
        pass