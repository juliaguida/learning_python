
# Write a program to play rock paper scissor with a user
# rock_paper_scissor_v1.py (Long code)
# rock_paper_scissor_v2.py (use and and or operators)
# user_input picks rock/paper/scissor
# computer_input Generate computer pick out of rock/paper/scissor using random.choice()
# Calculate who is winning:


from random import randint

choice = ['Rock','Paper', 'Scissors']
computer = choice[randint(0,2)]
player = input('Please enter Rock, Paper, or Scissors: ')

if player == computer:
    print('Draw!')
elif player == 'Rock' and computer =='Scissors':
    print('Player wins ')
elif player == 'Rock'and computer == 'Paper':
    print('Computer wins')
elif player == 'Paper'and computer == 'Rock':
    print('Player wins')
elif player == 'Paper' and computer == 'Scissors':
    print('Computer wins')
elif player == 'Scissors' and computer == 'Paper':
    print('Player wins')
elif player == 'Scissors' and computer == 'Rock':
    print('Computer wins')
else:
    print('I did not understand :)')


