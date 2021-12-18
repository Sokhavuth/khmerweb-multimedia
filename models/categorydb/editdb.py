#models/categorydb/editdb.py
import setConnection

def call(id):
    cursor, connection = setConnection.call()

    cursor.execute("SELECT * FROM category WHERE id = ?", (id,))
    item = cursor.fetchone()
    cursor.close()

    return item