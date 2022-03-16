from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-200, 240)
        self.write(arg=f"Level: {self.level}", font=FONT, align="center")

    def update_level(self):
        self.clear()
        self.level += 1
        self.goto(-200, 240)
        self.write(arg=f"Level: {self.level}", font=FONT, align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", font=FONT, align="center")
