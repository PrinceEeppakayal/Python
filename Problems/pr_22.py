
# QUESTION: Write a program to find greatest of four numbers entered by the user.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))

# if(a>b and a>c and a>d):
#     print("a is the greatest number")
# elif(b>a and b>c and b>d):
#     print("b is the greatest number")
# elif(c>a and c>b and c>d):
#     print("c is the greatest number")
# else:
#     print("d is the greatest number")


if(a>d):
    f1 = a
else:
    f1 = d

if(b>c):
    f2 = b
else:
    f2 = c

if (f1>f2):
    print("The greatest number is: ", str(f1))
else:
    print("The greatest number is: ", str(f2))