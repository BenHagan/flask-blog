# blog.py - controller

#imports
from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
import sqlite3

#configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY= "!^\xc1RP\xec<zx\xb5\xb8\x98\xd3'\xaf\x1f\xb0\xb8\xefR\xbb\xb7%E"

app = Flask(__name__)

#pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

#function user for connecting to the database

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
            request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials.  Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html', error=error)

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)