# Day_17: August/13/2020
# In the name 0f Allah..
# Me: Alifa
# From: 30 Days of Python by Asabeneh (Day: 6)

# A tuple is a collection of different data types which is ordered and unchangeable (immutable). We cannot use add, insert, remove methods in a tuple because it is not modifiable (mutable). 

# Empty tuple: Creating an empty tuple
empty_tuple = ()
#or,
empty_tuple = tuple()

# Tuple with initial values:
tpl = ('item1', 'item2', 'item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

print(len(tpl))         # 3

# Accessing Tuple Items:
# Positive Indexing Similar to the list data type we use positive or negative indexing to access tuple items.

first_item = tpl[0]
print(first_item)       # item1

second_item = tpl[1]
print(second_item)      # item2

first_fruit = fruits[0]
last_fruit = fruits[-1]
print(first_fruit)      # banana
print(last_fruit)       # lemon

last_index_fruits = len(fruits) - 1
last_fruit = fruits[last_index_fruits]
print(last_fruit)       # lemon


# Slicing tuples:
# Range of Positive Indexes
tpl =  ('item1', 'item2', 'item3', 'item4')
all_items = tpl[0 : 4]
print(all_items)
all_items =  tpl[0:]
print(all_items)
middle_two_items = tpl[1 : 3]
print(middle_two_items)         # ('item2', 'item3')

# Range of Negative Indexes
tpl =  ('item1', 'item2', 'item3', 'item4')
all_items = tpl[-4:]
print(all_items)
middle_two_items = tpl[-3 : -1]
print(middle_two_items)         #  ('item2', 'item3')


fruits = ('banana', 'orange', 'mango', 'lemon')
all_fruits = fruits[-4:]
print(all_fruits)               # ('banana', 'orange', 'mango', 'lemon')

orange_mango = fruits[-3 : -1]
print(orange_mango)             # ('orange', 'mango')

orange_to_the_rest = fruits[-3 : ]
print(orange_to_the_rest)       # ('orange', 'mango', 'lemon')

# Changing Tuples to list:
#  Tuple is immutable if we want to modify a tuple we should change it to a list.
tpl =  ('item1', 'item2', 'item3', 'item4')
tpl = list(tpl)
print(tpl)                 # ['item1', 'item2', 'item3', 'item4']

fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
print(fruits)              # ['banana', 'orange', 'mango', 'lemon']

#modifying the list of fruits:
fruits[0] = 'kiwi'
print(fruits)              # ['kiwi', 'orange', 'mango', 'lemon']

fruits = tuple(fruits)
print(fruits)              # ('kiwi', 'orange', 'mango', 'lemon')


# Checking am item in a tuple:
tpl =  ('item1', 'item2', 'item3', 'item4')
print("item1" in tpl)      # True
print("item5" in tpl)      # False

fruits = ('banana', 'orange', 'mango', 'lemon')
print('banana' in fruits)  # True
print('apple' in fruits)   # False
#fruits[0] = 'apple'        # if we print this we will get traceback.


# Joining tuples:
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables) # ('banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')

# Deleting tuples: It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
del vegetables
# print(vegetables)  # traceback