from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super(). __init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            ryu = Turtle("square")
            ryu.penup()
            ryu.goto(250, random.randint(-250, 250))
            ryu.setheading(180)
            ryu.resizemode("user")
            ryu.shapesize(stretch_len=2, stretch_wid=1)
            ryu.color(random.choice(COLORS))
            self.all_cars.append(ryu)

    def car_move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT





