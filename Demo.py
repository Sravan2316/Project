
from flask import Flask,render_template,request
app = Flask( __name__)

@app.route('/')
def demo():
    return render_template ('index.html')

dataset= {'sravan':'505','atr':'123'}

@app.route('/login-form' , methods=['POST','GET'])
def login():
    name = request.form['userName']
    pwd=request.form['userPassword']


    if name not in dataset:
        return render_template('index.html',info="invalid")
    else:
        if dataset[name]!=pwd:
            return render_template('index.html',info='invalid')
        else:
            return render_template('index.html',info="Logged In successfully")   

if __name__=='__main__':
    app.run()
