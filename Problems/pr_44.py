
# QUESTION: The game() function in a program lets a user play a game and returns a score as an integer. You need to read a file 'Hiscore.txt' which is either blank or contains the previous Hi-Score. You need to write a program to update the Hi-Score whenever game() breaks the Hi-Score

def game():
    return 4573

score = game()
with open("hiscore.txt") as f:
    hiscoreStr = f.read()

if hiscoreStr == '':
    with open("hiscore.txt", 'w') as f:
        f.write(str(score))

elif int(hiscoreStr)<score:
    with open("hiscore.txt", 'w') as f:
        f.write(str(score))