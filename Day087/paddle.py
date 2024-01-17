from turtle import Turtle

H_LIMIT = 280
PADDLE_SPEED = 20

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, -290)
        self.shape('square')
        self.color('white')
        self.shapesize(1, 5)
        self.penup()
        

    
    def move_left(self):
        if self.xcor() > -H_LIMIT:
            self.setx(self.xcor() - PADDLE_SPEED)

    def move_right(self):
        if self.xcor() < H_LIMIT:
            self.setx(self.xcor() + PADDLE_SPEED)
