
# QUESTION: Write a program to filter a list of numbers which are divisible by 5.

num = [10, 15, 22, 30, 44, 50, 60, 75, 88, 90]

filter_num = list(filter(lambda filter_num : filter_num % 5 == 0, num))
print(filter_num)