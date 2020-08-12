# Day_15: August/11/2020
# In the name 0f Allah..
# Me: Alifa
# From: Book : Python for everybody
# Chapter:5 (Iterations)

# Exercise 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number. Enter 7, 2, bob, 10, and 4 and match the output below.

while True:
    line = int(input("> "))
    if line == "done":
        break
    total = 0
    for value in (line):
        total = total + value
    print("total:", total)
    
while True:
    line = input("> ")
    if line == "done":
        break
    count = 0
    for value in line:
        count = count + 1
    print("Count:", count)



