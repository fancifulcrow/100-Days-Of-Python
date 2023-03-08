from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setup main screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

# Create and move a paddle
# Create another paddle
l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)

# Create the ball and make it move
ball = Ball()

# Keep score
scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect when paddles miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_l_score()
        time.sleep(2)

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_r_score()
        time.sleep(2)

screen.exitonclick()
