'''MAIN'''
from turtle import Turtle, Screen
import turtle
from player_class import Player
from scoreboard_class import Scoreboard
from car_manager_class import CarManager
import time
screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600,height=600)
screen.tracer(0)
game_on = True
screen.listen()
screen.onkeypress(player.go_up, 'w')
#screen.onkeypress(player.go_down,'s')
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 17:
            game_on = False
            scoreboard.game_over()
        if player.ycor() > 280:
            player.goto(0,-280)
            car_manager.level_up()
            scoreboard.increase_level()
            

screen.exitonclick()