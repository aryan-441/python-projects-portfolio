from turtle import Turtle
from car_manager_class import random_colour
STARTING_POSITION = (0,-200)
MOVE_DISTANCE = 280
FINISH_LINE_Y = 280
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color(random_colour())
        self.penup()
        self.setheading(90)
    def go_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)
    def go_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(),new_y)