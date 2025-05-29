import turtle as t
from turtle import Turtle, Screen
import random
tim = t.Turtle()
t.colormode(255)

""" Create random color """
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

"""" Random Walk(Turtle) """
# direction = [0, 90, 120, 180, 270, 360] # Random number to control angle for turtle.right()
# tim.pensize(10)
tim.speed("fastest")
# for i in range(200):
#     tim.color(random_color())
#     # tim.right(random.choice(direction))
#     tim.setheading(random.choice(direction))
#     tim.forward(30)

"""" draw spirograph """
def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()



"""" Create shape like hexagonal """
# def draw_shape(num_side):
#     angle = 360 / num_side
#     for i in range(num_side):
#         tim.right(angle)
#         tim.forward(100)
#
# for shape in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(shape)