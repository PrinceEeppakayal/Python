# Function is a group of statements that perform a specific task. It is reusable and helps to break down a program into smaller, manageable parts.

# NOTE: Function definition --> the part containing the exact set of instructions which are executed during the function call.

# NOTE: Function call -> whenever we want to call a function, we use its name followed by parentheses as follows: func1():  -->  this is a function call

# QUESTION:  Write a program to greet a user with a "Good Day" using functions

def greet(name):
    gr = "Good Day, " + name
    return gr

name = input("Enter your name: ")
print(greet(name))

# INFO: INBUILT FUNCTION --> already present in python like len(), range(), print().

# INFO: USER DEFINED FUNCTION --> made by the user like greet(), func1().
