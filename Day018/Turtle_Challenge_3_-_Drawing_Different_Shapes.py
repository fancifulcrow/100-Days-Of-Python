import random
from turtle import Turtle, Screen

trevor = Turtle()
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "pink", "brown", "grey", "violet"]

for n in range(3, 11):
    trevor.color(random.choice(colors))
    angle = 360/n
    for _ in range(n):
        trevor.forward(100)
        trevor.right(angle)

screen = Screen()
screen.exitonclick()
