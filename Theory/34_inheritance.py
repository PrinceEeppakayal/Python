
# INFO: Inheritance is a way of creating a new class from an existing class. The new class is called a subclass, and the existing class is called a superclass. The subclass inherits all the attributes and methods of the superclass, and can also have its own attributes and methods.

# SYNTAX:
class Employee:      # --> Base or Super class
    pass

class Programmer(Employee):   # --> Derived or Sub or Child class 
    pass

# NOTE:  We can use the methods and attributes of Employee in Programmer object. Also, we can overwrite or add new attributes and methods in Programmer class.

# EXAMPLE:

class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    company = "Gmail"

    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):
        print("This is a programmer")

e = Employee() 
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company) # -->this will print "Gmail" because the company attribute in Programmer class is overwriting the company attribute in Employee class. If the company attribute was not defined in Programmer class, then it would have printed Employee class's company attribute 

# NOTE: Types OF Inheritance:
# INFO: 1. Single Inheritance: Single inheritance occurs when a child class (subclass) inherits only a single parent class (superclass). In this type of inheritance, the child class can access the properties and methods of the parent class.

                #   Parent
                #     |
                #   Child

# EXAMPLE:
class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")
    
class Programmer(Employee):
    language = "Python"

    def getLanguage(self):
        print(f"The language is {self.language}")

p = Programmer()
p.showDetails()

# INFO: 2. Multiple Inheritance: Multiple inheritance occurs when a child class (subclass) inherits from more than one parent class (superclass). In this type of inheritance, the child class can access the properties and methods of all the parent classes.

                #  Parent1   Parent2
                #     |         |
                #     '---------'
                #          |
                #        Child

# EXAMPLE:
class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Freelancer:
    def showDetails(self):
        print("This is a freelancer")

class Programmer(Employee, Freelancer): # --> Programmer class is inheriting from both Employee and Freelancer classes but the one which is written first will be given priority in case of method overriding. In this case, Employee class's showDetails() method will be called when we call p.showDetails() because Employee class is written first in the inheritance list.
    language = "Python"

    def getLanguage(self):
        print(f"The language is {self.language}")

p = Programmer()
p.showDetails()

# INFO: 3. Multilevel Inheritance: Multilevel inheritance occurs when a child class (subclass) inherits from a parent class (superclass), and then another child class inherits from that child class. In this type of inheritance, the child class can access the properties and methods of all the parent classes in the hierarchy.

                #   Parent
                #     |
                #   Child1
                #     |
                #   Child2


# EXAMPLE:
class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"

    def getLanguage(self):
        print(f"The language is {self.language}")

class FrontendDeveloper(Programmer):
    def showDetails(self):
        print("This is a frontend developer")

f = FrontendDeveloper()
f.showDetails()

# INFO: Super Method: Super method is used to access the methods of parent class (superclass) in the child class (subclass). It is used to call the constructor of the parent class and to access the methods of the parent class.

# super()__init__( )
#                 '--> calls the constructor of the parent class 

# EXAMPLE:
class Employee:
    company = "Google"

    def __init__(self):
        print("Employee constructor called")

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):

    language = "Python"

    def __init__(self):
        super().__init__() # --> calling the constructor of the parent class
        print("Programmer constructor called")

    def getLanguage(self):
        print(f"The language is {self.language}")

p = Programmer()

# INFO: class methods: A class method is a method which bound to the class and not the object of the class. It can modify a class state that applies across all instances of the class. A class method takes cls as the first parameter while a static method needs no specific parameters. @classmethod decorator is used to define a class method.

# SYNTAX: 
@classmethod
def Employee(cls, p1, p2): # --> cls is the first parameter of a class method which refers to the class itself. We can use cls to access the attributes and methods of the class.
    pass

# INFO: @property: It is a decorator used to define a class method. It is used to access the attributes of the class. It is used to access the attributes of the class without creating an object of the class.

# Consider the following case:
class Employee:
    company = "Google"
    salary = 5000
    salaryBonus = 1000

    @property
    def totalSalary(self):
        return self.salary + self.salaryBonus
    
    @totalSalary.setter
    def totalSalary(self, value):
        self.salaryBonus = value - self.salary

e = Employee()
print(e.totalSalary) # --> this will print 6000 because totalSalary is a property and it is returning the sum of salary and salaryBonus. We can access totalSalary without creating an object of the class because it is a property.  
e.totalSalary = 7000
print(e.salary)
print(e.salaryBonus)

# if e = Employee() is an object of class employee, we can print(e.totalSalary) to print the etotalSalary/ call totalSalary() function. 

# INFO: @.getters and @.setters: The method name with @property decorator is called getter method. We can define a getter method like a . We can define a function + @name.setter decorator like above to define a setter method. The setter method is used to set the value of the property. We can use the setter method to set the value of the property without creating an object of the class.

# INFO: Operator Overloading: Operators in python can be overloaded using dunder methods. These methods are called when a given operator is used on the objects. Operators in python can be overloaded using the following methods:

''' p1 + p2 --> p1.__add__(p2)''' # --> this will call the __add__ method of the class of p1 and pass p2 as an argument to it. We can define the __add__ method in the class to overload the + operator.

#EXAMPLE:
class Number:
    def __init__(self, num):
        self.num = num
    def __add__(self, num2):
        print("Lets add")
        return self.num + num2.num
n1 = Number(5)
n2 = Number(10)
sum = n1 + n2
print(sum) # --> this will call the __add__ method of the Number class and pass n2 as an argument to it. The __add__ method will return the sum of n1.num and n2.num which is 15.


'''p1 - p2 --> p1.__sub__(p2)''' # --> this will call the __sub__ method of the class of p1 and pass p2 as an argument to it. We can define the __sub__ method in the class to overload the - operator.

#EXAMPLE:
class Number:
    def __init__(self, num):
        self.num = num
    def __sub__(self, num2):
        print("Lets subtract")
        return self.num - num2.num
n1 = Number(5)
n2 = Number(10)
sub = n1 - n2
print(sub) # --> this will call the __sub__ method of the Number class and pass n2 as an argument to it. The __sub__ method will return the difference of n1.num and n2.num which is -5.

'''p1 * p2 --> p1.__mul__(p2)''' # --> this will call the __mul__ method of the class of p1 and pass p2 as an argument to it. We can define the __mul__ method in the class to overload the * operator.

#EXAMPLE:
class Number:
    def __init__(self, num):
        self.num = num
    def __mul__(self, num2):
        print("Lets multiply")
        return self.num * num2.num
n1 = Number(5)
n2 = Number(10)
mul = n1 * n2
print(mul) # --> this will call the __mul__ method of the Number class and pass n2 as an argument to it. The __mul__ method will return the product of n1.num and n2.num which is 50.

'''p1 / p2 --> p1.__truediv__(p2)''' # --> this will call the __truediv__ method of the class of p1 and pass p2 as an argument to it. We can define the __truediv__ method in the class to overload the / operator.

#EXAMPLE:
class Number:
    def __init__(self, num):
        self.num = num
    def __truediv__(self, num2):
        print("Lets divide")
        return self.num / num2.num
n1 = Number(5)
n2 = Number(10)
div = n1 / n2
print(div) # --> this will call the __truediv__ method of the Number class and pass n2 as an argument to it. The __truediv__ method will return the quotient of n1.num and n2.num which is 0.5.

'''p1 // p2 --> p1.__floordiv__(p2)''' # --> this will call the __floordiv__ method of the class of p1 and pass p2 as an argument to it. We can define the __floordiv__ method in the class to overload the // operator.

#EXAMPLE:
class Number:
    def __init__(self, num):
        self.num = num
    def __floordiv__(self, num2):
        print("Lets floor divide")
        return self.num // num2.num
n1 = Number(5)
n2 = Number(10)
fldiv = n1 // n2
print(fldiv) # --> this will call the __floordiv__ method of the Number class and pass n2 as an argument to it. The __floordiv__ method will return the floor division of n1.num and n2.num which is 0 because 5 // 10 is 0 in floor division.

# Other dunder/magic methods in python:
'''__str__()''' # --> used to set what gets displayed upon calling str(obj). 

#EXAMPLE:
class Number:
    def __init__(self, num):
        self.num = num
    def __str__(self):
        return str(self.num)
n = Number(5)
print(n) # --> this will call the __str__ method of the Number class and return the string representation of n1.num which is "5"

'''__len__()''' # --> used to set what gets displayed upon calling __len__() or len(obj).

#EXAMPLE:
class Number:
    def __init__(self, num):
        self.num = num
    def __len__(self):
        return len(str(self.num))
n = Number(5)
print(n)
print(len(n)) # --> this will call the __len__ method of the Number class and return the length of the string representation of n1.num which is 1 because "5" has a length of 1.