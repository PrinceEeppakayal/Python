# String Concatenating and its use in the sentences
character_name = "Prince"
character_age = str(20)
character_percentage = str(80.80)
character_result = str(True)

print("This boy name is " + character_name + ",")
print("His age is " + character_age + " years old.") 
print("His percentage is " + character_percentage + "%")
print("His result is " + character_result + ".")

#NOTE: We cannot concatenate string with other data types like integer, float and boolean so we have to convert them into string using str() function before concatenating them with other strings

phrase = "This guy name is"
print(phrase + " Prince")

Greeting = "Good Morning, "
Name = "Prince"
Surname = "Eppakayal"

# Concatenating means adding of strings together
c = (Greeting + Name + Surname)
print(c)
