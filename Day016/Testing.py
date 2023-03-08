# Object-Oriented Programming
# An object is made up of methods(functions) and attributes(variables)

# Names of classes usually use the Pascal case of naming convention

# Turtle Graphics is used to put graphics onto the screen
from turtle import Turtle, Screen

# object = Class()
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.forward(100)

my_screen = Screen()
# object.attribute
print(my_screen.canvheight)

# object.method()
my_screen.exitonclick()

# You can install other python packages in File->Setting->{Project Name}->Python Interpreter
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Name", ["John", "Micheal""", "Gabriel", "Raphael", "Leonardo"])
table.add_column("Age", [22, 32, 40, 25, 27])
table.align = "l"
print(table)
