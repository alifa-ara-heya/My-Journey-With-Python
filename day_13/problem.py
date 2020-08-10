# Exercise of chapter 3:
# 1. Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
hours = input("Enter hours again please: ")
rate = input("Enter rate again please: ")
float_hours = float(hours)
float_rate = float(rate)
if float_hours > 40:
    regular_pay = float_hours * float_rate
    overtime_pay = (float_hours - 40) * (float_rate * 1.5)
    total_pay = regular_pay + overtime_pay
else:
    total_pay = float_hours * float_rate
print("Pay:", total_pay)