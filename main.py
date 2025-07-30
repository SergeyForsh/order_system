import sqlite3

conn = sqlite3.connect('exemple.db')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS user
    (id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL)
            ''')
conn.commit()
conn.close()

cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Алексей", 30))
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Игорь", 25))

conn.commit()

cur.execute("SELECT * FROM users")
rows = cur.fetchall()

for row in rows:
    print(row)