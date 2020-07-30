#Day_2: July/29/2020
#In the name 0f Allah..
#Me: Alifa Ara Heya

#practising input function:
input("please enter your name: ")                          #sample input
name = input("please enter your name: ")                   #assigning variables
age = input("please enter your age: ")
print(name)
print(age)


#problem
hourly_wage = input("Please enter your hourly wage: ")
print("Hourly wage: "+ hourly_wage)                         #Here we can use plus to concatenate because every input is considered as string. And two strings can be concatenated.

hours_worked = input("How many hours did you work this week? ")
print("Hours worked: "+ hours_worked)

print(int(hourly_wage) * int(hours_worked))                #Here we have converted the strings to integer.