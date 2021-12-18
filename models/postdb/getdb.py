#models/postdb/getdb.py
import setConnection

def call(amount):
    cursor, connection = setConnection.call()

    cursor.execute("SELECT * FROM post ORDER BY datetime(datetime) DESC, rowid DESC LIMIT ?", (amount,))
    posts = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM post")
    count = cursor.fetchone()
    
    cursor.close()

    return posts, count[0]