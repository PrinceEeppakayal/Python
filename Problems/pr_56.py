
# QUESTION: Create a class with a class attribute a; create an object from it and set a directly using object a = 0. Does this change the class attribute?

class sample:
    a = "Prince"

obj = sample()
obj.a = "Panda"

print(sample.a)
print(obj.a)

# INFO: No it does not change the class attribute because we have created an instance attribute a for the object obj. The class attribute a is still "Prince".