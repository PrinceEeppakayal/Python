
# QUESTION: Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

myDict = {
    "Chawal": "Rice",
    "Chana": "Gram",
    "Gajar": "Carrot",
    "Aloo": "Potato",
    "Tamatar": "Tomato",
}

print("Options are : ", myDict.keys())
a = input("Enter a Hindi Word : ")
# print("The meaning of the word is : ", myDict[a])
print("The meaning of the word is : ", myDict.get(a)) #r This will throw an error as get is a method and not a list