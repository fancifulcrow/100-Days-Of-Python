from flask import Flask, render_template

import random
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10);

    current_date = datetime.now()

    return render_template("index.html", num=random_number, current_year=current_date.year)


@app.route("/guess/<name>")
def guess(name):
    genderize_parameters = {
        "name" : name
    }
    genderize_response = requests.get(url="https://api.genderize.io", params=genderize_parameters)
    genderize_response.raise_for_status()
    genderize_json = genderize_response.json()

    agify_parameter = {
        "name" : name
    }
    agify_response = requests.get(url="https://api.agify.io", params=agify_parameter)
    agify_response.raise_for_status()
    agify_json = agify_response.json()

    return render_template("guess.html", name=name, gender=genderize_json["gender"], age=agify_json["age"])


@app.route("/blog")
def blog():
    blog_response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    blog_response.raise_for_status()
    all_posts = blog_response.json()

    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)