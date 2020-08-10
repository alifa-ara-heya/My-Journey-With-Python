# Day_14: August/10/2020
# In the name 0f Allah..
# Me: Alifa
# From: Book : Python for everybody
# Chapter:4 (Functions)

# Exercise 1: Run the program on your system and see what numbers you get. Run the program more than once and see what numbers you get.
# The random function is only one of many functions that handle random numbers. The function randint takes the parameters low and high, and returns an integer between low and high (including both).

import random
print(random.randint(5, 10))

# To choose an element from a sequence at random, you can use choice:
t = [1, 2, 3]
print(random.choice(t))
print(random.choice(t))

