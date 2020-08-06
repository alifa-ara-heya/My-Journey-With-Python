# Day_7: August/03/2020
# In the name 0f Allah..
# Me: Alifa Ara Heya
#From: Asabeneh

# .capitalize() converts the first character of the string to capital letter.
challenge = "thirty days of python"
print(challenge.capitalize())                 # Thirty days of python


# .count(): returns occurrences of substring in string, count(substring, start=.., end=..)
print(challenge.count('y'))                   # 3
print(challenge.count('y', 7, 14))            # 1
print(challenge.count('y', 7, 10))            # 1
# 2 (2 'y' between index 5 and 10)
print(challenge.count('y', 5, 10))
print(challenge.count('th'))                  # 2 (th in 'thirty' and 'python')
print(challenge.count('irty'))                # 1
print("Hello".count('e'))                     # 1
print("alifa ara heya ".strip().count("a"))   # 5
print("Alifa Ara Heya".count("a"))            # 3 (.count() is case sensitive.)


# .endswith(): Checks if a string ends with a specified ending.
print(challenge.endswith('on'))               # True
print(challenge.endswith('tion'))             # False
print("I love travelling.".endswith("ing"))   # False (it counts the fullstop.)
print("I love raining.".endswith("ing."))     # True


# .expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument.
challenge = "thirty\tdays\tof\tpython"
print(challenge)                              # thirty  days    of      python
print(challenge.expandtabs())                 # thirty  days    of      python
# thirty    days      of        python
print(challenge.expandtabs(10))


# .find(): Returns the lowest index of the first occurrence of a substring, if not found returns -1.
challenge = "thirty days of python"

# t  h  i  r  t  y     d  a  y  s     o  f    p  y  t  h  o  n
# 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20

print(challenge.find('y'))                    # 5
print(challenge.find("ty"))                   # 4
print(challenge.find('th'))                   # 0


# rfind(): Returns the highest index of the first occurrence of a substring, if not found returns -1.
challenge = "thirty days of python"
print(challenge.rfind('y'))                   # 16
print(challenge.rfind('th'))                  # 17


# .index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
challenge = "thirty days of python"
sub_string = "da"
print(challenge.index('y'))                    # 5 ( same as .find() )
print(challenge.index(sub_string))             # 7
print(challenge.index('y', 6))                 # 9 (didn't understand :( )
print(challenge.index('th'))                   # 0


# .rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
print(challenge.rindex('y'))                   # 16
print(challenge.rindex(sub_string))            # 7
print(challenge.rindex('y', 10))               # 16


# .isalnum(): Checks alphanumeric character
print(challenge.isalnum())                     # False
print("30daysofpython".isalnum())              # True
# False (space isn't alphanumeric)
print("thirty days of python 2019".isalnum())


# .isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
print(challenge.isalpha())                      # False
# True (Here I removed all spaces, so it's true.)
print(challenge.replace(" ", "").isalpha())
print("30daysofpython".isalpha())               # False
print("ThirtyDaysOfPython".isalpha())           # True


# .isdecimal(): Checks if all characters in a string are decimal (0-9)
print("123456".isdecimal())                     # True
print(challenge.isdecimal())                    # False
print("\u00B2".isdecimal())                     # False
print("1 2".isdecimal())                        # False


# .isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
print('123456'.isdigit())                       # True
print("Thirty".isdigit())                       # False
print('1 2 3 4'.isdigit())                      # False
print('\u00B2'.isdigit())                       # True ("\u00B2" is C/C++/Java source code)


# .isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
print('12345'.isnumeric())                      # True
print("1 2 3 4 5".isnumeric())                  # False
print('\u00B2'.isnumeric())                     # True
print('10.5'.isnumeric())                       # False


# .isidentifier(): Checks for a valid identifier - means it checks, if a string is a valid variable name
print(challenge.isidentifier())                 # False because "thirty days of python" is not a valid variable name.
print("30daysofpyhton".isidentifier())          # False because variable doesn't start with number.
print("thirty_days_of_python".isidentifier())   # true because underscore is accepted in naming variables.


# .islower(): Checks if all alphabet characters in the string are lowercase
print(challenge.islower())                      # true
print("Thirty days".islower())                  # False


# .isupper(): Checks if all alphabet characters in the string are uppercase
print(challenge.isupper())                      # False
challenge = challenge.upper()                
print(challenge)                                # THIRTY DAYS OF PYTHON
print(challenge.isupper())                      # True
print("Thirty days".isupper())                  # False


# .join(): Returns a concatenated string
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# ' .join(web_tech)
print(result)                                   # HTML# CSS# JavaScript# React

name = "Fatema"
nick_name = "Ruba"
full_name = name  .join(nick_name)
print(full_name)                                # RFatemauFatemabFatemaa (what is this?!!)


# .strip(): Removes all given characters starting from the beginning and end of the string
chal = "Thirty Days Of Pythonnnn"
print(chal.strip("n"))                          # Thirty Days Of Pytho ( by deafult .strip() removes space from the end and the start)
print(chal.strip("Thn"))                        # irty Days Of Pytho
print(chal.strip("y"))                          # Thirty Days Of Pythonnnn (can't remove middle characcters)


# .replace(): Replaces substring with a given string
challenge = "Thirty days of Python"
print(challenge.replace("Python", "Coding"))     # Thirty Days Of Coding


# .split(): Splits the string, using given string as a separator
challenge = "thirty days of python"
print(challenge.split())                         # ['thirty', 'days', 'of', 'python']
print(challenge.split(': '))                     # ['thirty days of python']
print(challenge.split('-'))                      # ['thirty days of python']


# .title(): Returns a title cased string
print(challenge.title())                         # Thirty Days Of Python


# .swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
print(challenge.swapcase())                      # THIRTY DAYS OF PYTHON
chal = 'tHirty dAys of pYthon'
print(chal.swapcase())                           # ThIRTY DaYS OF PyTHON


# .startswith(): Checks if String Starts with the Specified String
challenge = 'thirty days of python'
print(challenge.startswith('thirty'))            # True

chal = "30 days of python"
print(chal.startswith("thirty"))                 # False