myDict = {
    # keys: values
    "Fast": "In a quick manner",
    "Prince": "A coder",
    "Marks": [1, 2, 3],
    "anotherDict": {"Prince": "Cricketer"},
    1 : 2,
}

print(myDict.keys()) # Prints the keys of the dictionary  

print(myDict.values()) # Prints the values of the dictionary

print(myDict.items()) # Prints the (key, value) for all contents of the dictionary

print(myDict)

updateDict = {
    "Om": "Friend",
    "Vedant": "Friend",
    "Jyotiraditya": "Friend",
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("Prince")) # Prints value associated with key "Prince"
print(myDict["Prince"]) # Prints value associated with key "Prince"

# The difference between .get and [] syntax in Dictionaries?
print(myDict.get("Prince2")) # Returns None as Prince2 is not present in the dictionary
# print(myDict["Prince2"]) # throws an error as Prince2 is not present in the dictionary

print(myDict.pop("Prince")) # Removes element with key "Prince"

print(myDict.popitem()) # Removes the arbitrary key-value pair

print(myDict.setdefault("Prince", "Cricketer")) # Inserts key-value pair "Prince":"Cricketer"

print(myDict.fromkeys(updateDict, "Friend")) # Returns a dictionary with keys from updateDict and values as "Friend"

print(myDict.clear()) # Removes all items from the dictionary

print(myDict.copy()) # Returns a copy of the dictionary

