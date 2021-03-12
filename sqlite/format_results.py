import sqlite3

conn = sqlite3.connect("database.db")
_cursor = conn.cursor()

### Making a Query
_cursor.execute("SELECT * FROM costumers")

### Making a Fetch

#print(_cursor.fetchone())
#print(_cursor.fetchmany())
#print(_cursor.fetchall())

### Fetching espesific values
#print(_cursor.fetchone()[2])

### Printing each item of the db
items = _cursor.fetchall()
for item in items:
   print(item[0] + ' ' +item[1] + "\t" + item[2])

print('\n Comando executado com Sucesso!!!')

conn.commit()
conn.close()