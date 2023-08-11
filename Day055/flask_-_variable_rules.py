from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        return f"<i>{function()}</i>"
    
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    
    return wrapper_function


@app.route('/')
@make_bold
@make_emphasis
@make_underlined
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return '<h1 style="text-align: center;">Hello World</h1>'

######## Variable Rules ########
# You can add variable sections to a URL by marking sections with <variable_name>. 
# Your function then receives the <variable_name> as a keyword argument. 
# Optionally, you can use a converter to specify the type of the argument like <converter:variable_name>.

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f"User: {username}"

@app.route('/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f"Post ID: {post_id}"

@app.route('/user/<username>/followers/<int:num>')
def show_followers(username, num):
    return f"{username} has {num} followers"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f"subpath: {subpath}"

if __name__ == "__main__":
    # Debug mode allows changes to the code to reflect on the webpage without restarting our server
    app.run(debug=True)

#---------- Converter Types ----------#
# string: (default) accepts any text without a slash
# int: accepts positive integers
# float: accepts positive floating point values
# path: like string but also accepts slashes
# uuid: accepts UUID strings