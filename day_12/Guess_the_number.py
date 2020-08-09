# Day_12: August/08/2020
# In the name 0f Allah..
# Me: Alifa
# From: Book : Automate the boring stuff with Python;
# Chapter 2: Flow Control

# Guess the number:

import random

secretNumber = random.randint(1, 20)
print("I am thinking of a number between 1 to 20.")


# Ask the player to guess 6 times:
for guessesTaken in range(1, 7):
    print("Take a guess. Enter what you think. I will give you six chances to guess it.")
    guess = int(input())

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break      # This condition is the correct guess.

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print("Nope. The number I was thinking of was " + str(secretNumber))