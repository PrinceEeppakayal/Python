
# QUESTION: Write a program which finds out whether a given name is present in a list or not.

list = ["prince", "jyoti", "rahul", "om", "vedant"]
name = input("Enter your name: ")

if (name in list):
    print("Name is present in the list")
else:
    print("Name is not present in the list")