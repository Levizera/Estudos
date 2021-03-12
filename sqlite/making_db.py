import sqlite3

conn = sqlite3.connect("database.db")
_cursor = conn.cursor()

_cursor.execute('''CREATE TABLE costumers (
      first_name text,
      last_name text,
      email_address text
   
   )
''')

conn.commit()
conn.close()
