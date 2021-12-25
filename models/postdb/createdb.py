#models/postdb/createdb.py
import setConnection

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
        pass