from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

from flask_sqlalchemy import SQLAlchemy

from dotenv import load_dotenv
from os import getenv

load_dotenv()

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")
bootstrap = Bootstrap5(app)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///items.db"
db.init_app(app)


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    is_discounted = db.Column(db.Boolean, nullable=False)
    discount = db.Column(db.Float)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)