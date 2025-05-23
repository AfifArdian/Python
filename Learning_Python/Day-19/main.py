# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# def move_forward():
#     tim.forward(5)
#
# screen.listen()
# screen.onkey(fun=move_forward, key="space")
# screen.exitonclick()

"""" Make an Etch-A-Sketch App """
"""" Create by myself(Ardian) """
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    # tim.right(10) # version 1
    new_heading = tim.heading() + 10 # version 2
    tim.setheading(new_heading)

def clockwise():
    # tim.left(10) # version 1
    new_heading = tim.heading() - 10  # version 2
    tim.setheading(new_heading)

def clear_drawing():
    tim.speed("fastest")
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=counter_clockwise, key="d")
screen.onkey(fun=clockwise, key="a")
screen.onkey(fun=clear_drawing, key="c")
screen.exitonclick()