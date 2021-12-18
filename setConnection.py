#setConnection.py
import sqlite3, config

def call():
    connection = sqlite3.connect(config.kdict['DATABASE_URI'])
    cursor = connection.cursor()

    return cursor, connection