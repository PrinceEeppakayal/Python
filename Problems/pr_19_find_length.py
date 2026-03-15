s = set()

s.add(20)  
s.add(20.0) # 20.0 is same as 20
s.add('20')  # '20' is different from 20

print(s)
print(len(s)) 