print("---Welcome to User Tag Generator---")
print("To generate the usertag provide below details:")
first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
birth_year = int(input("Enter the birth year: "))

full_name = first_name + last_name
tag_prefix = first_name[0:2] + last_name[-2:]
age_code = (2026 - birth_year) * 2
user_tag = tag_prefix + str(age_code)
print(full_name)
print("The generated user_tag is:",user_tag)
