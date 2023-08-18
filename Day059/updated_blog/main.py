# Template from https://startbootstrap.com/theme/clean-blog

from flask import Flask, render_template
import requests

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/81bab482e62ce81face5")
response.raise_for_status()
data = response.json()


@app.route("/")
def home():
    return render_template("index.html", posts=data)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:blog_id>")
def view_blog(blog_id):
    # List comprehension
    blog = next(post for post in data if post["id"] == blog_id)
    return render_template("post.html", blog=blog)


if(__name__ == "__main__"):
    app.run(debug=True)