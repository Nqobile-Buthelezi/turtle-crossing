from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
CAR_HEADING = 180


class CarManager:

    def __init__(self):
        self.cars = []
        self.create_car()

    def create_car(self):
        random_y = random.randint(-250, 250)
        new_car = Turtle()
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.shape("square")
        new_car.setheading(CAR_HEADING)
        new_car.color(random.choice(COLORS))
        new_car.goto(260, random_y)
        self.cars.append(new_car)

    def move_each_car(self):
        for each_car in self.cars:
            each_car.forward(STARTING_MOVE_DISTANCE)
