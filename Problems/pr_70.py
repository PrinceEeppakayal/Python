
# QUESTION: Write a program to display a/b where a and b are integers. If b = 0, display infinite by handling the ZeroDivisionError.

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))

try:
    print(a/b)
except ZeroDivisionError:
    print(f"The value is Infinite")