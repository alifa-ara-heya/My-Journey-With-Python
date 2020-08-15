# Day_18: August/14/2020
# In the name 0f Allah..
# Me: Alifa
# From: 30 Days of Python by Asabeneh (Day: 9 {conditionals})
# exercises

# 5. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer.

print("Which season is this month?")
month = input("Please enter a month name: ").title()
if month == "September" or month == "October" or month == "November":
    print("The season is Autumn. Enjoy the new glowing leaves!")
if month == "December" or month == "January" or month == "February":
    print("This is Winter. Do you like falling snows? Enjoy!")
if month == "June" or month == "July" or month == "August":
    print("This is summer. Enjoy mango fruits.")