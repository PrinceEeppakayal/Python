
# NOTE: Tuple is an immutable data type in Python. Its elements cannot be changed after they have been assigned. They can have duplicate value and can be of different data types. 

# It is a collection of elements which is ordered and unchangeable.
# Creating a tuple using ()
t = (1, 2 , 4, 5)

t1 = () # Empty tuple
print(t1)

# t2 = (1) # Wrong way to declare a tuple with single element
t2 = (1,) # Tuple with single element
print(t2)

# Printing the elements of a tuple
print(t[3])

# Cannot change the value of tuple
# t[0] = 34 #--> Throws an error