from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.num_level = 1
        self.goto(-280, 250)
        self.write(f"Level: {self.num_level}", align="left", font=FONT)

    def update_level(self):
        self.num_level += 1
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.num_level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "bold"))
