num = int(input("Enter the number the star pattern should consist: "))

# QUESTION: Draw this pattern in the terminal :
'''
*
**
***
'''
for i in range(num):
    print("*" * (i+1))

# QUESTION: Draw this pattern in the terminal : 
'''
    *
   ***
  *****
'''
for i in range(num):
    print(" " * (num-i-1), end="")
    print("*" * (2*i-1), end="")
    print(" " * (num-i-1))

# QUESTION: Draw this pattern in the terminal : 
'''  
***
** 
*
'''
def star(num):
    pattern = ""
    for i in range(num):
        pattern = pattern + "*" * (num - i) + "\n"
    return pattern.strip()

b = star(3)
print(f"The pattern is \n{b}")