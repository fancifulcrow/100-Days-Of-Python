from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "<p>Bye!</p>"

# to see the app, type in the terminal:
# python -m flask --app hello_flask run

# or

if __name__ == "__main__":
    app.run()

# In Python, the special name __main__ is used for two important constructs:
# 1.) the name of the top-level environment of the program, which can be checked using the __name__ == '__main__' expression; and
# 2.) the __main__.py file in Python packages.

# if __name__ == '__main__':
#     # Execute when the module is not initialized from an import statement.
#     ...