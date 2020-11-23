# Write a program to check if you are the admin and if you have entered the right password, reply with ‘Welcome’ or ‘Go Away’ message


password = 'I am allowed'
user_input = input('Please enter you password: ')
if user_input == password:
    print('Welcome!!!')
else:
    print('Go Away!!!')