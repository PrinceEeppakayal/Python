myDict = {
    "Fast": "In a quick manner",
    "Prince": "A coder",
    "Marks": [1, 2, 3],
    "anotherDict": {"Prince": "Cricketer"}
}

 # This will print the value of key "Fast" & "Prince" from the dictionary
print(myDict["Fast"]) 
print(myDict["Prince"])  

print(myDict["Marks"])  # We can also print a list using dictionary

print(myDict["anotherDict"]["Prince"]) # We can also print a dictionary inside a dictionary
