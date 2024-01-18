from turtle import Turtle


class Alien(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.setpos(position)
        self.color("green")
        self.shape("circle")
        self.speed(0)

        self.alien_speed = 5

    def move(self):
        # Move the alien
        self.setx(self.xcor() + self.alien_speed)

        # Move the alien back and down
        if self.xcor() > 280 or self.xcor() < -280:
            self.alien_speed *= -1
            self.sety(self.ycor() - 40)