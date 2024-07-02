import random

billpayers = ["Megan", "Hannah", "AJ", "Ani"]

numnames= len(billpayers)
choice = random.randint(0, numnames -1)

print(f"Who is paying...\n{billpayers[choice]}")