#models/postdb/createdb.py
import setConnection

def call(title, thumb, datetime, id, edit, content, category, entries):
    cursor, connection = setConnection.call()

    if not edit:
        sql = "INSERT INTO post VALUES(?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, (title, thumb, datetime, id, content, category, entries))
    else:
        sql = """UPDATE post SET
            title = ?,
            thumb = ?,
            datetime = ?,
            content = ?,
            category = ?,
            entries = ?
            
            WHERE id = ? """

        cursor.execute(sql, (title, thumb, datetime, content, category, entries, id))

    connection.commit()
    cursor.close()