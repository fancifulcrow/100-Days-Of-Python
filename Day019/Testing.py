import turtle

# Event Listeners
# listen()
# onkey() or onkeyrelease()
# onkeypress()
# onclick or onscreenclick()
# ontimer()
# mainloop() or done()

# Object State and Instances
tim = turtle.Turtle()
tom = turtle.Turtle()


def move_forward():
    tim.forward(100)


screen = turtle.Screen()
# onkey() takes the parameters: a function with no arguments and a key
screen.listen()

# Here, the function, move_forward does not have the parentheses when taken as an argument
# onkey() is a Higher Order Function as it takes another function as an argument and works with it
# I used keyword arguments instead of positional arguments as it was safer
screen.onkey(fun=move_forward, key="space")
screen.exitonclick()
