#models/bookdb/deletedb.py
import setConnection

def call(id):
    cursor, connection = setConnection.call()

    cursor.execute("DELETE FROM book WHERE id = ?", (id,))
    
    connection.commit()
    cursor.close()