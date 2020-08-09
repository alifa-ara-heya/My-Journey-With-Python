# Day_12: August/08/2020
# In the name 0f Allah..
# Me: Alifa
# From: Book : Automate the boring stuff with Python;
# Chapter 2: Flow Control

# for Loops and the range() Function:
print('My name is:')
for i in range(5):
    print('Jimmy Five times (' + str(i) + ')')


# Adding all the numbers from 0 to 100:
total = 0
for num in range(101):
    total = total + num
print("The sum of 1 to 100 is:" ,total)

# An Equivalent while Loop:
print("My name is:")
i = 0
while i < 5:
    print('Jimmy Five Times (' + str(i) + ')')
    i = i + 1


# modules:
import random
for i in range(5):
    print(random.randint(1 , 10))


import random, sys, os, math

# or, another way of calling import modules:
from statistics import*