from random import randint

# #Print('Rules of the Game:\n Paper covers rock.\n Scissors cuts paper.\n Rock smash scissors')
# player = input("Let's play Rock - Paper - Scissors\nPick your favourite: ")
# randon = ['Rock','Paper','Scissors']
# computer = randon[randint(0,2)]
# if player == computer:
#         print( 'Tie!')
# elif player == 'Rock':
#     if computer == 'Scissors':
#         print('Player wins!')
# elif player == 'Paper':
#     if computer == 'Scissors':
#         print('Computer wins!')
# elif player == 'Scissors':
#     if computer == 'Paper':
#         print('Player wins!')
# elif player == 'Paper':
#     if computer == 'scissors':
#         print('compute wins!')

# #computer = randon[randint(0,2)]

choice = ['Rock','Paper','Scissors']
computer = choice[randint(0,2)]
player = input("Let's play Rock, Paper,Scissors: ")
if player == 'Rock':
    if computer == 'Rock':
        print('Draw')
    elif computer == 'Paper':
        print('Computer wins')
    elif computer == 'Scissors':
        print('Player wins')
elif player == 'Paper':
    if computer == 'Rock':
        print('Player wins!')
    elif computer == 'Paper':
        print('Draw')
    elif computer == 'Scissors':
        print('Computer wins')
elif player == 'Scissors':
    if computer == 'Rock':
        print('computer wins!')
    elif computer == 'Paper':
        print('Player wins')
    elif computer == 'Scissors':
        print('Draw')
    






