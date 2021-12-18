#models/categorydb/paginatedb.py
import setConnection

def call(page, amount):
    cursor, connection = setConnection.call()

    sql = "SELECT * FROM category ORDER BY DATETIME(datetime) DESC, rowid DESC LIMIT ? OFFSET ?"
    cursor.execute(sql, (amount, page*amount))
    categories = cursor.fetchall()
    cursor.close()

    return categories