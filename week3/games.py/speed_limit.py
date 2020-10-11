#import random
#random.speed(6779)
#speed_limit = random.randrange(15, 66, 50)
speed_limit = 65
print("The speed limit is", speed_limit)

speed = input('How fast are you going? ')
speed = int(speed)

if speed == 65:
  print('Have safe journey')
elif speed > 65:
  print('Are you on the hurry? You are above the speed limit, slow down please.')
elif speed < 65:
  print('You are fine')
  
