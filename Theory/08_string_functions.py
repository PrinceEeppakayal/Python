story = "there was a man named Suresh lied in the village Dholakpur. He was a farmer"

# len string tells the no. of characters in the string. 
print(len(story))  # --> 74

# string.endswith string tells whether the word written is ending the string. It replies in true or false
print(story.endswith("farmer"))  # --> True
# print(story.endswith("man")) --> False

# string.count string counts the total no. of occurence of any character in string 
print(story.count("a"))  # --> 9

# string.capitalize string capitalizes the first character of the given string
print(story.capitalize())

# string.find(word) string finds a word and returns the index of first occurence of that word in the string
print(story.find("Suresh"))  # --> 21

# string.replace(oldword,newword) string replaces the oldword with newword in the entered string
print(story.replace("Suresh","Ramesh"))  # --> there was a man name Ramesh lied in the village Dholakpur. He was a farmer

# string.upper() string converts the whole string into uppercase letters
print(story.upper()) 

# string.isupper() string checks whether the whole string is in uppercase letters or not. It replies in true or false
print(story.isupper())

# string.lower() string converts the whole string into lowercase letters
print(story.lower())

# string.islower() string checks whether the whole string is in lowercase letters or not. It replies in true or false
print(story.islower())

# string.title() string converts the first character of each word in the string into uppercase letter
print(story.title())

# string.isalpha() string checks whether the whole string is made up of only alphabets or not. It replies in true or false
print(story.isalpha())  # --> False because there are spaces in the string

# string.isdigit() string checks whether the whole string is made up of only digits or not. It replies in true or false
print(story.isdigit())  # --> False because there are alphabets and spaces in the string

# string.isalnum() string checks whether the whole string is made up of only alphabets and digits or not. It replies in true or false
print(story.isalnum())  # --> False because there are spaces in the string

# string.split() string splits the string into list of words
print(story.split())  # --> ["there", "was", "a", "man", "named", "Suresh", "lied", "in", "the", "village", "Dholakpur.", "He", "was", "a", "farmer"]

# string.strip() string removes the extra spaces from the beginning and end of the string
story2 = "   there was a man named Suresh lied in the village Dholakpur. He was a farmer   "
print(story2.strip())  # --> "there was a man named Suresh lied in the village Dholakpur. He was a farmer"

# string.replace(oldword,newword) string replaces the oldword with newword in the entered string
print(story.replace(" ", "_"))  # --> there_was_a_man_named_Suresh_lied_in_the_village_Dholakpur._He_was_a_farmer

# string.index(word) string finds a word and returns the index of first occurence of that word in the string. It gives error if the word is not found in the string
print(story.index("Suresh"))  # --> 21

# string[num] string finds a word and returns the index of first occurence of that word in the string. It gives -1 if the word is not found in the string
print(story[0])  # --> "t"

