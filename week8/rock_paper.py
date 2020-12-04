# from random import randint

# #Write a program to play rock paper scissor with a user
# computer = game_list[randint(0,2)]
# player = input("Let's play!!! Please enter either Rock, Scissor or Paper: ")
# game_list = ['Rock','Scissor','Paper']
# computer = game_list[randint(0,2)]
# if player == computer:
#     print('Tie')
# elif player == Rock and computer == paper:
#     print('Well Done! So happy for you, you win :)')
# else:
#    print('Try again, you did not make this time. Please keep trying :)')
# computer = t[randint(0,2)]


from random import randint

#create a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]