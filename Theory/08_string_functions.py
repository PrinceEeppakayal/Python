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

