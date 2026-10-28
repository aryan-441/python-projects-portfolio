from turtle import Turtle
import turtle
import random
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1
turtle.colormode(255)
def random_colour():
    random_r = random.randint(0,255)
    random_b = random.randint(0,255)
    random_g = random.randint(0,255)
    return (random_r,random_b,random_g)


class CarManager():
    def __init__(self):
        #super().__init__()
        self.move_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
    def create_car(self):
        rand_chance = random.randint(1,5)
        if rand_chance == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random_colour())

            #x_cord = random.randint(-270,270)
            y_cord = random.randint(-240,240)
            new_car.goto(300,y_cord)
            self.all_cars.append(new_car)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_speed)
    def level_up(self):
        self.move_speed += MOVE_INCREMENT