import sqlite3
sqlite_connection = sqlite3.connect('ltx.db')
cursor = sqlite_connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS mon (
    Id INTEGER PRIMARY KEY,
	Cudnum	TEXT,
	Koatyy	TEXT,
	Area	TEXT,
	District	TEXT,
	Settlement	TEXT,
	City	TEXT,
	Street	TEXT,
	TGName	TEXT,
	PurposeOfTheAssignment	TEXT,
    PurposeOfTheAssignmentNormal TEXT,
	NameOfTheSite	TEXT,
	TransactionType	TEXT,
	Price	TEXT,
	OwnershipType	TEXT,
	RegistrationDate	TEXT,
	RegistrationNumber	TEXT,
	ValueNGO	TEXT,
	EvaluationDate	TEXT
)''')
sqlite_connection.commit()

cursor.close()

