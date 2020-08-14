# Day_18: August/14/2020
# In the name 0f Allah..
# Me: Alifa
# From: 30 Days of Python by Asabeneh (Day: 8 {Dictionaries})
# Exercises:

# 1. Create a an empty dictionary called dog.
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary.
dog = {
    'name' : 'Tiku',
    'color' : 'brown',
    'breed' : "Doberman",
    'legs' : 4,
    'age' : 6
}

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary.
student = {
    'first_name' : 'Alfi',
    'last_name' : 'Ohi',
    'gender' : 'male',
    'age' : 12,
    'marital status': False,
    'skills' : ['gaming', 'hacking', 'running'],
    'country' : 'Bangladesh',
    'city' : 'Rajshahi',
    'address': {
        "road" : '21 no rocket road',
        'location' : 'Space road',
    }
}

# 4. Get the length of the student dictionary.
print(len(student))       # 9

# 5. Get the value of skills and check the data type, it should be a list.
skills_value = student['skills']
print(skills_value)       # ['gaming', 'hacking', 'running']
print(student['skills'])  # ['gaming', 'hacking', 'running']
print(type(skills_value)) # <class 'list'>

# 6. Modify the skills values by adding one or two skills.
student['skills'].append('tech')
print(student['skills'])  # ['gaming', 'hacking', 'running', 'tech']
print(student)

# 7. Get the dictionary keys as a list.
print(student.keys())     # dict_keys(['first_name', 'last_name', 'gender', 'age', 'marital status', 'skills', 'country', 'city', 'address'])

# 8. Get the dictionary values as a list.
print(student.values())  # dict_values(['Alfi', 'Ohi', 'male', 12, False, ['gaming', 'hacking', 'running', 'tech'], 'Bangladesh', 'Rajshahi', {'road': '21 no rocket road', 'location': 'Space road'}])

# 9. Change the dictionary to a list of tuples using items() method.
print(student.items())   # dict_items([('first_name', 'Alfi'), ('last_name', 'Ohi'), ('gender', 'male'), ('age', 12), ('marital status', False), ('skills', ['gaming', 'hacking', 'running', 'tech']), ('country', 'Bangladesh'), ('city', 'Rajshahi'), ('address', {'road': '21 no rocket road', 'location': 'Space road'})])

# 10. Delete one of the items in the dictionary.
print(student.popitem()) # ('address', {'road': '21 no rocket road', 'location': 'Space road'}) (removed the last item.)

print(student.pop("marital status")) # False (removed)

print(student)           # {'first_name': 'Alfi', 'last_name': 'Ohi', 'gender': 'male', 'age': 12, 'skills': ['gaming', 'hacking', 'running', 'tech'], 'country': 'Bangladesh', 'city': 'Rajshahi'}