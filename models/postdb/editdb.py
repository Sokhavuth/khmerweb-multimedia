#models/postdb/editdb.py
import setConnection

def call(id):
    cursor, connection = setConnection.call()

    cursor.execute("SELECT * FROM post WHERE id = ?", (id,))
    item = cursor.fetchone()

    cursor.execute("SELECT * FROM category")
    categories = cursor.fetchall()

    cursor.close()

    return item, categories