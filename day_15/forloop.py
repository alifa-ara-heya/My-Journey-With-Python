# Day_15: August/10/2020
# In the name 0f Allah..
# Me: Alifa
# From: Book : Python for everybody
# Chapter:5 (Iterations)

friends = ['joseph', 'glenn', 'sally']
for friend in friends:
    print("Happy new year:", friend.title())
print("Done!")

# Counting and summing loops:
# to count the number of items in a list,
count = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print("Count:", count)

# Another similar loop that computes the total of a set of numbers is as follows:
total = 0
for itervar in [3, 41, 12, 9, 74, 15]:
    total = total + itervar
print("total:", total)

# Maximum and minimum loops:
# To find the largest value in a list or sequence, we construct the following loop:
largest = None
print("Before:", largest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest:
        largest = itervar
    print("Loop:", itervar, largest)
    print("Largest:", largest)