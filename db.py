import sqlite3
sqlite_connection = sqlite3.connect('ltx.db')
sqlite_create_table_query = '''CREATE TABLE ltx (
                                id INTEGER PRIMARY KEY,
                               Cudnum TEXT);'''

cursor = sqlite_connection.cursor()
cursor.execute(sqlite_create_table_query)
sqlite_connection.commit()

cursor.close()

