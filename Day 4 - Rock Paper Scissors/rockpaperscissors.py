#!/bin/python
# Rock Paper Scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player_choice = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper, or 2 for Scissors.\n"))
if 0 <= player_choice <= 2:
    computer_choice = random.randint(0,2)
    items = [rock, paper, scissors]
    print("You chose . . . " + items[player_choice])
    print("The computer chose . . . " + items[computer_choice])
    if items[player_choice] == rock:
        if items[computer_choice] == rock:
            print("It's a draw!")
        elif items[computer_choice] == paper:
            print("You loose! Paper beats Rock.")
        elif items[computer_choice] == scissors:
            print("You win! Rock beats Scissors")
    elif items[player_choice] == scissors:
        if items[computer_choice] == rock:
            print("You lose! Rock beats Scissors")
        elif items[computer_choice] == paper:
            print("You win! Scissors beats Paper.")
        elif items[computer_choice] == scissors:
            print("It's a draw")
    elif items[player_choice] == paper:
        if items[computer_choice] == rock:
            print("You win! Paper beats Rock.")
        elif items[computer_choice] == paper:
            print("It's a draw!")
        elif items[computer_choice] == scissors:
            print("You lose! Scissors beats Paper.")
else:
    print("Invalid entry. Game over")


#   Alternative Logic from course
#
# computer_choice = random.randint(0,2)
# if player_choice == 0 and computer_choice == 2:
#     print("You win!")
# if computer_choice == 0 and player_choice == 2:
#     print("You lose!")
# elif computer_choice > player_choice:
#     print("You lose!")
# elif computer_choice < player_choice:
#     print("You win!")
# elif player_choice == computer_choice:
#     print("It's a draw.")
# else:
#     print("You typed an invalid number")



