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
import random

user_choice = input("What do you choose? Rock, paper or scissors? ").lower()
random_choice = round(random.randint(1, 3))
computer_choice = None

if random_choice == 1:
    computer_choice = "rock"
elif random_choice == 2:
    computer_choice = "paper"
elif random_choice == 3:
    computer_choice = "scissors"

if user_choice == "rock":
    print(rock)
    print(f"computer chooses {computer_choice}")
    if computer_choice == "rock":
        print(rock)
        print("equal")
    elif computer_choice == "paper":
        print(paper)
        print("You lost, computer wins")
    elif computer_choice == "scissors":
        print(scissors)
        print("You won!")
if user_choice == "paper":
    print(paper)
    print(f"computer chooses {computer_choice}")
    if computer_choice == "rock":
        print(rock)
        print("You won!")
    elif computer_choice == "paper":
        print(paper)
        print("equal")
    elif computer_choice == "scissors":
        print(scissors)
        print("You've lost!")
if user_choice == "scissors":
    print(scissors)
    print(f"computer chooses {computer_choice}")
    if computer_choice == "rock":
        print(rock)
        print("You've lost, computer wins!")
    elif computer_choice == "paper":
        print("You've won!")
    elif computer_choice == "scissors":
        print(scissors)
        print("Equal")


