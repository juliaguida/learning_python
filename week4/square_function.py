import turtle

def square(side_length):
    
 for i in range(4):
      turtle.forward(side_length)
      turtle.right(90)


user1_input = int(input('Please enter a number: '))
user2_input  = int(input('Please enter a number: '))
square(user1_input)
square(user2_input)
turtle.done()
