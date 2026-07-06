
# INFO: An environment which is same as the system interpretor but is isolated from the other python environments on the system.

# NOTE: Installation: To use virtual environments, we write 

'''pip install virtualenv''' # --> Install the package

# We create a new environment using:

'''virtualenv myprojectenv''' # --> Creates a new venv
# NOTE: For linux: source myprojectenv/bin/activate
# NOTE: For Windows: myprojectenv/Scripts/activate.ps1
# NOTE: https://stackoverflow.com/questions/18713086/virtualenv-wont-activate-on-windows

# INFO:The next step after creating the virtual environment is to activate it. We can now use this virtual environment as a separate python installation.

# NOTE: pip install command: pip freeze returns all the packages installed in a given python environment along with the versions

'''pip freeze > requirements.txt'''

# INFO: The above command creates a file named requirements.txt in the same directory containing the output of pip freeze. We can distribute this file to other users and they can recreate the same environment using:

'''pip install -r requirements.txt'''

# INFO: Lambda functions: Functions created using an expression using lambda keyword

# SYNTAX: 
'''lambda arguments: expressions''' # --> can be used as a normal function

# EXAMPLE: 
square = lambda x: x*x
square(6) # --> returns 36

sum = lambda a,b,c: a+b+c
sum(1,2,3) # --> returns 6

# INFO: bin method (Strings): creates a string from iterable objects
'''l = ["apple", "mango", "banana"]
"and".join(l)
The above line will return "apple, and, mango, and, banana"'''

# EXAMPLE:
l = ["Laptop", "Keyboard", "Mouse", "Nividia 4060 Graphics Card", "Intel i7 13th Gen Processor", "24GB DDR5 RAM", "1.5TB SSD"]

sentence = "and".join(l)
print(sentence)
print(type(sentence))

# INFO: format method (Strings): Formats the values inside the string into a desired output

'''template.format(p1, p2, ...)'''
                     # '--> arguments

# INFO: Syntax for format looks like:
'''"{} is a good {}".format("Prince","boy")''' # --(1)
'''"{1} is a good {0}".format("Prince","boy")''' # --(2)

# Output for (1): Prince is a good boy
# Output for (2): boy is a good Prince

# EXAMPLE:
name = "Prince"
age = 20
a = "My name is {} and I am {} years old".format(name, age)
print(a)

# INFO: Map, Filter & Reduce: Map applies a function to all the items in an input_list.

# SYNTAX: 
'''map(function, input_list)'''
       #  '--> can be lambda function

# EXAMPLE:
def square(num):
    return num*num
l = [1,2,3]
result = list(map(square, l))
print(result) 

# INFO: Filter creates a list of items for which the functions returns true.
    
'''list(filter(function, input_list))'''
              #  '--> can be lambda function 

# EXAMPLE:
def is_even(n):
    return n % 2 == 0

l = [1, 2, 3, 4, 5, 6]
result = list(filter(is_even, l))
print(result)

# INFO: Reduces applies a rating computation to sequential pair of elements

'''from functools import reduce
val = reduce(function, list1)'''
             #  '--> can be lambda function

# INFO: If the function computes sum of two numbers and the list is [1,2,3,4]

'''    1  2  3  4 
       '--'
         3  3  4
         '--'         # ==> Sequential Computation
           6  4
           '--'
            10       '''

# EXAMPLE: 
from functools import reduce

sum = lambda a,b : a+b
l = [1,2,3,4]

result = reduce(sum, l)
print(result)