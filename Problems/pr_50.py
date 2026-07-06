
# QUESTION: Write a program to find out whether a file is identical & matches the contents of another file

file1 = "this.txt"
file2 = "copy_this.txt"

with open("this.txt") as f:
    f1 = f.read()

with open("copy_this.txt") as f:
    f2 = f.read()

if f1 == f2:
    print("Files are identical")
else:
    print("Files are not identical")