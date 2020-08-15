# Day_18: August/14/2020
# In the name 0f Allah..
# Me: Alifa
# From: 30 Days of Python by Asabeneh (Day: 9 {conditionals})
# exercises


# 4. Write a code which gives grade to students according to their scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F

num = float(input("Enter number between 1 to 100: "))

if num >= 80:
    print("Congratulations! Your grade is 'A'.")
elif num >= 70:
    print("Congrates! Your grade is 'B'.")
elif num >= 60:
    print("Your grade is 'C'. Hope you will do better next time.")
elif num >= 50:
    print("Your grade is 'D'. Hope you will do better next time.")
elif num < 50:
    print("Sorry you failed. Your grade is 'F'.")
