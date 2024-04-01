import psycopg2


def insert_products(conn, products):
    cur = conn.cursor()
    for product in products:
        cur.execute("""
            INSERT INTO product (name, cost_price, sale_price, category_id)
            VALUES (%s, %s, %s, %s)
        """, product)
    conn.commit()
    cur.close()


conn = psycopg2.connect(
    database="postgres", user='postgres',  password='1234', host='127.0.0.1', port='5432'
)

products = [
    ("Phone Case", 5.99, 12.99, 3),
    ("Wireless Mouse", 9.99, 19.99, 3),
    ("Yoga Mat", 15.00, 29.99, 6),
    ("Laptop Bag", 20.00, 39.99, 5),
    ("Coffee Mug", 3.50, 7.99, 4),
    ("Running Shoes", 39.99, 79.99, 8),
    ("Backpack", 25.00, 49.99, 5),
    ("USB Flash Drive", 6.99, 14.99, 1),
    ("Portable Charger", 14.99, 29.99, 3),
    ("Bluetooth Earphones", 29.99, 49.99, 3),
    ("Desk Lamp", 12.99, 24.99, 7),
    ("Cooking Pan", 15.00, 29.99, 5),
    ("Sunglasses", 8.50, 18.99, 9),
    ("Water Bottle", 4.50, 9.99, 2),
    ("Travel Pillow", 10.00, 19.99, 1),
    ("Fitness Tracker", 49.99, 99.99, 7),
    ("Gaming Mousepad", 7.99, 16.99, 3),
    ("Dumbbell Set", 29.99, 59.99, 4),
    ("Bluetooth Speaker", 19.99, 39.99, 6),
    ("Notebook", 3.00, 6.99, 3),
]

insert_products(conn, products)

conn.commit()
conn.close()
