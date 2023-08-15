from flask import Flask, render_template
import requests

app = Flask(__name__)


response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
posts = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=posts)


@app.route("/post/<int:blog_id>")
def view_blog(blog_id):
    # List comprehension
    blog = next(post for post in posts if post["id"] == blog_id)
    return render_template("post.html", blog=blog)


if __name__ == "__main__":
    app.run(debug=True)
