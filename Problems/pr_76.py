
# QUESTION: Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce
l = [10, 20, 30, 40, 50]

a = reduce(max, l)
print(a)
