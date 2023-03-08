# import turtle
# timmy = turtle.Turtle()

# Import everything from a module
# from turtle import *
# this though may get confusing

# Import as with an alias
# import turtle as t

from turtle import Turtle, Screen

# Some modules have to be installed
# You can check python packages for more modules4
import heroes
print(heroes.gen())

timmy = Turtle()

timmy.shape("turtle")
timmy.color("red")

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

screen = Screen()
screen.exitonclick()
