# Day_11: August/07/2020
# In the name 0f Allah..
# Me: Alifa Ara Heya
# From: Book : Python Crash Course
# Chapter 4: Working with lists


# Working with part of a list (slicing a list):
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# To output the first three elements in a list,
print(players[0 : 3])            # ['charles', 'martina', 'michael']

# if you want the second, third, and fourth items in a list:
print(players[1 : 4])            # ['martina', 'michael', 'florence']

# If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list:
print(players[: 2])              # ['charles', 'martina']

# if you want all items from the third item through the last item,
print(players[2:])               # ['michael', 'florence', 'eli']

# if we want to output the last three players on the roster,
print(players[-3:])              # ['michael', 'florence', 'eli']


# Looping through a slice:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are my first three favourite players:")
for player in players[:3]:
    print(player.title())

# Copying a list: Creating copied but two separate list;
my_favourite_food = ["biriyani", "Fuchka", "Chicken fry"]
my_friend_likes = my_favourite_food.copy()
print(my_friend_likes)          # ['biriyani', 'Fuchka', 'Chicken fry']

my_favourite_food.append("chips")
print(my_favourite_food)        # ['biriyani', 'Fuchka', 'Chicken fry', 'chips']
print(my_friend_likes)          # ['biriyani', 'Fuchka', 'Chicken fry']

# or,
my_sister_likes = my_favourite_food[:]
print(my_sister_likes)          # ['biriyani', 'Fuchka', 'Chicken fry']

my_favourite_food.append("beef steak")
print(my_favourite_food)        # ['biriyani', 'Fuchka', 'Chicken fry', 'beef steak']

print(my_sister_likes)          # ['biriyani', 'Fuchka', 'Chicken fry']
print(my_friend_likes)          # ['biriyani', 'Fuchka', 'Chicken fry']

# But look here, if we create copied list like below, it won't produce separate list.
my_friend_likes = my_favourite_food
print(my_friend_likes)          # ['biriyani', 'Fuchka', 'Chicken fry', 'beef steak']

my_favourite_food.append("noodles")
print(my_favourite_food)        # ['biriyani', 'Fuchka', 'Chicken fry', 'beef steak', 'noodles']
print(my_friend_likes)          # ['biriyani', 'Fuchka', 'Chicken fry', 'beef steak', 'noodles']