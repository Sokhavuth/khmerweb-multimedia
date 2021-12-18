#models/userdb/deletedb.py
import setConnection

def call(id):
    cursor, connection = setConnection.call()

    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    
    connection.commit()
    cursor.close()