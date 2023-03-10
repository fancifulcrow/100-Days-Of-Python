# Advanced Python Arguements

# Arguments with Default Values
import turtle
tim = turtle.Turtle()
# def write(self, arg: object, move: bool = ..., align: str = ..., font : Tuple[str, int, str] = ...) -> None
# All the arguments except arg has a default value. So all we have to do is provide "arg"
tim.write("arg")
tim.forward(20)
# We can still change the the other arguments
tim.write("arg", font=("Times New Roman", 24, "italic"))

turtle.mainloop()

# *args: Many/Unlimited Positional Arguments
def add(*args):
    print(type(args)) # Tuple
    print(args)
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 2, 3, 4))


# **kwargs: Many/Unlimited Keyword Arguments
def calculate(n, **kwargs):
    print(type(kwargs)) # Dictionary
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("move")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


# With kw.get(key) I can create the class without any error despite no "model" or "color"
my_car = Car(make="Nissan", seat=4)