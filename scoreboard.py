FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.teleport(x = -250, y = 250)
        self.score = 0
        self.score_display()

    def score_display(self):
        self.clear()
        self.write(f"Score: {self.score}", font=FONT)

    def level_up(self):

        self.score += 1
        self.score_display()

    def game_over(self):
        self.clear()
        self.teleport(0, 0)
        self.write(f"Game over. Final Score: {self.score}", align="center", font=FONT)

    # pass
