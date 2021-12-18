#models/userdb/editdb.py
import setConnection, base64

def call(id):
    cursor, connection = setConnection.call()

    cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
    item = cursor.fetchone()
    cursor.close()

    password = base64.b64decode(item[5])
    item = list(item)
    item[5] = password
    
    return item, item[3]