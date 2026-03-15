a = 2

# NOTE: 1. if-elif-else ladder

if(a>3):
    print("a is greater than 3")
elif(a>13):
    print("a is greater than 13")
elif(a>7):
    print("a is greater than 7")
elif(a>17):
    print("a is greater than 17")
else:
    print("The value is not greater than 3 or 7")

# NOTE: 2. multiple if statements

if(a>3):
    print("a is greater than 3")

if(a>13):
    print("a is greater than 13")

if(a>7):
    print("a is greater than 7")

if(a>17):
    print("a is greater than 17")
else:
    print("The value is not greater than 3 or 7")

# NOTE: 3. Nested if-else

if(a>3):
    print("a is greater than 3")
    if(a>13):
        print("a is greater than 13")
    else:
        print("a is not greater than 13")
else: 
    print("a is not greater than 3")

