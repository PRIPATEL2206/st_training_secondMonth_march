import psycopg2

conn = psycopg2.connect(
    database="postgres", user='postgres',  password='1234', host='127.0.0.1', port='5432'
)

cur = conn.cursor()

update_queries = [
    "UPDATE product SET cost_price = 11.99 WHERE id = 1",
    "UPDATE product SET cost_price = 22.50 WHERE id = 5",
    "UPDATE product SET cost_price = 8.75 WHERE id = 10"
]

for query in update_queries:
    cur.execute(query)

conn.commit()

cur.close()
conn.close()
