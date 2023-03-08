from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.goto(200, 252)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def draw_game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
