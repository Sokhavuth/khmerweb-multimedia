#models/userdb/createdb.py
import setConnection

def call(name, thumb, datetime, id, email, password, content, role, entries, edit):
    cursor, connection = setConnection.call()

    if not edit:
        sql = "INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, (name, thumb, datetime, id, email, password, content, role, entries))
    else:
        sql = """UPDATE users SET
            name = ?,
            thumb = ?,
            datetime = ?,
            email = ?,
            password = ?,
            content = ?,
            role = ?,
            video = ?
            
            WHERE id = ? """

        cursor.execute(sql, (name, thumb, datetime, email, password, content, role, entries, id))

    connection.commit()
    cursor.close()