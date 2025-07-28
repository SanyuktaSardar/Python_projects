from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.show_level()
    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    #Detect successful crossing

    if player.ycor() == 280:
        scoreboard.update_score()
        player.goto(0, -280)
        car_manager.level_up()


screen.exitonclick()

