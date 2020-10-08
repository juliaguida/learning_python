# print the total cost of the oranges entered by the user

cost_orange = 0.50
user_input = int(input( 'How many oranges do you have ? Tell me and I will calculate the price for you. Enter in here:  '))
total_of_the_oranges = cost_orange * user_input
print('You have to pay £{:.2f} thank you for shopping '.format(total_of_the_oranges))