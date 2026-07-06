
# QUESTION: Write a program to greet all the person names stored in a list l1 and which starts with P.

l1 = ["Prince", "Om", "Vedant", "Panda"]

for name in l1:
    if name.startswith("P"):
        # print("Hello " + name)
        print(f"Hello {name}")