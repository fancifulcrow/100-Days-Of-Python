import time
from turtle import Screen
import snake
import food
import scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake")
screen.bgcolor("black")
screen.tracer(0)

is_game_on = True

# reference the Snake class properly
player = snake.Snake()
food_item = food.Food()
score_panel = scoreboard.Scoreboard()

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

    # detect collision with food
    if player.head.distance(food_item) < 15:
        food_item.refresh()
        score_panel.increase_score()
        player.extend_segment()

    # detect collision with wall
    if player.head.xcor() > 290 or player.head.xcor() < -290 or player.head.ycor() > 290 or player.head.ycor() < -290:
        is_game_on = False
        score_panel.game_over()

    # detect collision with body
    for segment in player.segments[1:]:
        if player.head.distance(segment) < 10:
            is_game_on = False
            score_panel.game_over()

screen.exitonclick()
