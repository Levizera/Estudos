import sqlite3

conn = sqlite3.connect("database.db")
_cursor = conn.cursor()

#ORDER BY -> DESC (do maior ao menor), ASC -> (do menor ao maior)
#nome_da_coluna -> Ordena pela forma alfabetica
_cursor.execute('SELECT rowid, * FROM costumers ORDER BY last_name')

items = _cursor.fetchall()
for item in items:
   print(item)
   
conn.commit()
conn.close()