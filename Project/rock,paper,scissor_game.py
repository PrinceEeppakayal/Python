print("Welcome to Game: ", end= "")
print("Rock (r), Paper (p), Scissor (s)")

def gameWin(comp,you):
    if comp == you:
        return None
    if comp == "r":
        if you == "s":
            return False
        elif you == "p":
            return True
    if comp == "p":
        if you == "r":
            return False
        elif you == "s":
            return True
    if comp == "s":
        if you == "p":
            return False
        elif you == "r":
            return True

import random
randomNO = random.randint(1,3)
if randomNO == 1:
    comp = "r"
elif randomNO == 2:
    comp = "p"
elif randomNO == 3:
    comp = "s"
 
print("Computer chose the choice")
you = input("Enter your choice: ")
a = gameWin(comp, you)

print(f"Computer Choice was {comp}")
print(f"Yours choice was {you}")

if a == None:
    print("The match tied")
elif a:
    print("You Won")
else:
    print("You Lose")