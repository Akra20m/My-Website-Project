from flask import Flask, render_template, request, flash, redirect, url_for, session, logging
from flask.ext.sqlalchemy import SQLAlchemy
#from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from passlib.hash import sha256_crypt


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:***REMOVED***@localhost/project1'
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
    validators.EqualTo('Confirm', message='Passwords do not match')])
    confirm=PasswordField('Confirm Password')
@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegisterForm(request.form)
    if request.method=='POST' and form.validate():
        return render_template('registration.html')
    return render_template('registration.html', form=form)


if __name__== "__main__":
    app.debug=True
    app.run()
