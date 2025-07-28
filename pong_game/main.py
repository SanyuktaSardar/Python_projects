from turtle import Screen

import scoreboard
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

#TODO: Create the Screen
screen = Screen()
screen.setup(width= 800,height=600)
screen.bgcolor("black")
screen.title("PONG GAME")

#TODO: Create and move a paddle
screen.tracer(0)
l_paddle = Paddle(-350,0)

#TODO: Create another paddle
r_paddle = Paddle(350,0)

#TODO: Create the ball and make it move
ball = Ball()

l_score = Scoreboard()
r_score = Scoreboard()

l_score.goto(-170, 260)
l_score.show_score()

r_score.goto(170,260)
r_score.show_score()

screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up,"i")
screen.onkey(r_paddle.go_down,"j")

game_on = True
while game_on :
    time.sleep(ball.move_speed)
    screen.update()
    # TODO: Detect collision with wall and bounce
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    #TODO: Detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        l_score.update_score()

    if ball.xcor() < -380:
        ball.reset_position()
        # TODO:Keep Score
        r_score.update_score()

screen.exitonclick()