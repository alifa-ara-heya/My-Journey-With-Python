# Day_9: August/05/2020
# In the name 0f Allah..
# Me: Alifa Ara Heya
# From: Asabeneh (30 Days of Python: Day-5)

# Modifying lists:
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = "avocado"
print(fruits)               # ['avocado', 'orange', 'mango', 'lemon']

fruits[2] = "jackfruit"
print(fruits)               # ['avocado', 'orange', 'jackfruit', 'lemon']

last_index = len(fruits)-1
fruits[last_index] = 'lime'
print(fruits)               # ['avocado', 'orange', 'jackfruit', 'lime']


# Checking items in a list:
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)           # True

does_exist = 'jackfruit' in fruits
print(does_exist)           # False


# Adding items to a list, syntax: list.append("item")
# To add item to the end of an existing list we use the .append() method:
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('lichi')
print(fruits)               # ['banana', 'orange', 'mango', 'lemon', 'lichi']

fruits.append('lime')
print(fruits)               # ['banana', 'orange', 'mango', 'lemon', 'lichi', 'lime']


# Inserting items into a list, syntax: list.insert(index, 'item')
# Use insert() method to insert a single item at a specified index in a list. Note that other items are shifted to the right.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(1, 'watermelon')
print(fruits)               # ['banana', 'watermelon', 'orange', 'mango', 'lemon']

fruits.insert(2, 'guava')
print(fruits)               # ['banana', 'watermelon', 'guava', 'orange', 'mango', 'lemon']


# Removing items from a list: 
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('orange')
print(fruits)               # ['banana', 'mango', 'lemon', 'banana']

fruits.remove('banana')     # this method removes the first occurrence of the item in the list
print(fruits)               # ['mango', 'lemon', 'banana']


# Removing items using Pop- The pop() method removes the specified index, (or the last item if index is not specified):
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.pop()
print(fruits)               # ['banana', 'orange', 'mango', 'lemon'] (remoed the last item)
fruits.pop(2)
print(fruits)               # ['banana', 'orange', 'lemon']


# Removing items using del:
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
del fruits[0]
print(fruits)               # ['orange', 'mango', 'lemon', 'banana'] (removed the first item)

pets = ["cat", 'rabbit', 'dog', 'eagle', 'dolphin']
del pets[2]
print(pets)                 # ['cat', 'rabbit', 'eagle', 'dolphin']

del pets [1 : 3]
print(pets)                 # ['cat', 'dolphin']


# Clearing list items:  The .clear() method empties the list.
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.clear()
print(fruits)               # []


# Copying a list:
pets = ['cat', 'rabbit', 'eagle', 'dolphin']
# one way:
list1 = pets                # declared a variable
print(list1)                # ['cat', 'rabbit', 'eagle', 'dolphin']
list2 = list1
print(list2)                # ['cat', 'rabbit', 'eagle', 'dolphin'] (copied the list)

#another way by copy() method:
copy_pets = pets.copy()
print(copy_pets)            # ['cat', 'rabbit', 'eagle', 'dolphin']


# Joining Lists:
# way-1: Plus operator; syntax: list3 = list2 + list1
# example-1:
vegetables = ['onion', 'Tomato', 'carrot', 'brocoli']
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_vegetables = vegetables + fruits
print(fruits_vegetables)    # ['onion', 'Tomato', 'carrot', 'brocoli', 'banana', 'orange', 'mango', 'lemon']


# example-2:
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)             # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# way-2: extend() method:
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['onion', 'Tomato', 'carrot', 'brocoli']
fruits.extend(vegetables)
print("Fruits and vegetables:", fruits)               # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'onion', 'Tomato', 'carrot', 'brocoli']


# Counting items in a list: The count() method returns the number of times an item appears in a list:
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.count('banana')
print(fruits.count('banana'))                         # 2

num = [3, 2, 3, 6, 3, 10, 11, 3]
print(num.count(3))                                   # 4


# Finding index of an item: The index() method returns the index of an item in the list:
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
print(fruits.index("orange"))                         # 1
print(fruits.index('banana'))                         # 0, returns the first occurrence
print(num.index(10))                                  # 5


# Reversing a list:
pets = ['cat', 'rabbit', 'eagle', 'dolphin']
#pets.reverse()
print(pets)                                           # ['dolphin', 'eagle', 'rabbit', 'cat']

num = [1, 2, 3, 4, 5]
num.reverse()
print(num)                                            # [5, 4, 3, 2, 1]


# Sorting list items: permanent sorting-
vegetables = ['onion', 'Tomato', 'carrot', 'brocoli']
vegetables.sort()
print(vegetables)                                     # ['Tomato', 'brocoli', 'carrot', 'onion'] (sorted in ascending order, capital letter comes first)

vegetables = ['onion', 'tomato', 'carrot', 'brocoli']
vegetables.sort()
print(vegetables)                                     # ['brocoli', 'carrot', 'onion', 'tomato'] (a to z)

vegetables = ['onion', 'tomato', 'carrot', 'brocoli']
vegetables.sort(reverse = True)
print(vegetables)                                     # ['tomato', 'onion', 'carrot', 'brocoli'] (z to a)

ages = [50, 20, 30, 10, 60]
ages.sort()
print(ages)                                           # [10, 20, 30, 50, 60] (smallest to largest)

ages = [50, 20, 30, 10, 60]
ages.sort(reverse = True)
print(ages)                                           # [60, 50, 30, 20, 10] (largest to smallest)


#another way to sort: a temporary way.
# To maintain the original order of a list but present it in a sorted order, you can use the sorted() function. 
# The sorted() function lets you display your list in a particular order but doesn’t affect the actual order of the list.
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))                                 # ['banana', 'lemon', 'mango', 'orange'] ( a to z)

fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits, reverse = True))                 # ['orange', 'mango', 'lemon', 'banana'] (z to a)

print(fruits)                                         # unchanged

cars = ["bmw", "audi", "toyota", "subaru"]
print("Here is the original list: ", cars)            # Here is the original list:  ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the sorted list:" , sorted(cars))      # Here is the sorted list: ['audi', 'bmw', 'subaru', 'toyota']
print("Here is the original list again: ", cars)      # Here is the original list again:  ['bmw', 'audi', 'toyota', 'subaru']

cars = ["bmw", "audi", "toyota", "subaru"]
cars.reverse()
print(cars)                                           # ['subaru', 'toyota', 'audi', 'bmw']
cars.sort(reverse = True)
print(cars)
# Note: sort(reveres = True) or sorted(reverse = True) make the list reverse alphabetically (from z to a)
# But, .reverse() just reverses the list (from backword to forward)
# Note: Use .sorted() if you want to sort the list temporarily.
# Notes collected from the book "Python Crash Course".