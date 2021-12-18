#models/postdb/deletedb.py
import setConnection

def call(id):
    cursor, connection = setConnection.call()

    cursor.execute("DELETE FROM post WHERE id = ?", (id,))
    
    connection.commit()
    cursor.close()