import time
from turtle import Screen

import car_manager
from player import Player, FINISH_LINE_Y, STARTING_POSITION
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
loop_number = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move_each_car()
    loop_number += 1

    # Create a new car every sixth time the game runs.
    if loop_number % 6 == 0:
        car.create_car()

    # Check for car and turtle collision, tell the user game over if car hits.
    for every_car in car.cars:
        if player.distance(every_car) < 20:
            score.game_over()
            game_is_on = False

    # detect if the turtle beat a level (made it to the end) and then go to the next one (level).
    if player.ycor() == FINISH_LINE_Y:
        score.update_level()
        player.goto(STARTING_POSITION)
        car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT

screen.exitonclick()

