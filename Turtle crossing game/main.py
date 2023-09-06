import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
score = Scoreboard()

screen.onkey(fun=player.move, key="Up")
all_turtles = []



game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.car_move()

    #Detect collision with the cars
    for carr in car.all_cars:
        if carr.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.is_at_finish():
        player.refresh()
        car.speed_up()
        score.next_level()






screen.exitonclick()