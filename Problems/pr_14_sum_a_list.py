import random 

no= [random.randint(10,100) for i in range(20)]
print(no)

no = [num for num in no if not (20<= num <= 50)]
print(no)