
# QUESTION: Write a program using function to find greatest of three numbers.

def maximum(num1, num2, num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3
    else:
        if (num2>num3):
            return num2
        else:
            return num3
    
m = maximum(5, 6 , 85)
print(f"The maximum value is {m}")
