import turtle

def shape(number_of_sides,side_length):
    angle = 360/number_of_sides   
    for i in range(number_of_sides):
        turtle.forward(side_length)
        turtle.right(angle)
    turtle.done()
          

number_of_sides = int(input('Please input the numbers of side: '))
side_length = int(input('Please input the of side length: '))
shape(number_of_sides,side_length)



