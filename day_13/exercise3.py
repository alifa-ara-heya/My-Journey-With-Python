# Day_13: August/09/2020
# In the name 0f Allah..
# Me: Alifa
# From: Book : Python for everybody
# chapter: 3
# Conditional operator: Exercises

# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score   Grade
# >= 0.9     A
# >= 0.8     B
# >= 0.7     C
# >= 0.6     D
# < 0.6      F

inp_score = input("Enter score between 0.0 to 1.0: ")
try:
    score = float(inp_score)
except:
    print("Bad score. Please enter score between the range.")
    quit()
if score >= 0.9:
        print("A")
elif score >= 0.8:
        print("B")
elif score >= 0.7:
        print("C")
elif score >= 0.6:
        print("D")
elif score < 0.6:
        print("F")