a = int(input("Enter marks in subject 1: "))
b = int(input("Enter marks in subject 2: "))
c = int(input("Enter marks in subject 3: "))
d = int(input("Enter marks in subject 4: "))

total = a+b+c+d
percentage = (total/400)*100

print("Total marks: ", total)
if(percentage>=90):
    print("Grade: Ex")
elif(percentage>=80):
    print("Grade: A")
elif(percentage>=70):
    print("Grade: B")
elif(percentage>=60):
    print("Grade: C")
elif(percentage>=40):
    print("Grade: D")
else:
    print("Grade: F")
