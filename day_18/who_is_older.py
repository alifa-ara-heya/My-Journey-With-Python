# Day_18: August/14/2020
# In the name 0f Allah..
# Me: Alifa
# From: 30 Days of Python by Asabeneh (Day: 9 {conditionals})
# exercises

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
print("Who is older me or you?")
my_age = 25
your_age = int(input("Enter your age: "))
if your_age > my_age:
    if (your_age - my_age) == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {your_age - my_age} years older than me.")
elif your_age < my_age:
    if (my_age - your_age) == 1:
        print("You are 1 year younger than me.")
    else:
        print(f"You are {my_age - your_age} years younger than me.")
elif your_age == my_age:
    print("We are of same age :D. Yeee!")