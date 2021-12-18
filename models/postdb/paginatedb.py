#models/postdb/paginatedb.py
import setConnection

def call(page, amount):
    cursor, connection = setConnection.call()

    sql = "SELECT * FROM post ORDER BY DATETIME(datetime) DESC, rowid DESC LIMIT ? OFFSET ?"
    cursor.execute(sql, (amount, page*amount))
    posts = cursor.fetchall()
    cursor.close()

    return posts