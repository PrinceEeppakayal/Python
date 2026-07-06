
# INFO: There are many built-in exceptions which are raised in Python when something goes wrong. Exceptions in Python can be handled using a try statement. The code that handles the exception is written in the except clause. 

try:
    pass                    
except Exception as e:   # --> Code which might throw Exception
    print(e)

# EXAMPLE: 
try:
    a = int(input("Enter a number: "))
    b = 1/a
    print(b)
except Exception as e:
    print(f"Exception occurred: {e}")

# When the exception is handled, the code flow continues without program interruption. We can also specify the exceptions to catch like below:

try:
    pass
except ZeroDivisionError:
    pass
except TypeError:
    pass
except:
    pass        # --> All other exceptions are handled here

# EXAMPLE: 
try:
    a = int(input("Enter a number: "))
    b = 1/a
    print(b)
except ZeroDivisionError as e:
    print(f"Please enter a non-zero value: {e}")
except TypeError as e:
    print(f"Enter a valid number: {e}")

print("Program continues...")

# INFO: Raising Exceptions: We can raise custom exceptions using the raise keyword in python. 

# EXAMPLE: 
def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Please provide a valid number")
    
a = increment("af32")
print(a)   

# INFO: try with else clause: Sometimes we want to run a piece of code when try was successful.

try:
    pass
except:
    pass
else:
    pass     # --> This is executed only if the try was successful

# EXAMPLE:
try:
    a = int(input("Enter a number: "))
    b = 1/a
    print(b)
except Exception as e:
    print(f"Exception occurred: {e}")
else:
    print("You are successful!")

# INFO: try with finally: Python offers a finally clause which ensures execution of a piece of code irrespective of the exception. 

try:
    pass
except:
    pass
finally:
    pass    # --> Executed regardless of error!

# EXAMPLE:
try:
    a = int(input("Enter a number: "))
    b = 1/a
    print(b)
except Exception as e:
    print(f"Exception occurred: {e}")
finally:
    print("We are done here!") # --> This will be executed regardless of the exception

# INFO: if__name__ == '__main__' in Python: __name__ evaluates to the name of the module in Python from where the program is ran.

# NOTE: If the module is being run directly from the command line, the __name__ is set to string "__main__". Thus this behavior is used to check whether the module is run directly or imported to another file.

# EXAMPLE:
# 1st file: main.py
'''def greet(name):
    print(f"Hello, {name}!")
if __name__ == '__main__':
    greet("Alice")'''  # --> This will only be executed if the module is run directly and not imported to another file.

# 2nd file: main2.py
'''import main
main.greet("Prince")'''  # --> This will not execute the greet function in main.py because we are importing it to another file and not running it directly.

# INFO: The global keyword: global keyword is used to modify the variable outside of the current scope.

# EXAMPLE:
a = 10 # --> This is Global variable 
def func():
    global a  # --> This allows us to modify the global variable a inside the function
    print(a)
    a = 20   # --> This is Local variable 
    print(a)

func()
print(a) # --> This will print 20 because we have modified the global variable a inside the function using global keyword.

# INFO: enumerate function in Python: The enumerate function adds counter to an iterable and returns it 
# list1 = [1, 2, 55, 32]
# for i, item in list1:
#     print(i, item) # --> Prints the items of list1 with index!

# EXAMPLE:
list1 = [3, 49, "Prince", 60.2, True]
for index, item in enumerate(list1): # --> This will print the items of list1 with index using enumerate function
    print(index, item) 

# INFO: list comprehensions: list comprehension is an elegant way to create lists based on existing lists.

# list1 = [1, 7, 12, 11, 22]
# list2 = [i for item in list1 if item>8]

# EXAMPLE:
list1 = [3, 49, 12, 34, 64, 39]
list2 = [i for i in list1 if i%2==0]
print(list2) # --> This will print the even numbers from list1 using list comprehension.