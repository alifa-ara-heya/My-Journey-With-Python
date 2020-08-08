# Day_12: August/08/2020
# In the name 0f Allah..
# Me: Alifa Ara Heya
# From: Book : Python Crash Course
# Chapter 4: Working with lists 
# Topic: Tuples

# Python refers to values that cannot change as immutable , and an immutable list is called a tuple.
# For example, if we have a rectangle that should always be a certain size, we can ensure that its size doesn’t change by putting the dimensions into a tuple:
dimensions = (200, 15)
print(dimensions[0])       # 200
print(dimensions[1])       # 15
print(type(dimensions))    # <class 'tuple'>
print(dimensions)          # (200, 15)

# Looping Through All Values in a Tuple:
for dimension in dimensions:
    print(dimension)       # same as lists.


# Writing over a Tuple
#Although you can’t modify a tuple, you can assign a new value to a variable that holds a tuple. 
dimensions = (200, 15)
print(f"Original dimensions are:")
for dimension in dimensions:
    print(dimension)       # Original dimensions are : 200  15 
dimensions = (400, 20)
print(f"\nModified dimensions are:")
for dimension in dimensions:
    print(dimension)       # Modified dimensions are : 400  20


# Exercises: 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
# • Use a for loop to print each food the restaurant offers.

buffet = ("Salad", "Fried Rice", "Beef steak", "Tuna fish")
for food in buffet:
    print(food)

# • Try to modify one of the items, and make sure that Python rejects the change.
#buffet[0] = "Chicken"     # disabled it because it gets traceback.
print(buffet)              #  ('Salad', 'Fried Rice', 'Beef steak', 'Tuna fish')

# • The restaurant changes its menu, replacing two of the items with different foods. 
# Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.
buffet = ("Mutton", "Ice-cream", "Cake", "Pasta")
print(f"Revised foods are:")
for food in buffet:
    print(food)