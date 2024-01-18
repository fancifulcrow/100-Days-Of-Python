from turtle import Turtle
from bullet import Bullet

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.color("white")
        self.shape("turtle")
        self.setpos(0, -250)
        self.setheading(90)

        self.player_speed = 15


    def move_left(self):
        if self.xcor() > -280:
            self.setx(self.xcor() - self.player_speed)


    def move_right(self):
        if self.xcor() < 280:
            self.setx(self.xcor() + self.player_speed)
    