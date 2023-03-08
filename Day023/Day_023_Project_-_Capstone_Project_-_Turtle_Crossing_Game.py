import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

screen.listen()
screen.onkey(player.move_player, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    carManager.create_car()
    carManager.move_cars()

    for car in carManager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.draw_game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        carManager.level_up()
        scoreboard.update_scoreboard()

screen.exitonclick()
