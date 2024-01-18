import random
from turtle import Turtle, Screen

from player import Player
from alien import Alien
from bullet import Bullet
from scoreboard import ScoreBoard

# Set up screen
screen = Screen()
screen.bgcolor("black")
screen.title("Space Invaders Clone")
screen.setup(width=640, height=640)

# Border
border_pen = Turtle()
border_pen.hideturtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setpos(-300, -300)
border_pen.pendown()
for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)

# Scoreboard
scoreboard = ScoreBoard()

# Player
player = Player()

# Bullet
bullet = Bullet(player=player)

# Firing the bullet
def fire_bullet():
    if not bullet.firing_state:
        bullet.firing_state = True
        bullet.setpos((player.xcor(), player.ycor()))
        bullet.showturtle()

# Move player
screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

# Fire bullet
screen.onkey(fire_bullet, "space")

# Aliens
aliens = []
for i in range(20):
    x = random.randint(-280, 280)
    y = random.randint(100, 250)
    alien = Alien((x, y))
    aliens.append(alien)


# Function for detecting collision
def is_collision(t1, t2, d):
    if t1.distance(t2) <= d:
        return True
    return False
    

game_is_on = True
while game_is_on:
    for alien in aliens:
        alien.move()
        if is_collision(bullet, alien, 20):
            bullet.hideturtle()
            bullet.firing_state = False
            alien.hideturtle()
            bullet.setpos((player.xcor(), player.ycor()))
            aliens.remove(alien)
            scoreboard.increase_score()

    # Moving the bullet when fired
    if bullet.ycor() < 300 and bullet.firing_state:
        bullet.move()
    
    # Reseting the bullet if out of bounds
    if bullet.ycor() >= 300:
        bullet.firing_state = False
        bullet.hideturtle()

    
    # End game if alien hits player
    if is_collision(player, alien, 20):
        print("Game Over")
        scoreboard.end_game()
        break

    # End the game if all aliens are defeated
    if not aliens:
        print("You Win")
        scoreboard.end_game()
        break

screen.exitonclick()