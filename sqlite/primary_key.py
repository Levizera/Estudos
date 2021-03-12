import sqlite3

conn = sqlite3.connect("database.db")
_cursor = conn.cursor()

_cursor.execute("SELECT  rowid, * FROM costumers")

items = _cursor.fetchall()
for item in items:
   print(item)



conn.commit()
conn.close()