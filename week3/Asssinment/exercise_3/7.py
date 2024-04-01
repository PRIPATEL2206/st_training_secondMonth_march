import psycopg2


def fetch_all_products(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM product")
    pro = cur.fetchall()
    cur.close()
    return pro


conn = psycopg2.connect(
    database="postgres", user='postgres',  password='1234', host='127.0.0.1', port='5432'
)

products = fetch_all_products(conn)

# Print the fetched products
for product in products:
    print(product)

products = fetch_all_products(conn)

# Print the fetched products
for product in products:
    print(product)
