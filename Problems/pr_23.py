
# QUESTION: Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

a = int(input("Enter the marks of first subject: "))
b = int(input("Enter the marks of second subject: "))
c = int(input("Enter the marks of third subject: "))

if(a<33 or b<33 or c<33):
    print("you are fail because you have less than 33% in one of the subjects")
elif(a+b+c)/3 <40:
    print("you are fail because you have less than 40%")
else:
    print("congratulations! you have passed the exam")
