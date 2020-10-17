import turtle
# This code draws a blue triange by importing turtle.

def triangle():
    turtle.color('blue')
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(90)
        turtle.left(120)
    turtle.end_fill()
triangle()
turtle.done()