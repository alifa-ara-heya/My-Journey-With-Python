# Day_19: August/15/2020
# In the name 0f Allah..
# Me: Alifa
# From: 30 Days of Python by teclado (Day: 5 {conditions})

# Exercises from Teclado Blog (30 Days of python)

name = input("Please enter your name: ")

if name:             # Checks the truth value of name by calling bool.
    print(f"You entered {name.title()}.")
else:
    print("You didn't type anything.")

# Exercises:
# 1) Try to approximate the behaviour of the is operator using ==. Remember we have the id function for finding the memory address for a given value, and we can compare memory addresses to check for identity.


# 2) Try to use the is operator or the id function to investigate the difference between these:
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
print(numbers == new_numbers)       # False
print(numbers is new_numbers)       # False
print(new_numbers)                  # [1, 2, 3, 4, 5]
print(numbers)                      # [1, 2, 3, 4]
print(id(numbers))                  # 59153672
print(id(new_numbers))              # 59232584
#and this:
numbers = [1, 2, 3, 4]
numbers.append(5)
print(numbers)
# Are new_numbers and numbers the same thing? What about numbers before and after we append 5?
print(id(numbers))                 # 24039880

# There are some more exercises. But I am lazy today! :(