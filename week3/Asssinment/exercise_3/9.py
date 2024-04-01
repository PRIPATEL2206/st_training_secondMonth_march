import psycopg2

conn = psycopg2.connect(
    database="postgres", user='postgres',  password='1234', host='127.0.0.1', port='5432'
)


cur = conn.cursor()


cur.execute("SELECT * FROM product ORDER BY cost_price")
products_ordered_by_cost_price = cur.fetchall()


for product in products_ordered_by_cost_price:
    print(product)


cur.close()
conn.close()
