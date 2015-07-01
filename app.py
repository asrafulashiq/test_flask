from flask import Flask,request,flash
from flask import render_template
from loginForm import LoginForm
from validate_email import validate_email

app = Flask(__name__)
app.config.from_object('config')
@app.route('/index')
def index():
    return  render_template('index.html',
            title='Ashiq')
@app.route('/')
@app.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    error = None
    if request.method == 'POST':
        email = request.form["email"]
        
        if validate_email(email):
            return "your mail is {0}".format(email)
        else:
            error = 'invalid_email'
            return render_template('login.html',form=form,error=error)
    return render_template('login.html',form=form)

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8000)
