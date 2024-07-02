import random

dice_choice = input("Welcome to dicey, the program that allows you to roll!\nFirst select your dice:D6, D10\t").lower()

if dice_choice == "d6":
    print(random.randrange(1, 6))
else:
    print(random.randrange(1, 10))