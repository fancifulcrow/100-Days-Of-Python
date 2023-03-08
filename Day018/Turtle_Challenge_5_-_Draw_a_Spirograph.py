import random
import turtle

theresa = turtle.Turtle()
turtle.colormode(255)
theresa.speed("fastest")


def decide_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        theresa.color(decide_color())
        theresa.circle(100)
        theresa.setheading(theresa.heading() + 10)


draw_spirograph(5)
screen = turtle.Screen()
screen.exitonclick()
