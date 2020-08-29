# Day_9: August/05/2020
# In the name 0f Allah..
# Me: Alifa Ara Heya
# From: Asabeneh (30 Days of Python: Day-5)

# Exercises-2:
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age:
ages.sort()
print(ages)                      # [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]

max_age = max(ages)
print(max_age)                   # 26

min_age = min(ages)
print(min_age)                   # 19

# Add the min age and the max age again to the list:
ages.insert(0, min_age)
last_index = len(ages)-1
ages.insert(last_index, max_age)
print(ages)                      # [19, 19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 26]
#                     index:        0    1   2   3   4   5   6   7   8   9  10   11
# Find the median age (one middle item or two middle items divided by two):
print("number of ages: ", len(ages)) # 12, which is an even number, so there are two middle values.
first_middle_index = int(len(ages)/2) - 1
print(first_middle_index)        # 5

first_middle_age = ages[first_middle_index]
print(first_middle_age)          # 24

second_middle_index = int(len(ages)/2)
print(second_middle_index)       # 6

second_middle_age = ages[second_middle_index]
print(second_middle_age)         # 24

median_age = (first_middle_age + second_middle_age)/2
print("Median age:", median_age) # 24.0
#or,
middle_ages = ages[5:7]
print(middle_ages)               # [24, 24]
median_age = sum(middle_ages)/2
print(median_age)                # 24.0
#or,
import statistics
median_age = statistics.median(ages)
print("Median age(statistics):", median_age) # 24.0


# Find the average age (sum of all items divided by their number)
sum1 = sum(ages)                 # 273
value = len(ages)               
average_age = sum1 / value
print(average_age)               # 22.75
#or,
average_age_mean = statistics.mean(ages)
print("Mean or average age:", average_age_mean) # 22.75


# Find the range of the ages (max minus min):
print(max_age - min_age)         # 7

# Compare the value of (min - average) and (max - average), use abs() method
# example:
print(abs(-2.7))                 # 2.7
# solution:
min_minus_average = min_age - average_age
max_minus_average = max_age - average_age
print(min_minus_average)                           # -3.75
print(max_minus_average)                           #  3.25
print(min_minus_average - max_minus_average)       # -7.0
print(abs(min_minus_average - max_minus_average))  #  7.0

import statistics
some_list = [1, 2, 3, 4, 5]
middle_num = statistics.median(some_list)                
print(middle_num)                                  #  3

some_list2 = [1, 2, 3, 4, 5, 6]
middle_num2 = statistics.median(some_list2)
print(middle_num2)                                 #  3.5

some_list3 = ['a', 'b', 'c', 'd', 'e']
print(statistics.median(some_list3))               # c

some_list4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(statistics.median(some_list4))               # d (median can't find the middle item of a list if it contains even number items and if the items are strings.)  