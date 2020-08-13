# Day_15: August/11/2020
# In the name 0f Allah..
# Me: Alifa
# From: Book : Python for everybody
# Chapter:5 (Iterations)

# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    string_num = input("Please, Enter a number: ")
    if string_num == "done":
        break
    try:
        int_num = int(string_num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = int_num
    elif int_num > largest:
        largest = int_num
    elif smallest is None:
        smallest = int_num
    elif int_num < smallest:
        smallest = int_num
print('Maximum is', largest )
print("Minimum is", smallest)