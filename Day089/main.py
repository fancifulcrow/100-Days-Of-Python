from flask import Flask, render_template, url_for, redirect
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "ONFN93jkKen340lmzWA0"
Bootstrap5(app)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///to-dos.db"
db.init_app(app)


class ToDos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    is_done = db.Column(db.Boolean, nullable=False)


class AddToDoForm(FlaskForm):
    description = StringField("What do you want to add", validators=[DataRequired()])
    submit = SubmitField("Add")


with app.app_context():
    db.create_all()


@app.route("/", methods=["GET"])
def home():
    result = db.session.execute(db.select(ToDos))
    all_todos = result.scalars()
    return render_template("index.html", all_todos=all_todos)


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = AddToDoForm()

    if add_form.validate_on_submit():
        new_todo = ToDos(description=add_form.description.data, is_done=False)
        db.session.add(new_todo)
        db.session.commit()

        return redirect(url_for("home"))
    
    return render_template("add.html", add_form=add_form)


@app.route("/delete/<int:item_id>", methods=["GET", "DELETE"])
def delete(item_id):
    item_to_delete = db.get_or_404(ToDos, item_id)
    db.session.delete(item_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/mark/<int:item_id>", methods=["GET","PATCH"])
def mark_complete(item_id):
    item_to_mark = db.get_or_404(ToDos, item_id)
    item_to_mark.is_done = not item_to_mark.is_done
    db.session.commit()

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)