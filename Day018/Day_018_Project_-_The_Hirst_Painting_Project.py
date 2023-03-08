# This code will not work in repl.it as there is no access to the colorgram package here.###
# We talk about this in the video tutorials##

import random
import turtle
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_tuple = (r, g, b)
#     rgb_colors.append(rgb_tuple)
#
# print(rgb_colors)

color_list = [(240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = turtle.Turtle()
turtle.colormode(255)
step = 50
tim.hideturtle()


# Make an n by n grid of dots
def draw_dot(n):
    for _ in range(n):
        for _ in range(n):
            tim.pendown()
            tim.dot(20, random.choice(color_list))
            tim.penup()
            tim.forward(step)

        tim.setheading(90)
        tim.forward(step)
        tim.left(90)
        tim.forward(step * n)
        tim.setheading(0)


def adjust_position():
    tim.penup()
    tim.setheading(225)
    tim.forward(300)
    tim.setheading(0)


adjust_position()
draw_dot(10)

screen = turtle.Screen()
screen.exitonclick()
