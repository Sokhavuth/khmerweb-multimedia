#models/categorydb/getdb.py
import setConnection

def call(amount):
    cursor, connection = setConnection.call()

    if amount == 'all':
        cursor.execute("SELECT * FROM category ORDER BY name ")
        categories = cursor.fetchall()
        return categories
    else:
        cursor.execute("SELECT * FROM category ORDER BY datetime(datetime) DESC, rowid DESC LIMIT ?", (amount,))
        categories = cursor.fetchall()

    cursor.execute("SELECT COUNT(*) FROM category")
    count = cursor.fetchone()
    
    cursor.close()

    return categories, count[0]