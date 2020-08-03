#Day_7: August/03/2020
#In the name 0f Allah..
#Me: Alifa Ara Heya
#From: Asabeneh

#More String Formatting:
first_name = "Alifa"
last_name = "Ara Heya"
language = "Bengali"
formatted_string = "I am %s %s. I teach %s." %(first_name, last_name, language)
print(formatted_string)                         #I am Alifa Ara Heya. I teach Bengali.

#strings and numbers:
#old style formatting:
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string = "The area of the circle with a radius %s is %f." %(radius, area)     # %f is for floating point numbers.
print(formatted_string)                         # The area of the circle with a radius 10 is 314.000000.

formatted_string = "The area of the circle with a radius %s is %.2f." %(radius, area)   # %.f is floating point numbers with fixed precision.
print(formatted_string)                         # The area of the circle with a radius 10 is 314.00.

python_libraries = ['Django', 'Flask', 'Numpy', 'Pandas']
print(python_libraries)                         # ['Django', 'Flask', 'Numpy', 'Pandas']
formatted_string = "The following are python libraries: %s" %python_libraries
print(formatted_string)                         # The following are python libraries: ['Django', 'Flask', 'Numpy', 'Pandas']


#new style formatting:
formatted_string = "I am {} {}. I teach {}." .format(first_name, last_name, language)
print(formatted_string)                         # I am Alifa Ara Heya. I teach Bengali.
print("I am {} {}. I teach {}." .format(first_name, last_name, language))            # I am Alifa Ara Heya. I teach Bengali.
#or,
formatted_string = f"I am {first_name} {last_name}. I teach {language}."
print(formatted_string)                         # I am Alifa Ara Heya. I teach Bengali.

a = 5
b = 3
print('{} + {} = {}'.format(a, b, a + b))       # 5 + 3 = 8
print('{} - {} = {}'.format(a, b, a - b))       # 5 - 3 = 2
print('{} * {} = {}'.format(a, b, a * b))       # 5 * 3 = 15
print('{} / {} = {}'.format(a, b, a / b))       # 5 / 3 = 1.6666666666666667
print('{} / {} = {:.2f}'.format(a, b, a / b))   # 5 / 3 = 1.67 (2 digits after decimal)
print('{} / {} = {:.3f}'.format(a, b, a / b))   # 5 / 3 = 1.667  (3 digits after decimal)
print('{} // {} = {}'.format(a, b, a // b))     # 5 // 3 = 1 (floor division)
print('{} % {} = {}'.format(a, b, a % b))       # 5 % 3 = 2  (modulus)
print('{} ** {} = {}' .format(a, b, a ** b))    # 5 ** 3 = 125

# strings and numbers:
radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string = "The area of circle with a radius {} is {:.2f}." .format(radius, area)
print(formatted_string)                         #The area of circle with a radius 10 is 314.00.

# f-strings and interpolation:
print(f'{a} + {b} = {a + b}')                   # 5 + 3 = 8
print(f'{a} - {b} = {a - b}')                   # 5 - 3 = 2
print(f'{a} * {b} = {a * b}')                   # 5 * 3 = 15
print(f'{a} / {b} = {a / b}')                   # 5 / 3 = 1.6666666666666667
print(f'{a} / {b} = {a / b:.2f}')               # 5 / 3 = 1.67
print(f'{a} / {b} = {a / b :.3f}')              # 5 / 3 = 1.667
print(f'{a} // {b} = {a // b}')                 # 5 // 3 = 1
print(f'{a} % {b} = {a % b}')                   # 5 % 3 = 2
print(f'{a} ** {b} = {a ** b}')                 # 5 ** 3 = 125

#Unpacking characters:
language = "Python"
a = language
print(a)                                        # Python
a, b, c, d, e, f = language                
print(a)                                        # P
print(b)                                        # y
print(c)                                        # t
print(d)                                        # h
print(e)                                        # o
print(f)                                        # n

print()

#accessing characters in strings by index:
language = "Python"
           #012345
           #-6,-5,-4,-3,-2,-1
first_letter = language [0]
print(first_letter)                             # P

second_letter = language [1]
print(second_letter)                            # y

last_index = len(language) - 1                  # (The last leeter of a string is the length of a string minus one.)
last_letter = language[last_index]
print(last_letter)                              # n
#or,
last_letter = language [-1]                     # (negative index)
print(last_letter)                              # n

second_last = language [-2]
print(second_last)                              # o
print()

print(language [0])                             # P
print(language [1])                             # y
print(language [2])                             # t
print(language [3])                             # h
print(language [4])                             # o
print(language [5])                             # n
print('-----')
print(language [-1])                            # n
print(language [-2])                            # o
print(language [-3])                            # h
print(language [-4])                            # t
print(language [-5])                            # y
print(language [-6])                            # P
print(language [0 : 2])                         # Py  ( অর্থ এটার রেঞ্জ ইন্ডেক্স এর ০ থেকে ১ পর্যন্ত)
print(language [0 : 5])                         # Pytho (অর্থ এটার রেঞ্জ ইন্ডেক্স এর ০ থেকে ৪ পর্যন্ত)
print(language [0 : 6])                         # Python
print(language [3 : 6])                         # hon
print(language [5 : 6])                         # n
print(language [-2 : 6])                        # on
print(language [-5 : 3])                        # yt
print(language [0  : ])                         # Python  
print(language [   : 6])                        # Python
print(language [0 : -1])                        # Pytho
print(language [0 : -3])                        # Pyt 
print(language [-3 : ])                         # hon
print("----") 


#Slicing Python Strings.
language = "Python"
first_three = language [0 : 3]
print(first_three)                              # Pyt

last_three = language [3 : 6]
print(last_three)                               # hon
#or,
first_three = language [0 : -3]                 
print(first_three)                              # Pyt

last_three = language [-3 : ]
print(last_three)                               # hon


#Reversing a string:
greeting = "Hello, World!"
print(greeting [::-1])                          # !dlroW ,olleH
print(greeting [::-2])                          # !lo olH
print(greeting [::-3])                          # !r lH
print(greeting [::1])                           # Hello, World!


#Skipping characters while slicing:
lang = "Python"
pto = language [0 : 6 : 2]                      #[start : stop : step] it will start from 0, then stops at 5, but it will always be one step ahead, so 6, then 2 steps forward to slice 'o'.
print(pto)                                      # Pto
#or,
print(lang[0] + lang[2] + lang[4])              # Pto                               