# 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

hours = input("Enter hours please: ")
rate = input("Enter rate please: ")
float_hours = float(hours)
float_rate = float(rate)
regular_pay = 40 * float_rate
if float_hours > 40:
    extra_rate = (float_hours - 40) * float_rate * 1.5
overtime_pay = regular_pay + extra_rate
print("Pay: ", overtime_pay)