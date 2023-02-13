from turtle import Turtle
#init scoreboard
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.l_score = 0
        self.r_score = 0
    def write_score(self):
        self.clear()
        self.write(f'{self.l_score} : {self.r_score}', False, align="center", font=("Courier", 24, "normal"))
    def update_l_score(self):
        self.l_score += 1
    def update_r_score(self):
        self.r_score += 1