
# QUESTION: Add a static method in problem 2 to greet the user with hello

class calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"The square of {self.number} is {self.number ** 2}")

    def squareroot(self):
        print(f"The squareroot of {self.number} is {self.number ** 0.5}")

    def cube(self):
        print(f"The cube of {self.number} is {self.number ** 3}")
        
    @staticmethod
    def greet():
        print("***WELCOME TO THE CALCULATOR PROGRAM***")

num = int(input("Enter the number: "))
a = calculator(num)
a.greet()
a.square()
a.squareroot()
a.cube()