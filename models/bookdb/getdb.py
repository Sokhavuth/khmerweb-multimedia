#models/bookdb/getdb.py
import setConnection

def call(amount):
    cursor, connection = setConnection.call()

    cursor.execute("SELECT * FROM book ORDER BY datetime(datetime) DESC, rowid DESC LIMIT ?", (amount,))
    books = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM book")
    count = cursor.fetchone()
    
    cursor.close()

    return books, count[0]