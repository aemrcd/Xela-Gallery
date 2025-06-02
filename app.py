from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
from database import connect_to_database
from util import hash_password, tokenize_email

app = Flask(__name__)
app.secret_key = 'Aerol'

@app.route('/')
def home():
    if 'username' in session:
        return f"Hello, {session['username']}! <a href='/logout'>Logout</a>"
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_pw = hash_password(password)

        conn = connect_to_database()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user and user['password'] == hashed_pw:
            session['username'] = username
            return render_template('index.html', username=username)
        msg = 'Invalid email or password!'
    return render_template('login.html', msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        tokenized_email = tokenize_email(email)
        hashed_pw = hash_password(password)

        conn = connect_to_database()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()

        if user:
            msg = 'Username already taken!'
        else:
            cursor.execute(
                'INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                (username, tokenized_email, hashed_pw)
            )
            conn.commit()
            msg = 'Registered successfully!'

        cursor.close()
        conn.close()
    return render_template('register.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)