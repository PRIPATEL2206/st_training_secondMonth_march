import psycopg2

conn = psycopg2.connect(
    database="postgres", user='postgres',  password='1234', host='127.0.0.1', port='5432'
)
cur = conn.cursor()

cur.execute("""
    ALTER TABLE product
    ADD COLUMN category_id INTEGER,
    ADD CONSTRAINT fk_category
    FOREIGN KEY (category_id)
    REFERENCES category(id)
    ON DELETE CASCADE;
""")

conn.commit()
conn.close()
