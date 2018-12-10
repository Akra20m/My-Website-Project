from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from flask.ext.sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from passlib.hash import sha256_crypt


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:202601@localhost/project1'
db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__='dictionary'
    id=db.Column(db.Integer, primary_key=True)
    #id=db.Column(db.Integer)
    word=db.Column(db.Text, unique=False)
    defination=db.Column(db.Text, unique=False)

    def __init__(self,word,defination):
        self.word=word
        self.defination=defination

class Users(db.Model):
    __tablename__='registration data'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text, unique=False)
    email=db.Column(db.Text, unique=True)
    username=db.Column(db.Text, unique=True)
    password=db.Column(db.Text, unique=False)

    def __init__(self,name,email,username,password):
        self.name=name
        self.email=email
        self.username=username
        self.password=password

@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/answer", methods=['POST'])
def answer():
    #words=request.form["word"]
    words=request.form["word"].lower().capitalize()
    print(words)

    #
    #news=Data.query.all()
    news=Data.query.filter_by(word=words).first()
    print(news)
    if news!=None:
        return render_template("answer.html", mynews=news)
    return render_template("index.html",text="We don't have the meaning for that, try again")
@app.route("/")
def main():
    return render_template("main.html")

class RegisterForm(Form):
    name=StringField('Name',[validators.length(min=1, max=50)])
    username=StringField('Username',[validators.length(min=4, max=25)])
    email=StringField('Email',[validators.length(min=6, max=50)])
    password=PasswordField('Password',[validators.DataRequired(),
    validators.EqualTo('confirm', message='Passwords do not match')])
    confirm=PasswordField('Confirm Password')
@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegisterForm(request.form)
    if request.method=='POST' and form.validate():
        name= form.name.data
        email=form.email.data
        username=form.username.data
        password=sha256_crypt.encrypt(str(form.password.data))
        users=Users(name,email,username,password)
        db.session.add(users)
        db.session.commit()
        #flash('You are registered', 'success')
        return redirect(url_for('main'))
    return render_template('registration.html', form=form)

@app.route('/panel', methods=['GET','POST'])
def panel():
    username=request.form["username"]
    password=request.form["password"]
    return render_template('panel.html')

@app.route('/login')
def login():
    return render_template('login.html')



if __name__== "__main__":
    app.debug=True
    app.run()
