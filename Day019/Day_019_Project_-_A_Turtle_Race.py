# There is a bug where multiple turtle can become first
import random
import turtle

is_race_on = False
screen = turtle.Screen()
screen.setup(width=854, height=480)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []

user_bet = screen.textinput(title="Color Picker", prompt="Which turtle will win? Pick a color:").lower()

for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-410, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for racer in all_turtles:
        if racer.xcor() > 420:
            winning_color = racer.pencolor()
            is_race_on = False

            if winning_color == user_bet:
                print("You won!")
            else:
                print("You lost!")

            print(f"The winner is the {winning_color} turtle")

        rand_distance = random.randint(0, 10)
        racer.forward(rand_distance)

screen.exitonclick()
