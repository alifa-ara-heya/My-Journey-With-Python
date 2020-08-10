# Day_14: August/10/2020
# In the name 0f Allah..
# Me: Alifa
# From: Book : Python for everybody
# Chapter:4 (Functions)


# Built-in functions:
max1 = max("hello world")
print("Maximum:", max1)       # Maximum: w ( “largest character”)

min1 = min("hello world")
print("Minimum:", min1)       # Minimum:"" (smallest character :"space")

import math
print(math)                   # <module 'math' (built-in)>

#1st example: The first example computes the logarithm base 10 of the signal-to-noise ratio.
#signal_power = 
#noise_power = 
#ratio = signal_power / noise_power
#decibels = 10 * math.log10(ratio)

#2nd example: The second example finds the sine of radians.
degrees = 45
radians =  degrees / 360.0 * 2 * math.pi
print(math.sin(radians))      # 0.7071067811865475

print(math.sqrt(2) / 2.0)     # 0.7071067811865476

# random>
import random

for i in range(10):
    x = random.random()
    print(x)


# Adding new functions:
def print_lyrics():           # print_lyrics() is the built-in function here.
    print("I'm a lumberjack, and I am okay.")
    print("I sleep all night and I work all day.")


print(print_lyrics)           # <function print_lyrics at 0x0355D268>
print(type(print_lyrics))     # <class 'function'>

print_lyrics()                # This will show the value of the function.

# using the function inside another function:
def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()


# Parameters and arguments:
def print_twice(bruce):
    print(bruce)
    print(bruce)

print_twice(17)      # When the function is called, it prints the value of the parameter (whatever it is) twice.
print_twice("spam")  # spam spam


import math
print_twice(math.pi) # 3.141592653589793
                     # 3.141592653589793

print_twice('spam' * 4)  # spamspamspamspam
                         # spamspamspamspam

print_twice('dim '* 4)   # dim dim dim dim
                         # dim dim dim dim

print_twice(math.cos(math.pi)) # -1.0  -1.0

ex = "Hi, there."
print_twice(ex)          # Hi, there. Hi, there.


# Fruitful functions and void functions:
x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2

#result = print_twice("bing")  # bing bing      # disabled
#print(result)                 # none           # disabled

print(type(None))             # <class 'NoneType'>


#  a very simple function called addtwo that adds two numbers together and returns a result.

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)               # 8




 