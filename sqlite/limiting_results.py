import sqlite3

conn = sqlite3.connect("database.db")
_cursor = conn.cursor()

# Para apagar um Table basta dar o seguinte comando
# _cursor.execute('DROP TABLE costumers')

_cursor.execute("SELECT rowid, * FROM costumers LIMIT 4")

items = _cursor.fetchall()
for item in items:
   print(item)
   
conn.commit()
conn.close()