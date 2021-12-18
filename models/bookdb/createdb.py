#models/postdb/createdb.py
import setConnection

def call(title, thumb, datetime, id, edit, content, chapter, entries, bookTitle):
    cursor, connection = setConnection.call()

    if not edit:
        sql = "INSERT INTO book VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, (title, thumb, datetime, id, content, chapter, entries, bookTitle))
    else:
        sql = """UPDATE book SET
            title = ?,
            thumb = ?,
            datetime = ?,
            content = ?,
            chapter = ?,
            entries = ?,
            bookTitle = ?
            
            WHERE id = ? """

        cursor.execute(sql, (title, thumb, datetime, content, chapter, entries, bookTitle, id))

    connection.commit()
    cursor.close()