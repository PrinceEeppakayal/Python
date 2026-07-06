
# QUESTION: Write a python function to remove a given word from a list and strip it at the same time. 

def remove_and_strip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

A = "    I am a boy    "
n = remove_and_strip(A, "a")
print(n)