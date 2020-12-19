import time
from turtle import Screen
from turtle_crossing_game.player import Player
from turtle_crossing_game.car_manager import CarManager
from turtle_crossing_game.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True

screen.listen()
screen.onkey(player.go_up, "Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing
    if player.is_at_finish_line():
        scoreboard.increase_score()
        player.go_to_start()
        car_manager.level_up()


screen.exitonclick()
