# List slicing
friends = ["Prince", "Rahul", "Om", "Vedant", "Jyotiradtiya", "28"]
print(friends[0:4]) #--> ['Prince', 'Rahul', 'Om', 'Vedant']
# same as string slicing 

# List slicing with skip value
print(friends[0:4:2]) #--> ['Prince', 'Om']

# List slicing with negative index
print(friends[-4:]) #--> ['Om', 'Vedant', 'Jyotiradtiya', '28']

# List slicing with negative index and skip value
print(friends[-4:-1:2]) #--> ['Om', 'Jyotiradtiya']
