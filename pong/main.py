from turtle import Turtle, Screen
import time
from paddle_class import Paddle
from ball_class import Ball
from scoreboard_class import Scoreboard
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('Pong')
screen.tracer(0)
scoreboard = Scoreboard()
from ball_class import Ball
ball = Ball()

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.ycor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    



screen.exitonclick()