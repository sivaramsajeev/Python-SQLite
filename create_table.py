
import sqlite3

try:
    sqliteConnection = sqlite3.connect('SQLite_Python.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    with open('create_table.sql', 'r') as sqlite_file:
        sql_script = sqlite_file.read()

    cursor.executescript(sql_script)
    print("SQLite script executed successfully")
    cursor.close()

except sqlite3.Error as error:
    print("Error while executing sqlite script", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("sqlite connection is closed")

