# Day_13: August/09/2020
# In the name 0f Allah..
# Me: Alifa
# From: Book : Python for everybody
# chapter: 3
# Conditional operator: Exercises

# Exercise of chapter 2:
# Exercise 3: Write a program to prompt the user for hours and rate per hour to compute gross pay.
hours = input("Enter hours: ")
rate = input("Enter rate: ")
pay = float(hours) * float(rate)
print(pay)


# Exercise of chapter 3:
# 1. Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hours = input("Enter hours again please: ")
rate = input("Enter rate again please: ")
float_hours = float(hours)
float_rate = float(rate)
if float_hours > 40:
    regular_pay = float_hours * float_rate
    overtime_pay = (float_hours - 40) * (float_rate * 0.5)
    total_pay = regular_pay + overtime_pay
else:
    total_pay = float_hours * float_rate
print("Pay:", total_pay)


# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
# my way:
try:
    hours = input("Enter hours again please: ")
    rate = input("Enter rate again please: ")
    float_hours = float(hours)
    float_rate = float(rate)
    if float_hours > 40:
        regular_pay = float_hours * float_rate
        overtime_pay = (float_hours - 40) * (float_rate * 0.5)
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = float_hours * float_rate
    print("Pay:", total_pay)
except:
    print("Error, please enter numeric input. ")

# Author's way:
sh = input("Enter hours again please: ")
sr = input("Enter rate again please: ")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input.")
    quit()

print(fh, fr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay:", xp)


# my way again: (understood)
hours = input("Enter hours please: ")
rate = input("Enter rate please: ")
float_hours = float(hours)
float_rate = float(rate)
regular_pay = 40 * float_rate
if float_hours > 40:
    extra_rate = (float_hours - 40) * float_rate * 1.5
overtime_pay = regular_pay + extra_rate
print("Pay: ", overtime_pay)

# chapter - 4:
# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).