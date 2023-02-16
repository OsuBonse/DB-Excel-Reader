from openpyxl import *
import sqlite3

workbook = load_workbook(r'...')
sheet = workbook['...']
for num in range(40):
        row_num = num + 26 
        b = sheet['B1' + str(row_num)].value
        c = sheet['C1' + str(row_num)].value
        d = sheet['D1' + str(row_num)].value
sqlite_connection = sqlite3.connect('ltx.db', timeout=10)
cursor = sqlite_connection.cursor()
for sqlite_insert_query in b:
    sqlite_insert_query = """INSERT INTO ltx (Cudnum) VALUES (?)"""
    cursor.execute(sqlite_insert_query,(b,))
    sqlite_connection.commit()
cursor.close() 
sqlite_connection.execute("PRAGMA journal_mode=WAL")
sqlite_connection.close()


 
    
