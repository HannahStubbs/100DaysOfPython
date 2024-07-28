import random
# import unittest

rock = '''
     _______
 ---'   ____)
       (_____)
 rock  (_____)
       (____)
 ---.__(___)
 '''

paper = '''
     _______
 ---'   ____)____
           ______)
paper      _______)
          _______)
 ---.__________)
 '''

scissors = '''
    ______
---'   ___)____
          ______)
scissors_________)
      (____)
---.__(___)
'''

choice = input("Welcome to rock paper scissors.\nPlease enter your choice: ").lower()

if choice == "rock":
    print(f"\nYour choice:{rock}")
if choice == "paper":
    print(f"\nYour choice:{paper}")
if choice == "scissors":
    print(f"\nYour choice:{scissors}")
else:
    print("invalid, You lose")

compchoice = (random.randrange(0,3))

if compchoice == 0:
    print(f"Your opponents choice:{rock}")
if compchoice == 1:
    print(f"Your opponents choice:{paper}")
if compchoice == 2:
    print(f"Your opponents choice:{scissors}")

if choice == "rock" and compchoice == 0:
    print("Good job you Tie\n")
elif choice == "rock" and compchoice == 1:
    print("Wah Wah you lose\n")
else:
    print("Well done, you win!\n")
  
