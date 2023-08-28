from flask import Flask, request, render_template, redirect, url_for, flash, session
import sqlite3
from config import SECRET_KEY, FLAG

app = Flask(__name__)
app.secret_key = SECRET_KEY

def query_database(query):
    conn = sqlite3.connect('instance/ctfchallenge.db')
    cursor = conn.cursor()
    result = cursor.execute(query).fetchall()
    conn.close()
    return result

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    message=""
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    # Vulnerable SQL query
    query = f"SELECT id, username FROM users WHERE username = '{username}' AND password = '{password}'"

    try:
        users = query_database(query)
    except:
        flash('Login failed', 'danger')
        return redirect(url_for('index'))

    if users:
        session['username'] = users[0][1]
        if session['username'] == 'admin':
            return redirect(url_for('dashboard'))
    else:
        flash('Login failed', 'danger')
        return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session and session['username'] == 'admin':
        return render_template('dashboard.html', message=FLAG)
    else:
        flash('Access denied. admin only.', 'danger')
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
