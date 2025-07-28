from turtle import Turtle
FONT = ('Courier',30,'normal')
ALIGNMENT = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()

    def increase_score(self):
        self.score += 1

    def show_score(self):
        self.write(f"{self.score}",align=ALIGNMENT,font=FONT)

    def clear_score(self):
        self.clear()

    def update_score(self):
        self.clear_score()
        self.increase_score()
        self.show_score()

    def game_over(self):
        self.write("GAME OVER!",align=ALIGNMENT,font=FONT)
