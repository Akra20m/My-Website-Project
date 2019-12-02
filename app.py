from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="postgres://bfdfczbsfcinwo:0d5b3fa1df74d1919e4d6a0954bb4a570fa1d6c955f346991b7fd9f2fad430f5@ec2-75-101-133-29.compute-1.amazonaws.com:5432/ddp0q09isres7h?sslmode=require"
#app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('LOCALPW')
app.secret_key='akram123'

db=SQLAlchemy(app)

class Data(db.Model):
    __tablename__='dictionary'
    id=db.Column(db.Integer, primary_key=True)
    word=db.Column(db.Text, unique=False)
    defination=db.Column(db.Text, unique=False)

    def __init__(self,word,defination):
        self.word=word
        self.defination=defination

@app.route("/main", methods=['GET', 'POST'])
def main():
    if request.method=='POST':
        words=request.form["word"].lower().capitalize()
        print(words)

        news=Data.query.filter_by(word=words).first()
        print(news)
        if news!=None:
            return render_template("main.html", mynews=news.defination,mynews1=news.word)
        return render_template("main.html",text="We don't have the meaning for this word")
    if request.method=='GET':
        return render_template("main.html")
@app.route("/")
def index():
    return render_template("index.html")


@app.route('/quiz')
def quiz():
    return render_template('quiz.html')


if __name__== "__main__":
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug=True
    app.run()
