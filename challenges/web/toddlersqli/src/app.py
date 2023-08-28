from flask import Flask, request, render_template, redirect, url_for, flash, session
import sqlite3
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

#utils
def query_database(query):
    conn = sqlite3.connect('instance/ctfchallenge.db')
    cursor = conn.cursor()
    result = cursor.execute(query).fetchall()
    conn.close()
    return result

#routes
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():

    username = request.form.get('username', '')
    password = request.form.get('password', '')

    query = f"SELECT id, username FROM users WHERE username = '{username}' AND password = '{password}'"

    users = query_database(query)

    if users:
        return render_template('dashboard.html', message=f"Welcome {users[0][1]}")
    else:
        flash('Login failed', 'danger')
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
