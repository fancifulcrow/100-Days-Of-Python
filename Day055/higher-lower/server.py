from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def landing_page():
    return "<h1>Guess a number between 0 and 9</h1> \
        <img src='https://media.giphy.com/media/WYUEY3niJ7Rbou4FSc/giphy.gif' alt='Rihanna walkking at NFL'>"

com_choice = random.randint(1, 9)

@app.route("/<int:num>")
def user_choice(num):
    if num > com_choice:
        return "<h1 style='color: red;'>Too high, try again!</h1> \
            <img src='https://media.giphy.com/media/OPU6wzx8JrHna/giphy.gif' alt='Patrick Star about to cry'>"
    elif num < com_choice:
        return "<h1 style='color: purple;'>Too low, try again!</h1> \
            <img src='https://media.giphy.com/media/7SF5scGB2AFrgsXP63/giphy.gif' alt='Pikachu sad'>"
    else:
        return "<h1 style='color: green;'>You Found me!</h1> \
            <img src='https://media.giphy.com/media/chzz1FQgqhytWRWbp3/giphy.gif' alt='Minions celebrating'>"
    

if __name__ == "__main__":
    app.run(debug=True)