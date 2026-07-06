
# NOTE: in and is operators

# INFO: is = it is used to check if the variables are the same object in memory or not. It returns True if both variables point to the same object, otherwise it returns False.

# INFO: in = it is used to check if a value is present in a sequence (like a list, tuple, or string) or not. It returns True if the value is found in the sequence, otherwise it returns False.

a = None
if(a is None):
    print("yes")
else:
    print("no") 

b = [45,36,6]
print(45 in b) # True
print(456 in b) # False