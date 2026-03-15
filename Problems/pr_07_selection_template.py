letter = ''' \nDear <|NAME|>,
Greetings from ABC company. I am happy to tell you about your selection
You are selected!
Have a great day ahead!
Thanks and Regards,
XYZ

Date: <|DATE|> 
'''
name = input("Enter your name : ")
date = input("Enter Date : ")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)