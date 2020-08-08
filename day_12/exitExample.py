# Day_32: August/09/2020
# In the name 0f Allah..
# Me: Alifa
# From: Book : Automate the boring stuff with Python;
# Chapter 2: Flow Control
# Ending a Program Early with the sys.exit() Function.

import sys
# you can cause the program to terminate, or exit, before the last instruction by calling the sys.exit() function. 
while True:
    print("Type exit to exit.")
    response = input()
    if response == "exit":
        sys.exit()
    print("You typed " + response + '.')

# This program has an infinite loop with no break statement inside. 
# The only way this program will end is if the execution reaches the sys.exit() call. When response is equal to exit, the line containing the sys.exit() call is executed. 
# Since the response variable is set by the input() function, the user must enter exit in order to stop the program.