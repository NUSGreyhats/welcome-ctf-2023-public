import sqlite3

conn = sqlite3.connect('instance/ctfchallenge.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS users')

cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
''')

cursor.executemany('''
INSERT INTO users (username, password) VALUES (?, ?)
''', [('admin', 'ASDFJASDJFHUIOSDHFIOQWHEOIF324231RKJ23H')])

conn.commit()
conn.close()