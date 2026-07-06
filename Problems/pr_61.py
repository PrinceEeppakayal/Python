
# QUESTION: Create a class pets from a class Animals and further create class Dog from Pets. Add a method bark to class Dog.

class Animals:
    animaltype = "Mammal"

class Pets:
    color = "White"

class Dog:
    @staticmethod
    def bark():
        print("Bow!! Bow!!")

d = Dog
d.bark()
    