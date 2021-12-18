#models/userdb/paginatedb.py
import setConnection

def call(page, amount):
    cursor, connection = setConnection.call()

    sql = "SELECT * FROM users ORDER BY DATETIME(datetime) DESC, rowid DESC LIMIT ? OFFSET ?"
    cursor.execute(sql, (amount, page*amount))
    users = cursor.fetchall()
    users = [list(user) for user in users]
    Users = []
    for user in users:
        user[5] = str(user[5])
        Users.append(user)

    cursor.close()

    return Users