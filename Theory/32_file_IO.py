# The random access memory is volatile and all its contents are lost once a program terminates so in order to persists the data forever, we use files.

# A file is data stored in a storage device. A Python program can talk to the file by reading content from it and writing content to it. 

# INFO: Types of files:
# 1. Text files (.txt, .c, etc)
# 2. Binary files (.jpg, .dat, etc)

# Opening a file:
# Python has an open() function for opening files. It takes 2 parameters: filename and mode
    
# f = open("sample.txt", "r")
#       |      |        '--> mode of opening (read mode)
#       |      '--> filename
#       '--> open is a built-in function

# Reading a file: 
from os import read


f = open("sample.txt") # By default, the mode is r --> open the file in r mode
# data = f.read() # --> reads its contents
data = f.read(5) # reads the first 5 characters from the file
print(data) # --> prints its contents
f.close() # --> close the file

# Other methods to read a file:
# We can also use f.readline() function to read a full line at a time. 

f = open("sample.txt") 
data = f.readline() # reads the first line from the file
print(data) 
data = f.readline() # reads the second line from the file
print(data) 
f.close() 

# INFO: Modes of opening a file:
# r --> open for reading (default)
# w --> open for writing (creates a new file if it does not exist or truncates the file if it already exists)
# a --> open for appending (creates a new file if it does not exist or adds to the end of the file if it already exists)
# + --> open for updating (allows both reading and writing to the file)

# 'rb' will open for read in binary mode
# 'rt' will open for read in text mode

# Writing files:
# In order to write to a file, we first open it in write or append mode after which, we use the python's f.write() method to write  to the file.

f = open("sample1.txt", "w") # open the file in write mode
f.write("This is a sample text file.\n") # write to the file and can be called multiple times
f.write("This is not a sample text file.\n") 
f.close()

# With Statement:
# The best way to open and close the file automatically is the with statement.

with open("sample.txt", 'r') as f:
    a = f.read()
with open("sample.txt", 'w') as f:
    a = f.write("message")
print(a) # |
        #  '--> Dont need to write f.close() as it is done automatically