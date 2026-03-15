a = "This string has a double  space between double and space" 
# You cannot delete a space having more than two space in between for that we need to use loop
a = a.replace("  ", " ")
print(a)