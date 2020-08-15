# Day_18: August/14/2020
# In the name 0f Allah..
# Me: Alifa
# From: 30 Days of Python by Asabeneh (Day: 9 {conditionals})
# exercises

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
a = float(input("Enter number one: "))
b = float(input("Enter number two: "))
if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{b} is greater than {a}.")
else:
    print(f"{a} is equal to {b}.")