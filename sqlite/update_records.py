import sqlite3

conn = sqlite3.connect("database.db")
_cursor = conn.cursor()

# WHERE, LIKE, SELECT, FROM
_cursor.execute("""UPDATE costumers SET last_name = 'Silva' WHERE rowid = 2 
   """)

_cursor.execute("SELECT rowid, * FROM costumers")
items = _cursor.fetchall()

for item in items:
   print(item)
print('\n Comando executado com Sucesso!!')


conn.commit()
conn.close()