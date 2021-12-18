#models/categorydb/deletedb.py
import setConnection

def call(id):
    cursor, connection = setConnection.call()

    cursor.execute("DELETE FROM category WHERE id = ?", (id,))
    
    connection.commit()
    cursor.close()