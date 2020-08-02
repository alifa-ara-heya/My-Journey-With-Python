#Day_2: July/30/2020
#In the name 0f Allah..
#Me: Alifa Ara Heya


#exercise_2: Hello "Your Name!"
Your_name = input("Please, enter your name: ").strip().title()
#or,
Your_name = Your_name.strip().title()
print("Hello,",Your_name,"!")                                         #Output: Hello, h !
#or,
print(f"Hello, {Your_name}!")                                         #Output: Hello, h! (better)

#A basic summation calculator:
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = float(num1) + float(num2)
print(result)