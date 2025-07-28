from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_pos,y_pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=6,stretch_len=1)
        self.goto(x_pos,y_pos)

    def go_up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(),new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

