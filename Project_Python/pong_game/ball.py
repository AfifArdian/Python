from turtle import Turtle,Screen

class Ball (Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_cor = 10
        self.y_cor = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_cor
        new_y = self.ycor() + self.y_cor
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_cor *= -1
        self.move_speed *= 0.9

    def bounce_x(self):
        self.x_cor *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.bounce_x()
        self.move_speed = 0.1
        self.goto(0,0)




