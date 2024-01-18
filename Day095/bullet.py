from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.penup()
        self.player = player
        self.hideturtle()
        self.color("white")
        self.shape("triangle")
        self.speed(0)
        self.setheading(90)
        self.shapesize(0.5, 0.5)

        self.firing_state = False
        self.bullet_speed = 10


    def move(self):
        self.sety(self.ycor() + self.bullet_speed)
        
    


