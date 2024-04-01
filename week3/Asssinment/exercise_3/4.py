import psycopg2

conn = psycopg2.connect(
    database="postgres", user='postgres',  password='1234', host='127.0.0.1', port='5432'
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE category (
        id SERIAL PRIMARY KEY,
        code VARCHAR(50) UNIQUE,
        name VARCHAR(255) NOT NULL
    );
""")

conn.commit()
conn.close()
