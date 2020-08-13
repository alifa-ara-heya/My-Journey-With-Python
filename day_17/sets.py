# Day_17: August/13/2020
# In the name 0f Allah..
# Me: Alifa
# From: 30 Days of Python by Asabeneh (Day: 7)

# Set is a collection of unordered and unindexed distinct elements. In python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.
# Creating a Set:
# Creating an empty set:
st = {}
#or,
st = set()

# Creating a set with initial items:
st = {'item1', 'item2', 'item3', 'item4'}
fruits = {'banana', 'apple', 'orange', 'lichi'}


# Getting Set's Length:
print(len(fruits))           # 4

# Accessing Items in a Set: We use loops to access items. We will see this in loop section. (inshaAllah)

# Checking an Item:
st = {'item1', 'item2', 'item3', 'item4'}
print('item2' in st)         # True

# Adding Items to a Set:
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
print(st)                    # {'item3', 'item5', 'item1', 'item4', 'item2'}

# Add multiple items using update()
vegetables = {'Tomato', 'Potato', 'Cabbage'}
vegetables.update(['Onion','Capsicum']) # third brackets must be used.
print(vegetables)            # {'Tomato', 'Cabbage', 'Capsicum', 'Potato', 'Onion'}
fruits =  {'banana', 'apple', 'orange', 'lichi'}
fruits.update(vegetables)
print(fruits)                # {'banana', 'Tomato', 'apple', 'Cabbage', 'Capsicum', 'Potato', 'Onion', 'lichi', 'orange'}

# Removing Items from a Set:
# We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
print(st)                   # {'item3', 'item4', 'item1'}

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()                # removes the last element from the set
print(fruits)               # {'mango', 'banana', 'orange'}


# Clearing Items in a Set:
fruits.clear()
print(fruits)               # set()

# Deleting a Set.
st = {'item1', 'item2', 'item3', 'item4'}
del st

# Converting List to Set:
