import sqlite3

conn = sqlite3.connect("database.db")
_cursor = conn.cursor()

_cursor.execute("INSERT INTO costumers VALUES ('rafela', 'santos', 'rafasantos@gmail.com')")

conn.commit()
conn.close()