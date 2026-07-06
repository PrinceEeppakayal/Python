
# QUESTION: Write a program to detect these spams. A spam comment is definded as a text containing following keywords:
'''"make a lot of money", "buy now", "subscribe this", "click this"'''

text = input("Enter the comment: ")
spam = False

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This comment is spam")
else:
    print("This comment is not spam")