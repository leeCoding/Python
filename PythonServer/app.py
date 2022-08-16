from crypt import methods
from email import message
import re
from flask import Flask,request,render_template

app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def home():
    return render_template('home.html')

@app.route('/signin',methods=['GET'])
def sigin_form():
    return render_template('form.html')

@app.route('/signin',methods=['POST'])
def sigin():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'password':
        return render_template('signin-ok.html',username=username)
    return render_template('form.html',message='Bad username or password',username=username)

if __name__ == '__main___':
    app.run()
