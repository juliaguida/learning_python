# Coin flip game:
import random first line

def flip(user_choice): # 2nd line definition
    computer_choice = random.choice(['head','tails'])
    print('The computer choose {}'.format(computer_choice))
    if computer_choice == user_choice:
        print ('You win')    
    else:
        print('You lost')

side_pick = input("Let's flip a coin? Please enter your side: head/tails ") # takes the input from the suerr
flip(side_pick)