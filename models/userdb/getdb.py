#models/userdb/getdb.py
import setConnection

def call(amount):
    cursor, connection = setConnection.call()

    cursor.execute("SELECT * FROM users ORDER BY datetime(datetime) DESC, rowid DESC LIMIT ?", (amount,))
    posts = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()
    
    cursor.close()

    return posts, count[0]