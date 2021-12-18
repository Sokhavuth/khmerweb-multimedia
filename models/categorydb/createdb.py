#models/categorydb/createdb.py
import setConnection

def call(name, link, datetime, id, edit):
    cursor, connection = setConnection.call()

    if not edit:
        cursor.execute("INSERT INTO category VALUES(?, ?, ?, ?)", (name, link, datetime, id))
    else:
        sql = """UPDATE category SET
            name = ?,
            link = ?,
            datetime = ?
            
            WHERE id = ? """

        cursor.execute(sql, (name, link, datetime, id))

    connection.commit()
    cursor.close()