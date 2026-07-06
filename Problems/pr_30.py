
# QUESTION: Write a program to find whether a given number is prime or not.

num = int(input("Enter the number: "))
prime = True

for i in range(2,num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")