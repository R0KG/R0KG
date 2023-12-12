from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import sqlite3
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)    

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False, unique= True )
    year = db.Column(db.Integer, nullable=False)
    description  = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float,nullable=False)
    ranking = db.Column(db.Integer,nullable=False)
    review = db.Column(db.String(255), nullable=False)
    img_url = db.Column(db.String(255), nullable=False)

@app.route("/")
def home():
    movies = Movie.query.order_by(Movie.rating.desc()).all()
        
    return render_template("index.html",movies=movies)

@app.route("/edit", methods = ["GET","POST"])
def update():
    mov_id = request.args.get("movie_id")
    movie = db.get_or_404(Movie,mov_id)
    if request.method == "POST":
        new_rating = request.form.get("new_rating")
        new_review = request.form.get("new_review")
        movie.rating= float(new_rating)
        movie.review= new_review
        db.session.commit()
        return redirect( url_for("home"))
    return render_template("edit.html",movie= movie)

@app.route("/delete")
def delete():
    mov_id = request.args.get("movie_id")
    movie = db.get_or_404(Movie, mov_id)

    db.session.delete(movie)
    db.session.commit()
    
    return redirect( url_for("home"))

class AddMovieForm(FlaskForm):
    title = StringField("Title of the Movie")
    submit = SubmitField("Done")

@app.route("/add")
def add():
    form = AddMovieForm()
    new_title = form.title.data
    
    return render_template("add.html",form=form)

with app.app_context():
    db.create_all()


    

if __name__ == '__main__':
    app.run(debug=True)
