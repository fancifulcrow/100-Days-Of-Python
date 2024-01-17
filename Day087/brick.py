from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.color("white", color)
        self.shape("square")
        self.shapesize(1.5, 3)
        self.penup()
        self.goto(position)