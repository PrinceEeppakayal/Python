
# QUESTION: Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files are not present a message without exiting the program must be printed prompting the same.

def readfile(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {filename} not found")

readfile("1.txt")
readfile("2.txt")
readfile("3.txt")