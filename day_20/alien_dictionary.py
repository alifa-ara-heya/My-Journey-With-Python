# Day_20: August/16/2020
# In the name 0f Allah..
# Me: Alifa
# Python Crash Course by Eric Matthes (Chapter: 6 [Dictionaries])

alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0['color'])          # green
print(alien_0['points'])         # 5

new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')
print(alien_0)                   # {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)                   # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

# Creating an empty dictionary:
alien_0 = {}
alien_0['color'] = "green"
alien_0['points'] = 5
print(alien_0)                   # {'color': 'green', 'points': 5}


# Modifying Values in a Dictionary:
alien_0['color'] = 'red'
print(alien_0)                   # {'color': 'red', 'points': 5}

alien_0 = {'color' : 'green'}
print("The alien is " + alien_0['color'] + '.' )     # The alien is green.
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + '.')  # The alien is yellow.

# For a more interesting example, let’s track the position of an alien that can move at different speeds. We’ll store a value representing the alien’s current speed and then use it to determine how far to the right the alien should move:

alien_0 = {'x-position' : 0, 'y-position' : 25, 'speed' : 'medium', 'points' : 5}
print('Original x-position: ' + str(alien_0['x-position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:                # This must be a fast alien.
    x_increment = 3  # The new position is the old position plus the increment.

alien_0['x-position'] = alien_0['x-position'] + x_increment
print("New x-position: " + str(alien_0['x-position']))


# Removing Key-Value Pairs:
del alien_0['points']
print(alien_0)

# A Dictionary of Similar Objects:
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + '.')                  # Sarah's favorite language is C.
# or,
print("Sarah's favorite language is " +
favorite_languages['sarah'].title() +
'.')

# Looping through a Dictionary:
user_0 = {
    'username' : 'efarmi',
    'first' : 'enrico',
    'last' : 'fermi',
}

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

#or,
for k, v in user_0.items():
    print("\nInfo: " + k)
    print("Value: " + v)

# looping the favorite language:
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
for person, favorite_language in favorite_languages.items():
    print(f"{person.title()} loves {favorite_language.title()}.")


# Looping Through All the Keys in a Dictionary: Printing who took the pole.
for person in favorite_languages.keys():
    print(person.title())            # Jen      Sarah       Edward     Phil
# or,
for person in favorite_languages:
    print(person.title())            # Jen      Sarah       Edward     Phil

print()
# You can access the value associated with any key you care about inside the loop by using the current key. Let’s print a message to a couple of friends about the languages they chose.
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
friends = ['phil', 'sarah']
for person in favorite_languages.keys():
    print(person.title())
    if person in friends:
        print('Hi ' + person.title() + ", I see your favorite language is " + favorite_languages[person].title() + "!")


if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


# Looping Through a Dictionary’s Keys in Order.
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll!")

# Looping Through All Values in a Dictionary.
print("The following languages have been mentioned: ")
for language in favorite_languages.values():
    print(language.title())

# if we want to print the languages without repetition we can use set method.
print("The following languages have been mentioned: ")
for language in set(favorite_languages.values()):
    print(language.title())