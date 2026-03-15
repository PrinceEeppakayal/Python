
#INFO: If the condition never becomes false, the loop keeps getting executed infinitely.

#INFO: The while loop is used when you don't know the number of iterations in advance.
#NOTE: Iterations refer to the number of times a loop executes its block of code.

#QUESTION: Write a program to print the numbers from 1 to 50 using while loops
i = 1
while i <= 50:
    print(i)
    i = i + 1

#QUESTION: Write a program to print the content of the list using while loops
fruits = ["apple", "banana", "cherry", "orange", "kiwi"]
i = 0 
while i < len(fruits):
    print(fruits[i])
    i = i + 1 