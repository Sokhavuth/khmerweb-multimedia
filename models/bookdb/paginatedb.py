#models/bookdb/paginatedb.py
import setConnection

def call(page, amount):
    cursor, connection = setConnection.call()

    sql = "SELECT * FROM book ORDER BY DATETIME(datetime) DESC, rowid DESC LIMIT ? OFFSET ?"
    cursor.execute(sql, (amount, page*amount))
    books = cursor.fetchall()
    cursor.close()

    return books