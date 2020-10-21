import turtle

def shape(side_lenght, angle,number_of_sides):
    turtle.begin_fill()
    turtle.fillcolor('black')
    for i in range(9):
        turtle.forward(side_length)
        turtle.right(number_of_sides)
    turtle.end_fill()
   
 