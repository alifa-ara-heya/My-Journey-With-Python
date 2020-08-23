# day 24
# 23- August- 2020
# sohoj vashay python

# problem: User will input a character and Python will tell him/her whether it's lower case or upper case.

alphabet = input("Please enter an alphabet , and I will tell you whether it's uppercased or lowercased: ")
if alphabet == alphabet.lower():
    print("Lower")
elif alphabet == alphabet.upper():
    print("Upper")
else:
    print("Nothing")


# author's way:
print('Please, input the character: ')
character = input()

if character >= 'a' and character <= 'z':
    print("Lower case")
elif character >= "A" and character <= 'Z':
    print("Upper case")
else:
    print("Nothing")