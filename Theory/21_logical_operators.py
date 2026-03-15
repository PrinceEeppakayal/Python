
# NOTE: Short circuiting/Logical operators (and, or, not) in if-else statements 

a = 10
if(a>3 and a>13):
    print("a is greater than 3 and 13")
else:
    print("a is not greater than 3 and 13")

if(a>3 or a>13):
    print("a is greater than 3 or 13")
else:
    print("a is not greater than 3 or 13")

if(not a>3):
    print("a is not greater than 3")
else:
    print("a is greater than 3")

if(a>3 and not a>13):
    print("a is greater than 3 but not 13")
else:
    print("a is not greater than 3 but 13")

if(a>3 and a>13 and a>7):
    print("a is greater than 3, 13 and 7")
else:
    print("a is not greater than 3, 13 and 7")