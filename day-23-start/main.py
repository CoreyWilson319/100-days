import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player_1 = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.onkey(player_1.move_up, "Up")
screen.onkey(player_1.cheat, "Down")


# multiply time.sleep() interval by level or something to have it progress as the level gets higher
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player_1) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player_1.is_at_finish_line():
        player_1.player_reset()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()