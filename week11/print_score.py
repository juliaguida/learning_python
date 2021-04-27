# Take a list of game scores as inputs from the user. Write a program to display the following:
# Number of scores recorded:
# Max score recorded:
# Min score recorded:
# Print the list of scores in descending order


user_input = (input('Enter the list of games score: '))
print(user_input)
user_list = user_input.split()
print(user_list)
user_int_list = []

for i in user_list:
    user_int_list.append(int(i))
print(user_int_list)
print('numbers of scores recorded {}'.format(len(user_int_list)))
print('Max score recorded {}'.format(max(user_int_list)))
print('Min score recorded {}'.format(min(user_int_list)))
user_int_list.sort(reverse = True)
print('List of score in descending order {}'.format(user_int_list))
