from flask import Flask,render_template,request
import sqlite3

app = Flask( __name__)

@app.route('/')
def demo():
    return render_template ('index.html')

@app.route('/index')
def index():
    return render_template ('index.html')



@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/register' , methods=['POST','GET'])
def login():
    new_user = request.form['username']
    new_pwd=request.form['password']
    new_email=request.form['email']
    new_phone=request.form['phone']

    conn=sqlite3.connect('brain.db')
    cur=conn.cursor()

    cur.execute('INSERT INTO student (username,password,email,phone) values(?,?,?,?)',(new_user,new_pwd,new_email,new_phone))
    conn.commit()

    return render_template('index.html',info="successfully added student details")


if __name__=='__main__':
    app.run(port=5001)

