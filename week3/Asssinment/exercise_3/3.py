import psycopg2

conn = psycopg2.connect(
    database="postgres", user='postgres', password='1234', host='127.0.0.1', port='5432'
)
cur = conn.cursor()

cur.execute("CREATE SEQUENCE product_id_seq START 1 INCREMENT 1;")

# Create table
cur.execute("""
    CREATE TABLE product (
        id INTEGER PRIMARY KEY DEFAULT nextval('product_id_seq'),
        name VARCHAR(255),
        cost_price NUMERIC,
        sale_price NUMERIC,
        CONSTRAINT check_prices CHECK (sale_price > cost_price)
    );
""")

conn.commit()
conn.close()
