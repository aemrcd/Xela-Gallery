from flask import Flask, render_template, request, redirect, url_for, session
from flask_bcrypt import Bcrypt
from database import connect_to_database

app = Flask(__name__)
app.secret_key = 'Aerol'
bcrypt = Bcrypt(app)

users = {}  # Temporary storage (replace with database later)

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
        user = users.get(username)
        if user and bcrypt.check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('home'))
        msg = 'Invalid email or password!'
    return render_template('login.html', msg=msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        dob = request.form['dob']

        if username in users:
            msg = 'Username already taken!'
        else:
            hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
            users[username] = {'password': hashed_pw, 'email': email, 'dob': dob}
            msg = 'Registered successfully!'
    return render_template('register.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)