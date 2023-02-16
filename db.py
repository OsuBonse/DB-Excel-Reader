import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")

    sqlite_insert_query = """INSERT INTO sqlitedb_developers
                          (id, name, email, joining_date, salary)
                          VALUES
                          (1, 'Oleg', 'oleg04@gmail.com', '2020-11-29', 8100);"""
    count = cursor.execute(sqlite_insert_query)
    sqlite_connection.commit()
    print("Запись успешно вставлена ​​в таблицу sqlitedb_developers ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")