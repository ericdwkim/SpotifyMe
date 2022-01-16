import psycopg2
# import pandas

conn = psycopg2.connect(
   #  host = 'pg_spotifyMe',
    host = 'localhost',
   #  host = 'ec2-3-135-127-249.us-east-2.compute.amazonaws.com',
    database = 'spotify',
    user = 'postgres',
    port = '5432'
)

# audios = pandas.read_sql('SELECT * FROM audios;', conn)
# print(audios)
# print(conn)
