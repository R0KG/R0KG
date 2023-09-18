from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy

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

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
db = SQLAlchemy(app)

    


@app.route('/')
def home():
    all_books = Book.query.all()
    
    return render_template("index.html",all_books=all_books)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()
    
@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Book(title=request.form["title"], author=request.form["author"], rating=request.form["rating"])
            db.session.add(new_book)
            db.session.commit()

        return redirect( url_for('home') )
    
    return render_template("add.html")

@app.route("/edit/<int:book_id>", methods = ["GET","POST"])
def edit_rating(book_id):
    book = db.get_or_404(Book, book_id)
    if request.method == "POST":
        new_rating = request.form.get("new_rating")
        book.rating = float(new_rating)
        db.session.commit()
        return redirect( url_for("home") )
    
    return render_template("edit.html",book=book)

@app.route("/delete")
def delete_book():
    book_id = request.args.get("book_id")
    book = db.get_or_404(Book, book_id)

    db.session.delete(book)
    db.session.commit()
    
    return redirect( url_for("home"))




# Create the database schema within the Flask app context

# Create a new entry in the books table

    
    
if __name__ == "__main__":
    app.run(debug=True)

