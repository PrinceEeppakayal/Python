name = "Prince"

#   P  R  I  N  C  E
#   0  1  2  3  4  5
#  -6 -5 -4 -3 -2 -1 


# Python starts to count the words from 0
# Negative indics is used when we want to access the end but we don't know the length of string then we access it using print(name[:-1]) 
# We start the nagative indics from -1 not from 0 in reverse order 

''' Slicing means till what no. you want to print 
    eg.print(name[0:4])
    The output will be Prin
   *It will provide output less than you asked range for by -1* '''   

''' You cannot change the character of string it will show error
    eg.name[3] = "d" '''

''' We can make slice a string from wherever we need by giving the range from where to start and where to end 
    eg.print(name[2:6])
    The output will ince '''

# print(name[0])  --> is same as print(name[0:1])
# print(name[0:1])  --> P
# print(name[0:2])  --> Pr
# print(name[1:3])  --> ri
# print(name[0:4])  --> Prin
# print(name[2:5])  --> inc
# print(name[3:6])  --> nce
# print(name[1:6])  --> rince
print(name[:4])  # is same as print(name[0:4])
print(name[1:])  # is same as print(name[1:6])
print(name[-4:-1]) # is same as print(name[2:5])
print(name[0:5])  # --> Princ

'''If you count the no of words normally it will show error
   eg.print(name[6])'''

# When we want to skip any words we slice using skip value after writing the range we write the value of character we want to skip 
print(name[0:5:2])  # --> Pic  here we skip 2 characters from the start till 5 
''' i.e. P which is 0 is printed then skipping 2 charcters including the printed one then i which is 2 is printed then skipping 
         2 charcters including the printed one then c which is 4 is printed as we know the output provided will be less than range by -1 ''' 
