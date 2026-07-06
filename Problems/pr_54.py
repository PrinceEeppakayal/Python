
# QUESTION: Create a class programmer for storing information of few programmers working at microsoft

class programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product
    
    def getInfo(self):
        print(f"The name of the programmer is {self.name} and the product working on is {self.product}")

prince = programmer("Prince", "Xbox")
panda = programmer("Panda", "Github")   
prince.getInfo()
panda.getInfo()     