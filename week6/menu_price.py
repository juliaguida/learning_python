# You are given the cost of 3 menu_items of a restaurant:
# ham_sandwich = £3, spring_roll = £5,  hot_soup: £1
# Write a program that takes an input from the user for the dish they want to buy and prints the cost that the user has to pay
# Extension1: check if the input provided by the user exists
# Extension2: print the menu list before asking the user to input the item they want to buy.

#import tkinter

ham_sandwich = 3
spring_roll = 5
hot_soup = 1
print( 'Hi, welcome! glad you come to eat this is the menu, please pick your favourites: \n Ham sandwich = £{}\n Spring Roll = £{}\n Hot Soup = £{}'.format(ham_sandwich,spring_roll,hot_soup))

user_order = input('What you would like to order ? ')
if user_order.lower() == 'ham sandwich':
     print('Good choice it will be £{} please '.format(ham_sandwich))
elif user_order.lower() == 'spring roll':
     print('Good choice it will be £{} please'.format(spring_roll))
elif user_order.lower()== 'hot soup':
     print('Good choice it will be £{} please'.format(hot_soup))
else:
     print('It does not exist please refer to the above menu,thank you !')