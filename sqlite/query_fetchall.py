import sqlite3

conn = sqlite3.connect("database.db")
_cursor = conn.cursor()

#Making a Query
_cursor.execute("SELECT * FROM costumers")

#Making a Fetch

#print(_cursor.fetchone())
#print(_cursor.fetchmany(2))
#print(_cursor.fetchall())







print('Comando executado com Sucesso!!!')
conn.commit()
conn.close()