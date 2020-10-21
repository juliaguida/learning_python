import turtle

def triangle(side_length):
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)
    turtle.done()

user_input = int(input('Please enter a number: '))
triangle(user_input)
