import sqlite3
from config import FLAG

conn = sqlite3.connect('instance/ctfchallenge.db')
cursor = conn.cursor()

# Drop the old table
cursor.execute('DROP TABLE IF EXISTS users')
cursor.execute('DROP TABLE IF EXISTS flags')

cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
''')

cursor.execute('''
CREATE TABLE flags (
    id INTEGER PRIMARY KEY,
    flag TEXT
)
''')

cursor.execute('''
INSERT INTO users (username, password) VALUES (?, ?)
''', ('admin', 'ASDFJASDJFHUIOSDHFIOQWHEOIF324231RKJ23H'))

cursor.execute('''
INSERT INTO flags (flag) VALUES (?)
''', (FLAG,))

conn.commit()
conn.close()
