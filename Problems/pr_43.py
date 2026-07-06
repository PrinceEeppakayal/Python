
# QUESTION: Write a program to read the text from a given file 'poems.txt' and find out whether it contains the word 'twinkle'

f = open("poems.txt", 'r')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()