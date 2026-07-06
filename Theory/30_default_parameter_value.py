# We can have a value as a default argument in a function. If we specify name = "User" in the line containing def, this value is used when no argument is passed to the function. 

def greet(name="User"):
    gr = "Hello, " + name
    return gr

a = greet("Prince") # --> name will be "Prince" in a function body (passed)
print(a)

b = greet() # --> name will be "User" in a function body (default value)
print(b)