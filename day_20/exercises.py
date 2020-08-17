# Day_19: August/15/2020
# In the name 0f Allah..
# Me: Alifa
# Python Crash Course by Eric Matthes (Chapter: 6 [Dictionaries])

# 6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name , last_name , age , and city . Print each piece of information stored in your dictionary.

person = {
    'first_name' : 'Tahera',
    'last_name' : 'Siddiqua',
    'age' : 24,
    'city' : 'Chittagong',
}
print(f"I know {person['first_name']} {person['last_name']}.")
print(f"She is {person['age']} years old.")
print(f"She lives is {person['city']}.")