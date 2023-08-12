# Get more HTML templates at https://html5up.net/
# get images at https://unsplash.com/

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()