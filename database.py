import sqlite3

conn = sqlite3.connect('data.db')

c = conn.cursor()

# c.execute(
#     """CREATE TABLE products (
#     id INTEGER,
#     product TEXT,
#     price INTEGER
#     )
#     """
# )

# c.execute("INSERT INTO products VALUES ('2', 'Pepsi', 2.98)")

c.execute("SELECT * FROM products WHERE id = '2'")

print(c.fetchall())

conn.commit()

conn.close()
