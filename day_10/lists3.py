# Day_10: August/06/2020
# In the name 0f Allah..
# Me: Alifa Ara Heya
# From: Book : Python Crash Course
# Chapter 3: Introducing lists

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())                    # Trek

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)                                # My first bicycle was a Trek.

#Exercise 3-1
# Store the names of a few of your friends in a list called names . 
# and  Print each person’s name by accessing each element in the list, one at a time.

names = ['Ayesha', 'Mumu', 'Fabiha', 'Nipu']
print(names[0])                               # Ayesha
print(names[1])                               # Mumu
print(names[2])                               # Fabiha
print(names[3])                               # Nipu 

#Exercise 3-2:
# Greetings: Start with the list you used in Exercise 3-1 , but instead of just printing each person’s name, print a message to them. 
# And The text of each message should be the same, but each message should be personalized with the person’s name.

print(f"I adore {names[0]} very much.")       # I adore Ayesha very much.
print(f"I adore {names[1]} very much.")       # I adore Mumu very much.
print(f"I adore {names[2]} very much.")       # I adore Fabiha very much.
print(f"I adore {names[3]} very much.")       # I adore Nipu very much.


#Exercise 3-3:
# Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. 
# Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
transportation = ['Rickshaw', 'Boat', 'Train', 'Bus', 'Scooter']
print(f"I love to ride on {transportation[0].lower()} very much. I miss it.")
print(f"I am afraid of riding a {transportation[1].lower()} but very much want to ride it.")
print(f"I miss riding on {transportation[2].lower()}.")
print(f"I love the breeze while riding on a {transportation[3].lower()}.")
print(f"I would like to own a {transportation[4].lower()} some day, inshaaAllah.")
print("I like " + transportation[2].lower() + ".")

# Modifying the list.
transportation[1] = 'Ship'
print(transportation)                         # ['Rickshaw', 'Ship', 'Train', 'Bus', 'Scooter']

# Adding elements to a list
pets = []
pets.append("cat")
pets.append("chicken")
pets.append("falcon")
pets.append("eagle")
print(pets)                                   # ['cat', 'chicken', 'falcon', 'eagle']

del pets[2]
print(pets)                                   # ['cat', 'chicken', 'eagle']

# deleting elements by pop() method:
motorcycles = ["Honda", "Yamaha", "Suzuki"]
motorcycles.pop()
print(motorcycles)                             # ['Honda', 'Yamaha']

# if you want to work with the remoed item, you better use pop() method.
motorcycles = ["Honda", "Yamaha", "Suzuki"]
popped_motorcycles = motorcycles.pop()
print(popped_motorcycles)                      # Suzuki
print(motorcycles)                             # ['Honda', 'Yamaha']

motorcycles = ["Honda", "Yamaha", "Suzuki"]
last_bike = motorcycles.pop(1)
print("The last motorcycle I owned was a " + last_bike + ".")  # The last motorcycle I owned was a Yamaha.


# remove() method: deleting item by value:
motorcycles = ["Honda", "Yamaha", "Suzuki", "Ducati"]
removed_bike = "Ducati"
motorcycles.remove(removed_bike)
print(motorcycles)                             # ['Honda', 'Yamaha', 'Suzuki']
print(removed_bike)                            # Ducati
print("\nA "+ removed_bike + " is too expensive for me.")      # A Ducati is too expensive for me.