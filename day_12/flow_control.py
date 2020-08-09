# Day_12: August/08/2020
# In the name 0f Allah..
# Me: Alifa
# From: Book : Automate the boring stuff with Python;
# Chapter 2: Flow Control
# Topic: Conditionals (if statements)
# Example:
name = "Mary"
password = 'swordfish'
if name == "Mary":
    print("Hello, Mary")
    if password == "swordfish":
        print("Access granted")
    else:
        print("Wrong password")

# example:
name = "Alice"
if name == "Alice":
    print("Hello, Alice")


#3.
name = "Sienna"
if name == "Alice":
    print("hello, Alice")
else:
    print("hello, stranger")

# 4.
name = "Mita"
age = 6
if name == "Alice":
    print("Hi, Alice.")
elif age < 12:
    print('You are not Alice, kiddo.')    # You are not Alice, kiddo.
# The elif clause executes if age < 12 is True and name == 'Alice' is False.

# or,
name = "Alice"
age = 12
if name == "Alice":
    print("Hi, Alice.")                   # Hi, Alice.
elif age < 12:
    print('You are not Alice, kiddo.')    # This line isn't executed.

print()

# When there is a chain of elif statements, only one or none of the clauses will be executed.
# Once one of the statements’ conditions is found to be True, the rest of the elif clauses are automatically skipped.
name = "Carol"
age = 3000
if name == 'Alice':
    print("Hi, ALice.")
elif age < 12:
    print("You are not Alice, kiddo")
elif age > 2000:
    print("Unlike you, Alice is not an undead, immortal vampire.")   # Unlike you, Alice is not an undead, immortal vampire.
elif age > 100:
    print("You are not Alice, Granny.")

# if we write like this:
name = "Carol"
age = 3000
if name == 'Alice':
    print("Hi, ALice.")
elif age < 12:
    print("You are not Alice, kiddo")
elif age > 100:
    print("You are not Alice, Granny.")    # You are not Alice, Granny. (This is executed first, because it is first executed.)
elif age > 2000:
    print("Unlike you, Alice is not an undead, immortal vampire.")


# else statement: If the conditions in every if and elif statement are False, then the else clause is executed.
name = "Carol"
age = 3000
if name == 'Alice':
    print("Hi, ALice.")
elif age < 12:
    print("You are not Alice, kiddo")
else:
    print("You are neither Alice nor a little kid.")


# while loop  statements:
#if:
spam = 0
if spam < 5:
    print("Hello, World!")      # Hello, World!
    spam = spam + 1             # This isn't executed.


# while:
spam = 0
while spam < 5:
    print("Hello, World.")      # "Hello, World." is repeated five times here.
    spam = spam + 1             # This is executed.


# An Annoying while Loop:
# Your name:
name = ""
while name != 'Your name':
    print("Please type your name.")   # "Please type your name" (this outcome will be printed again and again)
    name = input()
print("Thank you.")                   # Type "Your name"  

# Your name2 with a break statement:
while True:
    print("Please type your name.")
    name = input()
    if name == "Your name":
        break
print("Thank you.")

# Creating a infinite while loop to stop the program by ctrl+C.
while True:
    print("Hello, world")

# example:
while True:
    print("Who are you?")
    name = input()
    if name != "Joe":
        continue
    print("Hello, Joe. What is the password? (It is a fish.)")
    password = input()
    if password == "swordfish":
        break
print("Access Granted.")