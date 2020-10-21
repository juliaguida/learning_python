import turtle

def square(side_length):
    turtle.color('red','pink')
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(side_length)
        turtle.right(90)
    turtle.end_fill()

def triangle(side_length):
    turtle.color('red','pink')
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)
    turtle.end_fill()
user_input = int(input('Please enter a number: '))
square(user_input)
triangle(user_input)
turtle.done()
