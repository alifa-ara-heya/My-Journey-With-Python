# Day_16: August/12/2020
# In the name 0f Allah..
# Me: Alifa
# Book : Python Crash Course
# chapter - 5 (If statements)

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


# conditional test:
car = 'bmw'
car == "bmw"
print(car == "bmw")            # True
print(car == "audi")           # False

# Ignoring Case When Checking for Equality:
car = "Audi"
print(car == 'audi')           # False

# if case doesn't matter:
car = 'Audi'
print(car.lower() == 'audi')   # True

# The lower() function doesn’t change the value that was originally stored in car , so you can do this kind of comparison without affecting the original variable:

car = "Audi"
print(car.lower() == 'audi')   # True
print(car)                     # Audi

# Checking for Inequality:
requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")

answer = 17
if answer != 17:
    print("Please try again. That is not the correct answer.")


# Using and to Check Multiple Conditions:
# you can check whether two people are both over 21 using the following test:

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)      # False

age_1 = 23
print(age_0 >= 21 and age_1 >= 21)      # True
#or,
print((age_0 >= 21) and (age_1 >= 21))  # True

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print("mushrooms" in requested_toppings) # True
print("mushroom" in requested_toppings)  # False
print("pepperoni" in requested_toppings) # False


# Checking Whether a Value Is Not in a List:
banned_users = ['andrew', 'caroline', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + " ,you can post a response if you wish.")

game_active = True   # checking whether a game is running.
can_edit = False     # checking if a user can edit certain contents on a website.

age = 17
if age >= 18:
    print("You are old enough to vote.")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18.")


# The if-elif-else Chain:
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
#or,
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Yor admission cost is $" + str(price) + ".")


# Using Multiple elif Blocks:
age = 100
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Yor admission cost is $" + str(price) + ".")


# Omitting the else Block:
age = 3
if age < 4:
    price = 0   # Just this code has been executed in this block.
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Yor admission cost is $" + str(price) + ".")
# If you have a specific final condition you are testing for, consider using a final elif block and omit the else block. As a result, you’ll gain extra confidence that your code will run only under the correct conditions.

# Testing multiple conditions:
requested_toppings = ['mushrooms', 'onions', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print('\nFinished making your pizza!')
#Each code is executed here.

# In summary, if you want only one block of code to run, use an if-elif-else chain. If more than one block of code needs to run, use a series of independent if statements.

# Using if Statements with Lists:
# toppings.py
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
print()   # For a blank line in the terminal.
# But what if the pizzeria runs out of green peppers? An if statement inside the for loop can handle this situation appropriately:
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green pepper now.')
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")


# Checking That a List Is Not Empty:
requested_toppings = []
if requested_toppings:    # As it has no item in it, it is false. So the for loop isn't executed.
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print('Finished making your pizza.')
else:
    print('Are you sure you want a plain pizza?')

print()
# Using multiple lists:
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("Finished making your pizza.")