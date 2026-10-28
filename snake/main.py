'''Snake Game Main'''

from turtle import Turtle, Screen
import turtle

import time
from snake_class import Snake
from food_class import Food
from scoreboard_class import Scoreboard




screen = Screen()
screen.setup(height=600,width=600)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.left,'a')
screen.onkey(snake.down,'s')
screen.onkey(snake.right,'d')



game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 18:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()  
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        time.sleep(1)
        scoreboard.reset()
        snake.reset()
        
        
        #scoreboard.game_over()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 13:
            time.sleep(1)
            
            scoreboard.reset()
            snake.reset()
            



screen.exitonclick()