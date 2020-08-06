#Day_5: August/01/2020
#In the name 0f Allah..
#Me: Alifa Ara Heya
#Topic: A simple chat program.
#Book: Automate the boring staff by Python, Page: 21
#This program says hello and asks for my name and age.

print("Hello there!")
print("What is your name? ")
my_name = input().title().strip()
print("It is good to meet you,", my_name)
print("The length of your name is:", len(my_name))
print("What is your age? Please type your age in number.")
my_age = int(input())
print("You will be", int(my_age+1), "in a year." )