from random import randint

sides = int(input('Please enter a side: '))
is_continue = 'True'
while is_continue == 'True':
    print(is_continue)
    if sides <= 1:
        print('Your dice has one side or less sides')
    else:
        choice = randint(1, sides)
        print('You rolled {}'.format(choice))
    is_continue = input('Do you want to continue? True/False: ')


