from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "Center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.color("white")
        self.hideturtle()
    def show_level(self):
        self.goto(-280, 250)
        self.write(f"Level:{self.score}",font=("Courier",12,"normal"))

    def increment_level(self):
        self.score += 1

    def update_score(self):
        self.clear()
        self.increment_level()
        self.show_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
