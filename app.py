from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from database import connect_to_database
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

@app.route('/')
def home():
    if 'email' in session:
        return render_template('homepage.html', 
                               email=session.get('email'), 
                               username=session.get('username'))
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']


        hashed_pw = generate_password_hash(password)

        conn = connect_to_database()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT * FROM users WHERE username = %s OR email = %s', (username, email))
        user = cursor.fetchone()

        if user:
            flash('Username or email already taken!', 'error')
        else:
            cursor.execute(
                'INSERT INTO users (username, email, password) VALUES (%s, %s, %s)',
                (username, email, hashed_pw)
            )
            conn.commit()
            flash('Registered successfully! Please login.', 'success')
            return redirect(url_for('login'))

        cursor.close()
        conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        conn = connect_to_database()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user is not None:
            
            if check_password_hash(user['password'], password):
                session['email'] = user['email']
                session['username'] = user['username']
                flash('Logged in successfully!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Incorrect password!', 'error')
        else:
            flash('User not found!', 'error')
    return render_template('login.html')

# MODELS route

@app.route('/model1')
def model1():
    return render_template('model1.html', username=session.get('username'))

@app.route('/model2')
def model2():
    return render_template('model2.html', username=session.get('username'))

@app.route('/model3')
def model3():
    return render_template('model3.html', username=session.get('username'))

@app.route('/model4')
def model4():
    return render_template('model4.html', username=session.get('username'))

@app.route('/model5')
def model5():
    return render_template('model5.html', username=session.get('username'))


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
