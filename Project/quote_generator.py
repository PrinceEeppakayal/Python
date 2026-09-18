print("--- Welcome to the Custom Quote Generator ---")
author_name = input("Enter the author name: ")
quote_text = input("Enter the quote: ")
publication_year = int(input("Enter the publication year: "))

author_name = author_name.strip().title()
formatted_quote = f"\"{quote_text}\""
quote_age = 2026 - publication_year
line = f'''{formatted_quote}
\t-{author_name} (Age: {quote_age} years ago)'''
print(line)