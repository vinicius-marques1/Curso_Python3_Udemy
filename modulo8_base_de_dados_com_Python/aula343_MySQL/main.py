# Doc: https://pymysql.readthedocs.io/en/latest/
# Pypy: https://pypi.org/project/pymysql/
# GitHub: https://github.com/PyMySQL/PyMySQL
import pymysql
import os
from dotenv import load_dotenv
load_dotenv(override=True)

TABLE_NAME = 'customers'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    password=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE'],
)

with connection:
    with connection.cursor() as cursor:
        # SQL
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'nome VARCHAR(50) NOT NULL, '
            'idade INT NOT NULL, '
            'PRIMARY KEY (id)'
            ') '
        )
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()
    

    with connection.cursor() as cursor:
        # SQL
        cursor.execute(
            f'INSERT INTO {TABLE_NAME} ' 
            '(nome, idade) VALUES (%s, %s)',
            ('Maria', 24)
        )
        cursor.execute(
            f'INSERT INTO {TABLE_NAME} ' 
            '(nome, idade) VALUES (%(nome)s, %(idade)s)',
            {'nome': 'João', 'idade': 30}
        )
    connection.commit()

    with connection.cursor() as cursor:
        sql_query = (
            f'INSERT INTO {TABLE_NAME} '
            '(nome, idade) VALUES (%s, %s)'
        )
        data = [
            ('Ana', 22),
            ('Pedro', 28),
            ('Lucas', 35)
        ]
        cursor.executemany(sql_query, data)
    connection.commit()

    # Lendo os dados
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM {TABLE_NAME}')
        result = cursor.fetchall()
        for id, name, age in result:
            print('ID:', id, 'Nome:', name, 'Idade:', age)