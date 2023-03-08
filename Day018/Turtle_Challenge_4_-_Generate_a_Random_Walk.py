import random
import turtle

ted = turtle.Turtle()
turtle.colormode(255)
directions = [0, 90, 180, 270]
ted.width(5)
ted.speed("fastest")

# Tuple uses (), Lists use [] and Dictionaries use {}
# To access an element in the tuple we write it as a_tuple[n] where n is the index of the element
# Tuples, unlike lists are 'set in stone' or immutable, meaning the elements cannot be changed
# we can change a tuple to a list by list(a_tuple)


def decide_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


def random_walk(n):
    for _ in range(n):
        ted.color(decide_color())
        ted.forward(20)
        ted.setheading(random.choice(directions))


random_walk(200)

screen = turtle.Screen()
screen.exitonclick()
