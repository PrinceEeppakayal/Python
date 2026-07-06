
# QUESTION: Write a program to print multiplication table of n using for loop in reversed order.

num = int(input("Enter the nunber: "))
for i in range(10,0,-1):
    # print (str(num) + " X " + str(i) + " = " + str(num*i))

#INFO: we can also use f-string to print the output  
    print(f"{num} X {i} = {num*i}")
