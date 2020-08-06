# Day_7: August/03/2020
# In the name 0f Allah..
# Me: Alifa Ara Heya
# From: 30 Days of Python by Asabeneh (day-4 exercises)

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print("Thirty " + "Days " + "Of " + "Python")    # Thirty Days Of Python


# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print('Coding ' + 'For ' + 'All')                # Coding For All


# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"


# 4. Print the variable company using print().
print(company)                                   # Coding For All


# 5. Print the length of the company string using len() method and print().
print(len(company))                              # 14


# 6. Change all the characters to capital letters using upper() method.
print(company.upper())                           # CODING FOR ALL


# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())                           # coding for all


# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())                      # Coding for all
print(company.title())                           # Coding For All
print(company.swapcase())                        # cODING fOR aLL


# 9. Cut(slice) out the first word of Coding For All string.
print(company[0])                                # C


# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
print("Coding" in company)                       # True
# or,
print("Coding" in "Coding For All.")             # True
# or,
print(company.index("Coding"))                   # 0 (First)
# or,
print(company.find("Coding"))                    # 0


# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding", "Python"))       # Python For All


# 12. Change Python for Everyone to Python for All using the replace method or other methods.
motto = "Python for Everyone"
print(motto.replace("Everyone", "All"))          # Python For All


# 13. Split the string 'Coding For All' using space as the separator (split()) .
print("Coding For All".split(" "))               # ['Coding', 'For', 'All']
print("Coding For All".split())                  # ['Coding', 'For', 'All']


# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" .split())    # ['Facebook,', 'Google,', 'Microsoft,', 'Apple,', 'IBM,', 'Oracle,', 'Amazon']


# 15. What is the character at index 0 in the string Coding For All.
print("Coding For All" [0])                      # C


# 16. What is the last index of the string Coding For All.
print("Coding For All" [-1])                      # l


# 17. What character is at index 10 in "Coding For All" string.
print("Coding For All" [10])                      # space


# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.


# 19. Create an acronym or an abbreviation for the name 'Coding For All'.


# 20. Use index to determine the position of the first occurrence of C in Coding For All.
print("Coding For All".index("C"))                 # 0


# 21. Use index to determine the position of the first occurrence of F in Coding For All.
print("Coding For All".index('F'))                 # 7


# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print("Coding For All People.".rfind("l"))         # 19


# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find('because'))     # output: 31  (I could have used variable here.)


# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))


# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.index('because'))    # output: 31   (at first, I found the index no of first 'because' using .index() method)
print('You cannot end a sentence with because because because is a conjunction'.rindex('because'))   # output: 47   (then, I found the index no of last 'because' using .rindex() method, that gave us the start point of last 'because')
print('You cannot end a sentence with because because because is a conjunction'[31 : 54])            # because because because (finally, I added 6 with 46 and 1 more because the last index is excluded when using in range. That gave me 54.)

# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find('because'))     # output: 31


# 27. same question 25

# 28. Does ''Coding For All' start with a substring Coding?
print("'Coding For All" .startswith('Coding'))    # False (no)


# 29. Does 'Coding For All' end with a substring coding?
print("Coding For All".endswith('coding'))        # False (no)


# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip())          # Coding For All
check = '   Coding For All      '.strip()
print(check.endswith(" "))                        # False
print(check.endswith("l"))                        # True (so we successfully removed the spaces)


# 31. Which one of the following variables return True when we use the method isidentifier():
# ~30DaysOfPython
# ~thirty_days_of_python
print('30DaysOfPython'.isidentifier())            # False (because variable doesn't start with number)
print('thirty_days_of_python'.isidentifier())     # True


# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(python_libraries))                # Django# Flask# Bottle# Pyramid# Falcon


# 33. Use the new line escape sequence to separate the following sentences.
# ~I am enjoying this challenge.
# ~I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")


# 34. Use a tab escape sequence to write the following lines.
#Name      Age     Country
#Asabeneh  250     Finland
print("Name\tAge\tCountry\nAsabeneh\t250\tFinland".expandtabs(10))
#or,
one = "Name\tAge\tCountry\nAsabeneh\t250\tFinland"
print(one.expandtabs(10))                         # perfect


# 35. Use the string formating method to display the following:
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
radius = 10
pi = 3.14
area = int(pi * radius ** 2)
print(f"The area of a circle with radius {radius} is {area} meters square.")


# 36. Make the following using string formating methods:
a = 8
b = 6
print(f'{a} + {b} = {a + b}')                     # 8 + 6 = 14
print(f'{a} - {b} = {a - b}')                     # 8 - 6 = 2
print(f'{a} * {b} = {a * b}')                     # 8 * 6 = 48
print(f'{a} / {b} = {a / b :.2f}')                # 8 / 6 = 1.33
print(f'{a} % {b} = {a % b}')                     # 8 % 6 = 2
print(f'{a} // {b} = {a // b}')                   # 8 // 6 = 1
print(f'{a} ** {b} = {a ** b}')                   # 8 ** 6 = 262144

print("Alhamdulillah finished")