
# QUESTION: Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if n == 0:
        return 0
    else:
        return sum(n-1) + n
    
b = sum(4)
print(f"The sum is {b}")