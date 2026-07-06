
# QUESTION: Store the multiplication tables generated in pr_69 in a file named Tables.txt

num = int(input("Enter a number: "))
table = [num * i for i in range(1, 11)]
print(f"Multiplication table of {num}: {table}")

with open("logs//Tables.txt", 'w') as f:
    f.write(f"Multiplication table of {num}: {table}\n")