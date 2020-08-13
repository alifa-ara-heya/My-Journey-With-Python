# Day_17: August/13/2020
# In the name 0f Allah..
# Me: Alifa
# From: 30 Days of Python by Asabeneh (Day: 6)

# 1. Create an empty tuple.
empty_tuple = ()
# or,
empty_tuple = tuple()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Musa', 'Sakib', 'Asif', 'Ridwan')
sisters = ('Fatema', 'Sushoma', 'Mohima')

# 3. Join brothers and sisters tuples and assign it to siblings.
siblings = brothers + sisters
print(siblings)            # ('Musa', 'Sakib', 'Asif', 'Ridwan', 'Fatema', 'Sushoma', 'Mohima')

# 4. How many siblings do you have?
print(len(siblings))       # 7

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to siblings.
siblings = list(siblings)
print(siblings)            # ['Musa', 'Sakib', 'Asif', 'Ridwan', 'Fatema', 'Sushoma', 'Mohima']
siblings.insert(0,"Mohammad Abdullah")
siblings.insert(1, "Amatullah")
family_members = siblings
print(family_members)

# 6. Unpack siblings and parents from family_members.
family_members = ['Mohammad Abdullah', 'Amatullah', 'Musa', 'Sakib', 'Asif', 'Ridwan', 'Fatema', 'Sushoma', 'Mohima']
father, mother, *siblings = family_members
print(father)             # Mohammad Abdullah
print(mother)             # Amatullah
print(siblings)           # ['Musa', 'Sakib', 'Asif', 'Ridwan', 'Fatema', 'Sushoma', 'Mohima']
family_members = tuple(family_members)
print(family_members)


# 7. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('milk', 'cheese', 'butter')
food_stuff = fruits + vegetables + animal_products
print(food_stuff)

# 8. Slice out the middle item or items from the food_staff list.
middle_index = int(len(food_stuff) / 2)
print(food_stuff[middle_index])       # cabbage

# 9. Slice out the first three items and the last three items from food_staff list.
first_three = food_stuff[0 : 3]
print(first_three)                    # ('banana', 'orange', 'mango')

last_three = food_stuff[-3: ]
print(last_three)                     # ('milk', 'cheese', 'butter')

# 10. Delete the food_staff list completely
del food_stuff

# 11. Check if an item exist in a tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
print("Estonia" in nordic_countries)   # false

# Check if 'Iceland' is a nordic country.
print("Iceland" in nordic_countries)   # true
print("iceland" in nordic_countries)   # False (case sensitive)