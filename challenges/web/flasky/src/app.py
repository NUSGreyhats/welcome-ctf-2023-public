from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User
from config import FLAG, SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Configuration for SQLite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')

        new_user = User(username=username, password=hashed_password)

        db.session.add(new_user)
        try:
            db.session.commit()
            flash('Registered successfully!', 'success')
            return redirect(url_for('login'))
        except:
            db.session.rollback()
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['loggedin'] = True
            session['username'] = user.username
            session['admin'] = user.admin
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Incorrect username/password!', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/flag')
def flag():
    if 'loggedin' in session:
        if session['admin']:
            message = f"Hello, {session['username']}! Here's your secret flag: {FLAG}"
        else:
            message = f"Hello, {session['username']}! You don't have access to the flag."
    else:
        message = "Please log in first."

    return render_template('flag.html', message=message)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
