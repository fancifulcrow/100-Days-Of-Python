# 1.) import the sqlite3 module.
# import sqlite3

# 2.) Now create a connection to a new database (if the database does not exist then it will be created).
# db = sqlite3.connect("library-collection.db")
# 3.) Run main.py and you should see a new file appear called library-collection.db

# 4.) Next we need to create a cursor which will control our database.
# cursor = db.cursor()


####### Creating Tables in our Database #######

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

# This is basically how we run sql statements

###### Adding data to our table ######
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()
# SQL queries are very sensitive to typos.


# Writing SQL commands are complicated and error-prone. 
# It would be much better if we could just write Python code and 
# get the compiler to help us spot typos and errors in our code. 
# That's why SQLAlchemy was created.


###### Configure the Extension ######
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)


###### Define Models ######
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


###### Create the Tables ######
with app.app_context():
    db.create_all()


####### CREATE a Record ######
with app.app_context():
    new_book = Book(title="Harry Potter", author="J. K. Rowling", rating=9.3) # id is generated automatically
    db.session.add(new_book)
    db.session.commit()
    # When creating new records, the primary key fields is optional.

###### READ All Records ######
with app.app_context():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars()
    # To read all the records we first need to create a "query" to select things from the database (a Result object).
    # When we execute a query during a database session we get back the rows in the database.
    # We then use scalars() to get the individual elements rather than entire rows.

###### READ a particular Record by query ######
with app.app_context():
    book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    # To get a single element we can use scalar() instead of scalars().

###### UPDATE a particular Record by query ######
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
    book_to_update.title = "Harry Potter and the Chamber of Secrets"
    db.session.commit()

###### UPDATE a particular Record by primary key ######
book_id = 1
with app.app_context():
    book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_update = db.get_or_404(Book, book_id)  
    book_to_update.title = "Harry Potter and the Goblet of Fire"
    db.session.commit() 
    # Flask-SQLAlchemy also has some handy extra query methods like get_or_404() that we can use.

###### DELETE a particular Record by primary key ######
book_id = 1
with app.app_context():
    book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    # or book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
