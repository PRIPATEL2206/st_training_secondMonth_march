import psycopg2

conn = psycopg2.connect(
    database="postgres", user='postgres',  password='1234', host='127.0.0.1', port='5432'
)

cur = conn.cursor()

cur.execute("""
    SELECT p.id, p.name, p.cost_price, p.sale_price, c.code AS category_code, c.name AS category_name
    FROM product p
    JOIN category c ON p.category_id = c.id
""")
products_with_category_details = cur.fetchall()

for product in products_with_category_details:
    print(product)

cur.close()
conn.close()
