# Day_18: August/14/2020
# In the name 0f Allah..
# Me: Alifa
# From: 30 Days of Python by Asabeneh (Day: 8 {Dictionaries})

# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

empty_dict = {}
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
person = {
    'first name' : 'Asiya',
    'last name' : 'Amatullah',
    'age' : 20,
    'country' : 'Egypt',
    'religion' : 'Muslimah',
    'skills' : ['Javascript', 'Python', 'Node', 'React'],
    'fav colors' : {'red', 'orange', 'purple'},
    'address' : {
        'street' : 'Space street',
        'zipcode' : '02215'
    }
}
# The dictionary above shows that a value could be any different data type:string, boolean, list, tuple, set or a dictionary.

# Dictionary Length:
about = {'name' : 'Fatema', 'country' : 'Bangladesh', 'age': 20}
print(len(about))         # 3
print(len(person))        # 8

# Accessing Dictionary Items:
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
print(dct['key1'])        # value1
print(about['country'])   # Bangladesh

print(person['skills'])     # ['Javascript', 'Python', 'Node', 'React']
print(person['address'])    # {'street': 'Space street', 'zipcode': '02215'}
print(person['fav colors']) # {'purple', 'red', 'orange'}
# print(person['city'])     # error

# checking if a key exists: (get method)
print(person.get('skills'))      # ['Javascript', 'Python', 'Node', 'React']
print(person.get('fav colors'))  # {'purple', 'orange', 'red'}
print(person.get('city'))        # None

# Adding Items to a Dictionary:
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
dct['key5'] = 'value5'
print(dct)                  # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key5': 'value5'}

about = {'name' : 'Fatema', 'country' : 'Bangladesh', 'age': 20}
about['language'] = 'Bengali'
print(about)                # {'name': 'Fatema', 'country': 'Bangladesh', 'age': 20, 'language': 'Bengali'}

person['occupation'] = 'student'
person['skills'].append('HTML')       # adding an item in list.
person['fav colors'].add('magenta')   # adding an item in set.
print(person)

# Modifying Items in a Dictionary.
about['name'] = 'Ohi'
print(about)      # {'name': 'Ohi', 'country': 'Bangladesh', 'age': 20, 'language': 'Bengali'}

# Checking Keys in a Dictionary:
print("name" in about)           # True
print('Ohi' in about)            # False

print("purple" in person)        # False
print('fav colors' in person)    # True

# Removing Key and Value Pairs from a Dictionary:
# pop(key): removes the item with the specified key name:
# popitem(): removes the last item.
# del: removes an item with specified key name.

print(about)           # {'name': 'Ohi', 'country': 'Bangladesh', 'age': 20, 'language': 'Bengali'}
print(about.pop('language'))    # Bengali
print(about)           # {'name': 'Ohi', 'country': 'Bangladesh', 'age': 20}
print(about.popitem()) # ('age', 20)
print(about)           # {'name': 'Ohi', 'country': 'Bangladesh'}
del about['country']
print(about)           # {'name': 'Ohi'}

# Changing Dictionary to a List of Items.
about = {'name': 'Ohi', 'country': 'Bangladesh', 'age': 20}
print(about.items())   # dict_items([('name', 'Ohi'), ('country', 'Bangladesh'), ('age', 20)])

# Clearing a Dictionary: If we don't want the items in a dictionary we can clear them using clear() method.
about = {'name': 'Ohi', 'country': 'Bangladesh', 'age': 20}
print(about.clear())   # None

# Deleting a Dictionary: If we do not use the dictionary we can delete it completely.
del about
# print(about)         # nameerror

# Copy a Dictionary: We can copy a dictionary using a copy() method. Using copy we can avoid mutation of the original dictionary.
about = {'name': 'Ohi', 'age': 20}
about2 = about.copy()
print(about2)          # {'name': 'Ohi', 'age': 20}
print(about2.popitem())
print(about2)          # {'name': 'Ohi'}
print(about)           # {'name': 'Ohi', 'age': 20} (unchanged)

# Getting Dictionary Keys as a List: The keys() method gives us all the keys of a a dictionary as a list.
about = {'name': 'Ohi', 'age': 20}
about_description = about.keys()
print(about_description)         # dict_keys(['name', 'age'])

# Getting Dictionary Values as a List: The values method gives us all the values of a a dictionary as a list.
about = {'name': 'Ohi', 'age': 20}
about_value = about.values()
print(about_value)               # dict_values(['Ohi', 20])