import sqlite3
from main import DB_NAME, TABLE_NAME, DB_FILE


connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

cursor.execute(f'SELECT * FROM {TABLE_NAME}')
for row in cursor.fetchall():
    _id, name, weight = row
    print(f'ID: {_id}, Name: {name}, Weight: {weight}')

# close the cursor and connection
cursor.close()
connection.close()