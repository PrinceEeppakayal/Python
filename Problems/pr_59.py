
# QUESTION: Can you change the self parameter inside a class to something else (say 'prince'). Try changing self to 'slf' or 'prince' and see the effects.

class sample:
    def __init__(prince, name):
        prince.name = name

obj = sample("Prince")
print(obj.name)

# NOTE: Yes you can change the self parameter to something else. But it will cause difficult in understanding the code for other programmers. 