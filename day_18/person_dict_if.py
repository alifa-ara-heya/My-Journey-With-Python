# Day_18: August/14/2020
# In the name 0f Allah..
# Me: Alifa
# From: 30 Days of Python by Asabeneh (Day: 9 {conditionals})
# exercises

# 7. Here we have a person dictionary. Feel free to modify it!
person = {
    'first_name': 'Fatima',
    'last_name': 'Zahrah',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React','Node', 'MongoDB', 'Python'],
    'address': {
    'street': 'Space street',
    'zipcode': '02210'
}
}

# * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person.keys():
    print(person['skills'])

# * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person.keys():
    if 'Python' in person['skills']:
        print("The person is skilled in Python.")
# * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if 'Javascript' and 'React' in person['skills']:
    print('Frontend Developer.')
if 'Node' and 'Python' and 'MongoDB' in person['skills']:
    print('Backend Developer.')
if 'React' and 'Node' and 'MongoDB' in person['skills']:
    print("He is a fullstack developer.")
else:
    print('unknown title.')

# * If the person is married and if he lives in Finland, print the information in the following format:
if person['is_married'] == True and person['country'] == "Finland":
    print(f'{person.keys('first_name')} {person['last_name']} lives in {person['country']}. She is married.')