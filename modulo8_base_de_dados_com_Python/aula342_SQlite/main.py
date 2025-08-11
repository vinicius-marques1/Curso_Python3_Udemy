import sqlite3
from pathlib import Path

DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# Create Table
cursor.execute(f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
                '('
                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
                'name TEXT,'
                'weight REAL'
                ')'
               )
connection.commit()


# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)

# Registrar valores nas colunas da tabela
# CUIDADO: sql injection
sql = (
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) '
    'VALUES '
    '(?, ?)'
    )
# cursor.execute(sql, ('Luiz', 100.5))
cursor.executemany(sql, [
    ('Luiz', 100.5),
    ('Maria', 60.0)
])
connection.commit()

# Update valores
cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET name = ?, weight = ? '
    'WHERE id = ?',
    ('João', 80.0, 1)
)
connection.commit()

# close the cursor and connection
cursor.close()
connection.close()