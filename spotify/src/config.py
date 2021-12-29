import psycopg2
import pandas

conn = psycopg2.connect(
    host = 'localhost',
    database = 'spotify',
    user = 'postgres',
    port = '5432'
)

audios = pandas.read_sql('SELECT * FROM audios;', conn)
# print(audios)
print(conn)