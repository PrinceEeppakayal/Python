
# QUESTION: Write a program to print multiplication table of a given number using while loop.

num = int(input("Enter the number: "))
i = 1
while i<=10:
    # print(str(num) + "X" + str(i) + "=" + str(num*i))
    print (f"{num} X {i} = {num*i}")
    i = i + 1

# QUESTION: Write a python function to print multiplication table of a given number.

def table(num):
    for i in range(1, 11):
        a = str(num) + " X " + str(i) + " = " + str(num*i)
        print(a)

b = int(input("Enter the number: "))
table(b)
