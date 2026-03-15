
# NOTE: We cannot access elements of a set using index as it is unordered and does not have index
# NOTE: We can use loops to access elements of a set

# Creating a empty set
a = set()
print(type(a))

# Adding values to an empty set
a.add(4)
a.add(5)
a.add(4) # Adding a value repeatedly does not changes a set

a.add((4, 5, 6, 7)) # We can add a tuple to a set

# a.add({4:5}) # Cannot add list or dictionary to sets
print(a)

print(len(a)) # Length of the set

a.remove(5) # Removes 5 from the set
# a.remove(15) # Throws an error while trying to remove 15 (which is not present in the set)
print(a)

print(a.pop()) # Removes a random element from the set
print(a)

# a.clear() # Clears the set
# print(a)

# Union and Intersection
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
set_c = {1, 3, 5, 6, 7, 8, 9}

union_set = set_a.union(set_b,set_c) # Returns the union of two sets
print(union_set) # Prints {1, 2, 3, 4, 5, 6, 7, 8, 9}

intersection_set = set_a.intersection(set_b,set_c) # Returns the intersection of two sets
print(intersection_set) # Prints {3}