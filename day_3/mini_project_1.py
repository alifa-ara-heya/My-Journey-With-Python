#Day_2: July/30/2020
#In the name 0f Allah..
#Me: Alifa Ara Heya

#Project: A simple earning calculator:

name = input("Enter your name: ").title().strip()
hourly_wage = input("Hourly wage: ")
hours_worked = input("Hours you worked this week: ")

total_earned = float(hourly_wage) * float(hours_worked)

print(f"{name} earned {total_earned}$ this week.")