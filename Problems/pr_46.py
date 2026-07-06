
# QUESTION: A file contains a word "Donkey" multiple times. You need to write a program which replaces this word with ###### by updating the same file 

with open("sample1.txt") as f:
    content = f.read()

content = content.replace("donkey", "######")

with open("sample1.txt", 'w') as f:
    f.write(content)
