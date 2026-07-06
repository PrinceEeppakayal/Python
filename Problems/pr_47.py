
# QUESTION: Repeat pr_46 for a list of such words to be censored 

words = ["donkey", "lazy"]

with open("sample1.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word , "######")
    
    with open("sample1.txt", 'w') as f:
        f.write(content)