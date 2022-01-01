import psycopg2
import pandas

conn = psycopg2.connect(
    # host = '192.168.144.2', # db IPAddress
    host = 'localhost',
    database = 'spotify',
    user = 'postgres',
    port = '5432'
)

audios = pandas.read_sql('SELECT * FROM audios;', conn)
# print(audios)
# print(conn)