from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
#TODO:CONTROL SNAKE
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on = True
while game_on :
    screen.update()
    time.sleep(0.1)
    snake.move()
    #TODO:detect collision with food
    if snake.head.distance(food) < 20:
        scoreboard.clear()
        food.refresh()
        scoreboard.score_update()
        scoreboard.show_score()
        snake.extend()
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.update_high_score()
        scoreboard.reset()
        snake.reset()
    #TODO:detect collision with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 12:
            scoreboard.update_high_score()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()