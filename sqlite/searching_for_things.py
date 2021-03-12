import sqlite3

conn = sqlite3.connect("database.db")
_cursor = conn.cursor()

# WHERE, LIKE, SELECT, FROM
_cursor.execute("SELECT * FROM costumers WHERE last_name LIKE 'fer%'")

items = _cursor.fetchall()
for item in items:
   print(item)

 

conn.commit()
conn.close()