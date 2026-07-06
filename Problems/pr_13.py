
# QUESTION: Write a program to sum a list with 4 numbers.

a = [28, 17, 43, 14]

print(a[0]+a[1]+a[2]+a[3]) 
# print(sum(a))


import random 

no= [random.randint(10,100) for i in range(20)]
print(no)

no = [num for num in no if not (20<= num <= 50)]
print(no)