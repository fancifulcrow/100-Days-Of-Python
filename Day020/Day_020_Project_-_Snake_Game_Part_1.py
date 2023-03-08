import time
from turtle import Screen
import snake

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)

is_game_on = True

# reference the Snake class properly
player = snake.Snake()

# Taking Input

screen.listen()
# The keys are case-sensitive
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    player.move()

screen.exitonclick()
