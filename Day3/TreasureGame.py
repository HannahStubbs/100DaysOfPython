print("Welcome to treasure Island!\nYour goal is to find the lost treasure, Good luck!")

choice1 = input("\nYour ship wreaks and you wash up on the beach.\nDo you choose to stay on the beach or venture into the looming forest?\t").lower()
choice2 = input("\nIn the forest you see a lake. Do you choose to swim or wait for a boat?\t").lower()
choice3 = input("\nYou made it across the lake safetly and see a small cave, but it is dark. Do you make a tourch and then go in or do you go in without light?\t").lower()
endcomment = print("\nYou walk into the cave and find a billion fireflies. It is the most magical thing you have ever seen. In the middel of the cave you find the chest.\nWell Done!")

if choice1 == "venture":
    print(choice2)
else:
    print("You were attacked by crabs1\nGAME OVER!")

if choice2 == "wait":
    print(choice3)
else:
    print("You were eaten by a lake monster!\nGAME OVER!")

if choice3 == "without light":
    print(endcomment)
else:
    print("Sorry you attracted a swarm of moths.\nGAME OVER!")
