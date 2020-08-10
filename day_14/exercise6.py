# Day_14: August/10/2020
# In the name 0f Allah..
# Me: Alifa
# From: Book : Python for everybody
# Chapter:4 (Functions)

# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.
# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate). The output should be look like this:
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

hours = input("Enter hours please: ")
rate = input("Enter rate please: ")
float_hours = float(hours)
float_rate = float(rate)

def computepay(hours, rate):
    multiplied = hours * rate
    return multiplied

regular_pay = computepay(40, float_rate)
if float_hours > 40:
    extra_rate = (float_hours - 40) * (float_rate * 1.5)

overtime_pay = regular_pay + extra_rate
print("Pay: ", overtime_pay)



# instructor's hints:
def computepay2(h,r):
    return 42.37

hrs = input("Enter Hours:")
p = computepay2(10,20)
print("Pay",p)