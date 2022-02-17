import psycopg2
# import pandas

conn = psycopg2.connect(
    # host = 'pg_spotifyMe',
    host = 'localhost',
    # host = '127.0.0.1',
    database = 'spotify',
    user = 'postgres',
    port = '5432'
)

# audios = pandas.read_sql('SELECT * FROM audios;', conn)
# print(audios)
# print(conn)