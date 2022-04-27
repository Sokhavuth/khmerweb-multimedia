#models/postdb/createdb.py
import setConnection, config
from bottle import request

def call(title, thumb, datetime, id, edit, content, category, entries, authorID):
    
    mycol = setConnection.call("posts")

    if not edit:
        post = {
            "id":id,
            "title":title,
            "thumb":thumb,
            "datetime":datetime,
            "content":content,
            "category":category,
            "entries":entries,
            "authorID":authorID
        }
        
        mycol.insert_one(post)
        
    else:
        post = mycol.find_one({"id":edit})
        userRole = request.get_cookie('userRole', secret=config.kdict['SECRET_KEY'])

        if(post["authorID"] == authorID) or (userRole == "Admin"):
            myquery = {"id": edit}
            newvalues = {"$set": {
                    "title":title,
                    "thumb":thumb,
                    "datetime":datetime,
                    "content":content,
                    "category":category,
                    "entries":entries,
                    "authorID":authorID
                }
            }

            mycol.update_one(myquery, newvalues)