# Day_11: August/07/2020
# In the name 0f Allah..
# Me: Alifa Ara Heya
# From: Book : Python Crash Course
# Chapter 4: Working with lists

# Looping Through an Entire List:

foods = ["fruits", 'vegetables', 'meat', 'salad', 'fish', 'chips']
for food in foods:
    print(food)

foods = ["fruits", 'vegetables', 'meat', 'salad', 'fish', 'chips']
for food in foods:
    print("I love " + food + ".\n")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("We are looking forward for you next trick, " + magician.title() + ".\n")  # see what happens without the indentation.
print("Thank you everyone.")


# Using the range() function:
for value in range(1,5):
    print(value)                 # 1   2   3   4 (new line for every number)

for value in range(100, 111):
    print(value)

numbers = list(range(1,10))
print(numbers)                   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# printing a list of even numbers from 1 to 10:
even_numbers = list(range(2, 11, 2))
print(even_numbers)              # [2, 4, 6, 8, 10]


# printing a list of odd numbers from 1 to 20:
odd_numbers = list(range(1, 21, 2))
print(odd_numbers)               # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
 

# make a list of the first 10 square numbers (that is, the square of each integer from 1 through 10).
squares = []
for value in range(1 , 11):
    square = value ** 2
    squares.append(square)
print(squares)                   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# To write this code more concisely, omit the temporary variable square and append each new value directly to the list:
squares = []
for value in range(1 , 11):
    squares.append(value ** 2)
print(squares)                   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# or, making the same list using list comprehension:
squares = [value ** 2 for value in range(1,11)]
print(squares)                   # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 
print(value)                     # 10

# Simple Statistics with a List of Numbers:
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))               # 0
print(max(digits))               # 9
print(sum(digits))               # 45

# Automate the boring staff with Python, example:
for i in range(5, -1, -1):
    print(i)                     # 5 4 3 2 1 0