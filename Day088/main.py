from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, URL

app = Flask(__name__)
Bootstrap5(app)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


class AddForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
    coffee_price = StringField("Price of Coffee")
    seats = StringField("No of Seats", validators=[DataRequired()])
    map_url = StringField("Cafe Location on Google Maps (URL)", validators=[DataRequired(), URL()])
    img_url = StringField("Image (URL)", validators=[DataRequired(), URL()])
    has_toilet = BooleanField("Does it have toilets?")
    has_wifi = BooleanField("Does it have WiFi?")
    has_sockets = BooleanField("Does it have sockets?")
    can_take_calls = BooleanField("Can one take call?")
    submit = SubmitField('Add Cafe')


class UpdateForm(FlaskForm):
    new_price = StringField("New Price", validators=[DataRequired()])
    submit = SubmitField("Submit")

class SearchForm(FlaskForm):
    term = StringField(validators=[DataRequired()], render_kw={"placeholder": "Search a location"})
    submit = SubmitField("Search")

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/all", methods=["GET"])
def view_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    
    return render_template("all.html", all_cafes=all_cafes)


@app.route("/search", methods=["GET", "POST"])
def search():
    search_form = SearchForm()
    if search_form.validate_on_submit():
        query_location = search_form.term.data
        result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location.title()))
        # Note, this may get more than one cafe per location
        all_cafes = result.scalars().all()
        return render_template("search.html", search_form=search_form, all_cafes=all_cafes, term=query_location)
    
    return render_template("search.html", search_form=search_form)


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    add_form = AddForm()

    if add_form.validate_on_submit():
        new_cafe = Cafe(
            name=add_form.cafe.data,
            map_url=add_form.map_url.data,
            img_url=add_form.img_url.data,
            location=add_form.location.data,
            has_sockets=add_form.has_sockets.data,
            has_toilet=add_form.has_toilet.data,
            has_wifi=add_form.has_wifi.data,
            can_take_calls=add_form.can_take_calls.data,
            seats=add_form.seats.data,
            coffee_price=add_form.coffee_price.data,
        )
        db.session.add(new_cafe)
        db.session.commit()

        return redirect(url_for("view_all_cafes"))

    return render_template("add.html", add_form=add_form)


@app.route("/update-price/<int:cafe_id>", methods=["GET", "POST", "PATCH"])
def patch_new_price(cafe_id):
    update_form = UpdateForm()
    cafe = db.get_or_404(Cafe, cafe_id)

    if update_form.validate_on_submit():
        new_price = update_form.new_price.data
        cafe = db.get_or_404(Cafe, cafe_id)
        cafe.coffee_price = new_price
        db.session.commit()
        return  redirect(url_for("view_all_cafes"))
    
    return render_template("update.html", update_form=update_form, cafe=cafe)
    

@app.route("/report-closed/<int:cafe_id>", methods=["GET","DELETE"])
def delete_cafe(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    db.session.delete(cafe)
    db.session.commit()
    return redirect(url_for("view_all_cafes"))


if __name__ == '__main__':
    app.run(debug=True)
