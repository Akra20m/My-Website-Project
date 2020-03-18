from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
# app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('LOCALPW')
app.secret_key = os.environ.get('SECRET_KEY')

db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = 'dictionary'
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.Text, unique=False)
    defination = db.Column(db.Text, unique=False)

    def __init__(self, word, defination):
        self.word = word
        self.defination = defination


@app.route("/main", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        words = request.form["word"].lower().capitalize()
        print(words)

        news = Data.query.filter_by(word=words).first()
        print(news)
        if news != None:
            return render_template("main.html", mynews=news.defination, mynews1=news.word)
        return render_template("main.html", text="We don't have the meaning for this word")
    if request.method == 'GET':
        return render_template("main.html")


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/quiz')
def quiz():
    return render_template("quiz.html")


@app.route('/project')
def project():
    return render_template("project.html")


@app.route('/course')
def course():
    return render_template("course.html")


if __name__ == "__main__":
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run()
