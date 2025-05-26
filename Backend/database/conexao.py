import psycopg2

def conecta_bd():
    return psycopg2.connect(
        host='localhost',
        database='projeto',
        user='postgres',
        password='Rubinho091123'
    )
