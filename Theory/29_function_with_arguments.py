# A function can accept some values it can work with. We can put these values in the parentheses. A function can also return values as shown below:

def greet(name):
    gr = "Hello, " + name
    return gr

            # .---> "Prince" is passed to greet in name
a = greet("Prince")
#'--> a will now contain Hello, Prince
print(a)
