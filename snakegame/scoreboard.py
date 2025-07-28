from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier',20,'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = int(self.get_high_score())
        self.color("white")
        self.show_score()
    def show_score(self):
        self.penup()
        self.goto(0,270)
        self.write(f"score: {self.score} High score :{self.highscore}",align=ALIGNMENT,font=FONT)
        self.hideturtle()
    def score_update(self):
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align= ALIGNMENT, font=FONT)

    def clear_board(self):
        self.clear()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.clear()
        self.write(f"score: {self.score} High score :{self.highscore}",align=ALIGNMENT,font=FONT)

    def get_high_score(self):
        with open("data.txt") as score_data:
            hiscore = score_data.read()
            return hiscore
    def update_high_score(self):
        with open("data.txt","w") as score_data:
            score_data.write(f"{self.highscore}")

