from turtle import Screen

from paddle import Paddle
from ball import Ball
from brick import Brick
from scoreboard import ScoreBoard

HORIZONTAL_LIMIT = 315
VERTICAL_LIMIT = 315

# Set up screen
screen = Screen()
screen.title("Breakout Clone")
screen.bgcolor("black")
screen.setup(width=640, height=640)

# Draw Bricks
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
bricks = []
bricks_x = -245
bricks_y = 200

for i in range(6):
    for j in range(9):
        brick = Brick((bricks_x, bricks_y), colors[i])
        bricks.append(brick)
        bricks_x += 60
    
    bricks_x = -245
    bricks_y -= 30


paddle = Paddle()

# Move paddle
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

screen.listen()

# Ball
ball = Ball()

# Scoreboard
scoreboard = ScoreBoard()

game_running = True

while game_running:
    ball.move()

    # Detect collision with ceiling
    if ball.ycor() > VERTICAL_LIMIT:
        ball.bounce_y()

    # Detect collision with side walls
    if ball.xcor() > HORIZONTAL_LIMIT or ball.xcor() < -HORIZONTAL_LIMIT:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < 45 and ball.ycor() < 290:
        ball.bounce_y()

    # Detect collision with brick
    for brick in bricks:
        if ball.distance(brick) < 30:
            ball.bounce_x()
            brick.hideturtle()
            x_axis_difference = ball.distance(brick)
            y_axis_difference = ball.distance(brick)
            if x_axis_difference > y_axis_difference:
                # If the ball ditches at the side of the brick then ball's x-axis will be switched.
                ball.bounce_x()
            else:
                # If the ball ditches on the top or bottom of the brick then ball's y-axis will be switched.
                ball.bounce_x()
                ball.bounce_y()
            bricks.remove(brick)
            scoreboard.increase_score()
            break

    # Detect paddle miss
    if ball.ycor() < -VERTICAL_LIMIT:
        game_running = False

    if not bricks:
        game_running = False


scoreboard.end_game()


screen.exitonclick()