from openpyxl import *
import sqlite3

workbook = load_workbook(r'F:\Prog\Py\b1.xlsx')
sheet = workbook['123']
for num in range(40):
        row_num = num + 26 
        a = sheet['A1' + str(row_num)].value 
sqlite_connection = sqlite3.connect('ltx.db', timeout=10)
cursor = sqlite_connection.cursor()
for sqlite_insert_query in a:
    sqlite_insert_query = """INSERT INTO ltx (Cudnum) VALUES (?)"""
    cursor.execute(sqlite_insert_query,(a,))
    sqlite_connection.commit()
cursor.close() 
sqlite_connection.execute("PRAGMA journal_mode=WAL")
sqlite_connection.close()


 
    
