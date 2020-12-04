import random

choice = random.random()
print(choice)
choice1 = random.randrange(5)
print(choice1)
choice2 = random.randint(1,5)
print(choice2)
choice3 = random.randrange(1,101,2)
print(choice3)
choice4 = random.choice(['Win','Loose','Draw'])
print(choice4)

from random import randrange

choice5 = randrange(5)
print(choice5)