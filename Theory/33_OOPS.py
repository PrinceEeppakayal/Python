
# INFO: Solving a problem by creating objects is one of the most popular approaches in programming. This is called Object-Oriented Programming (OOP).

# NOTE: This concept focused on using reusable code.  --> Implements DRY principle (Don't Repeat Yourself). 

# CLASS: A class is a blueprint for creating objects.

# NOTE: PascalCase: The name of the class should be in PascalCase. It means the first letter of each word should be capitalized. For example, MyClass, StudentDetails, etc.

# NOTE: camelCase: The name of the object should be in camelCase. It means the first letter of the first word should be in lowercase and the first letter of each subsequent word should be capitalized. For example, myObject, studentDetails, etc.

# Object: An object is an instantiation of a class. When class is defined, a template (info) is defined. Memory is allocated only after object instantiation. Objects of a given class can invoke the methods available to it without revealing the implementation details to the user. --> Abstraction & Encapsulation 

# Modelling a problem in OOPs
# we identify the following in our problem

# Noun --> Class --> Employee
# Adjective --> Attribute --> name, age, salary
# Verb --> Method --> getSalary(), increment()

# INFO: Class Attributes: An attribute that belongs to the class rather than a particular object.
# Example:
class Employee:
    company = "Google" # --> specific to each class

prince = Employee() # --> object instantiation
print(prince.company)
Employee.company = "YouTube" # --> changing the class attribute 
print(prince.company) # --> it will reflect the change in the class attribute

# INFO: Instance Attributes: An attribute that belongs to the Instance (object). Assuming the class from the previous example:
class Employee:
    company = "Google"
    salary = 1000 

prince = Employee()
panda = Employee()
prince.salary = 5000 # --> changing the instance attribute for prince object
print(prince.salary) # --> it will reflect the change in the class attribute because it is an instance attribute
print(panda.salary) # --> it will not reflect the change in the class attribute because it is an instance attribute
# print(prince.address) # --> it will give an error because address is not defined in the class or instance

# NOTE: Instance attributes take preferences over class attributes during assignment & retrieval

# INFO: Self: refers to the instance of the class. It is automatically passed with a function call from an object

# prince.getSalary() # --> here self is prince
              # '--> equivalent to Employee.getSalary(prince) 

# The function getSalary is defined as:
class Employee:
    company = "Google"
    
    def getSalary(self):
        print("Salary is not there")

class Employee:
    company = "Google"

    def getSalary(self): 
        print(f"The salary of the employee working in {self.company} is {self.salary}")

prince = Employee()
prince.salary = 5000
prince.getSalary() # same as Employee.getSalary(prince) 


# INFO: Static Method: Sometimes we need a function that doesn't use the self parameter we can define a static method like this:

@staticmethod # --> decorator to mark greet as a static method
def greet():
    print("Hello user")

# EXAMPLE:
@staticmethod
def time():
    print("The time is 12PM")

# INFO: __init__() Constructor: It is a special method which is first run as soon as the object is created. __init__() method is also known as constructor. It takes self argument and can also take further arguments. 

# EXAMPLE: 
class Employee:
    company = "Google"

    def __init__(self, name, salary, subcompany):
        self.name = name 
        self.salary = salary
        self.subcompany = subcompany
        print("Employee object is created")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subcompany of the employee is {self.subcompany}")

    def getSalary(self):
        pass

prince = Employee("Prince", 5000, "Gemini") # --> Object can be instantiated using constructor like this!
prince.getDetails()
prince.getSalary()

