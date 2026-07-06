
# QUESTION: Write a program to print third, fifth and seventh element from a list using enumerate function.

list = [1, 3 ,5, 63, 2, 4, 56, 143]
for index, value in enumerate(list):
    if index == 2 or index == 4 or index == 6:
        print(f"Element at {index + 1}th is {value}")
