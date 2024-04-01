import psycopg2

conn = psycopg2.connect(
    database="postgres", user='postgres',  password='1234', host='127.0.0.1', port='5432'
)


cur = conn.cursor()


cur.execute("SELECT * FROM product LIMIT 1")
first_product = cur.fetchone()


print("First Product:", first_product)


cur.close()
conn.close()
