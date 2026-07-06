# Normal way to find factorial of a number
def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product

print(factorial_iter(5))

# INFO: Recursion is a function which calls itself. It is used to directly use a mathematical formula as a function. For example: 
#    factorial(n) = n * factorial(n-1)  --> this is the mathematical formula for factorial.

# This function can be defined as follows:
def factorial_rec(n):
    if n == 0 or n == 1: # --> Base condition which doesn't call the function any further
        return 1
    else:
        return n * factorial_rec(n-1) # --> Function calling itself

print(factorial_rec(5))

# NOTE: The programmer need to be extremely careful while working with recursion to ensure that the function doesn't infinitely keep calling itself. Recursion is sometimes the most direct way to code an algorithm. 