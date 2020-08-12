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