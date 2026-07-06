
# QUESTION: A list contains the multiplication table of 7. Write a program to convert it to a vertical string of same numbers (7 14 ...).

table = [str(i * 7) for i in range(1, 11)]
string = "\n".join(table)
print(table)
print(string)