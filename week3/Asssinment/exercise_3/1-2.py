import psycopg2

conn = psycopg2.connect(
    database="postgres", user='postgres', password='1234', host='127.0.0.1', port='5432'
)
cursor = conn.cursor()

cursor.execute("select version()")

data = cursor.fetchone()
print("Connected to: ", data)

conn.close()
