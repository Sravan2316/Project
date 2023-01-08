import sqlite3
from flask import Flask, redirect, url_for, render_template, request, session


def register_user_to_db(email, password, new_password):
    con = sqlite3.connect('NEW.db')
    cur = con.cursor()
    cur.execute('INSERT INTO New(email,password,new_password)values(?,?,?)',
                (email, password, new_password))
    con.commit()
    con.close()


def check_user(email, password):
    con = sqlite3.connect('NEW.db')
    cur = con.cursor()
    cur.execute(
        'Select email,password FROM New WHERE email=? and password=?', (email, password))

    result = cur.fetchone()
    if result:
        return True
    else:
        return False


app = Flask(__name__)
app.secret_key = "random"


@app.route("/")
def first():
    return render_template('first.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route("/reg")
def register():
    return render_template('register.html')


@app.route("/signup1", methods=["POST", "GET"])
def signup1():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        new_password = request.form['new_password']

        register_user_to_db(email, password, new_password)
        return redirect(url_for('register'))

    else:
        return render_template('first.html')


@app.route("/valid_login", methods=["POST", "GET"])
def valid_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if check_user(email, password):
            session['email'] = email

        return redirect(url_for('success'))

    else:
        redirect(url_for('index'))


@app.route('/success', methods=["POST", "GET"])
def success():
    if 'email' in session:
        return render_template('success.html', email=session['email'])
    else:
        return render_template('fail.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('first'))


if __name__ == '__main__':
    app.run(port=5005, debug=True)
