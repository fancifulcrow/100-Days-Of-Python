import requests
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

from dotenv import load_dotenv
from os import getenv

load_dotenv()

WEATHER_API_KEY = getenv("WEATHER_API_KEY")
WEATHER_API_ENDPOINT = "http://api.weatherapi.com/v1/current.json"

weather_api_param = {
    "key" : WEATHER_API_KEY,
    "q" : "Abuja"
}



app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

class SearchForm(FlaskForm):
    city = StringField(label=None, render_kw={"placeholder": "Search for a city"}, validators=[DataRequired()])
    submit = SubmitField(label="Search")
    

@app.route("/", methods=["GET", "POST"])
def home():
    search_form = SearchForm()
    if search_form.validate_on_submit():
        weather_api_param = {
            "key" : WEATHER_API_KEY,
            "q" : search_form.city.data
        }

        response = requests.get(url=WEATHER_API_ENDPOINT, params=weather_api_param)
        weather_data = response.json()
        try:
            if int(weather_data["location"]["localtime"].split(" ")[1].split(":")[0]) < 18:
                time_of_day = "day"
            else: 
                time_of_day = "night"
        except KeyError:
            time_of_day = None

        return render_template("index.html", search_form=search_form, weather_data=weather_data, time_of_day=time_of_day)


    return render_template("index.html", search_form=search_form)


if __name__ == "__main__":
    app.run(debug=True)