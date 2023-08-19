from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wij29enwqqiQWE02309op'
Bootstrap5(app)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library-collection.db"
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'


with app.app_context():
    db.create_all()

# all_books = []

class BookForm(FlaskForm):
    book_name = StringField("Book Name", validators=[DataRequired()])
    book_author = StringField("Book Author", validators=[DataRequired()])
    rating = StringField("Rating", validators=[DataRequired()])
    submit = SubmitField("Add Book")


class EditForm(FlaskForm):
    new_rating = StringField("New Rating", validators=[DataRequired()])
    submit = SubmitField("Edit Rating")


@app.route('/', methods=["GET"])
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    return render_template("index.html", all_books=all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    book_form = BookForm()
    if book_form.validate_on_submit():
        # book_info = {
        #     "title" : book_form.book_name.data,
        #     "author" : book_form.book_author.data,
        #     "rating" : book_form.rating.data,
        # }
        # all_books.append(book_info)
        new_book = Book(title=book_form.book_name.data, author=book_form.book_author.data, rating=book_form.rating.data)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template("add.html", book_form=book_form)


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book_to_edit = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    edit_form = EditForm()

    if edit_form.validate_on_submit():
        book_to_edit.rating = edit_form.new_rating.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", book=book_to_edit, edit_form=edit_form)


@app.route("/delete/<int:book_id>", methods=["GET", "POST"])
def delete(book_id):
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

