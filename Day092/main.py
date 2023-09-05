from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileAllowed
from wtforms.validators import InputRequired

import colorgram

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
Bootstrap5(app)


class ImageForm(FlaskForm):
    img = FileField('Upload Image', validators=[
        InputRequired(message="Please choose a file."),
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Only images (jpg, jpeg, png, or gif) are allowed.')
    ])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def home():
    image_form = ImageForm()
    if image_form.validate_on_submit():
        colors = colorgram.extract(image_form.img.data, 5)

        return render_template("index.html", colors=colors)
    
    return render_template("index.html", image_form=image_form)


if __name__ == "__main__":
    app.run(debug=True)
