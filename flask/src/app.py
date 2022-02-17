import psycopg2

# Try to connect

try:
    conn=psycopg2.connect("dbname='spotify' user='postgres' host=''localhost")
except:
    print ("I am unable to connect to the database.")

cur = conn.cursor()
try:
    cur.execute("""SELECT 1""")
except:
    print ("I can't SELECT from bar")

rows = cur.fetchall()
print ("\nRows: \n")
for row in rows:
    print ("====")
    print (row)
    print ("====")