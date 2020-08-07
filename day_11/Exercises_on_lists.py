# Day_11: August/07/2020
# In the name 0f Allah..
# Me: Alifa Ara Heya
# From: Book : Python Crash Course
# Chapter 3 and 4: Introducing lists and Working with lists (Exercises)

# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.

travel_dream = ["Sylhet", "Satkhira","Makkah", "Madina", "Kashmir", "Ladakh", "Norway"]

# • Print your list in its original order. Don’t worry about printing the list neatly, just print it as a raw Python list.
print(travel_dream)

# • Use sorted() to print your list in alphabetical order without modifying the actual list.
print(sorted(travel_dream))

# • Show that your list is still in its original order by printing it.
print(travel_dream)

# • Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(sorted(travel_dream, reverse = True))

# • Show that your list is still in its original order by printing it again.
print(travel_dream)

# • Use reverse() to change the order of your list. Print the list to show that its order has changed.
travel_dream.reverse()
print(travel_dream)

# • Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
travel_dream.reverse()
print(travel_dream)

# • Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
travel_dream.sort()
print(travel_dream)

# • Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
travel_dream.sort(reverse=True)
print(travel_dream)

# Exercise: 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
pizzas = ["BBQ Chicken", "Margherita pizza", "Pepperoni pizza"]
for pizza in pizzas:
    print(pizza)

#• Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
for pizza in pizzas:
    print("I like " + pizza + " very much.")

# • Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
for pizza in pizzas:
    print("I like " + pizza + " very much.")
print("\nI like pizza a lot. Because they are spicy.")

# Exercise: 4-2. Animals: Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal.
pets = ["cat", "rabbit", "horse", "dog"]
for pet in pets:
    print(pet.title())

# • Modify your program to print a statement about each animal, such as A dog would make a great pet.
print(f"Jimmy likes {pets[0]}.")                     # Jimmy likes cat
print(f"{pets[1].title()}s are so cute.")            # Rabbits are so cute.
print(f"I wish I had a {pets[2]}!")                  # I wish I had a horse!
print(f"{pets[3].title()}s are so faithful.")        # Dogs are so faithful.


# • Add a line at the end of your program stating what these animals have in common. You could print a sentence such as Any of these animals would make a great pet!
print("Any of these animals would make a great pet!")


# Exercises: 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.
for numbers in range(1, 21):
    print(numbers)


#Exercises: 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL -C or by closing the output window.)
million = list(range(1, 1000001))
# print(million)            # I have disabled this because it's a huge list.

# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.
print("Sum of million numbers:", sum(million),"\n")          # Sum of million numbers: 500000500000
print("Maximum million numbers:",max(million),"\n")          # Maximum million numbers: 1000000
print("Minimum million numbers:", min(million))              # Minimum million numbers: 1


# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.
odd_numbers = list(range(1,21,2))
print(odd_numbers)                                           # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
for odd_number in odd_numbers:
    print(odd_number)


# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
threes = []
for value in range(1, 11):
    threes.append(value * 3)
print(threes)            # I have programmed to make this list in stead of manually adding the numbers in a list.

for multiples_of_three in threes:
    print(multiples_of_three)


# 4-8. Cubes: A number raised to the third power is called a cube . For example, the cube of 2 is written as 2**3 in Python. 
# Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.
cubes = []
for integer in range(1 , 11):
    cubes.append(integer ** 3)
print(cubes)             # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

for cube in cubes:
    print(cube)


# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.
cubes2 = [integer ** 3 for integer in range(1, 11)]
print(cubes2)            # [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# • Print the message, The first three items in the list are: . Then use a slice to print the first three items from that program’s list.
color = ["blue", 'red', 'yellow', 'black', 'white']
print(f"The first three colors in my lists are: ")
print(color[:3])         # ['blue', 'red', 'yellow']


# • Print the message, Three items from the middle of the list are: . Use a slice to print three items from the middle of the list.
print(f"Three items from the middle of the list are: {color[1 : 4]}.")   # Three items from the middle of the list are: ['red', 'yellow', 'black']


# • Print the message, The last three items in the list are: . Use a slice to print the last three items in the list.
print(f"The last three items in the list {color[-3:]}.")                 # The last three items in the list ['yellow', 'black', 'white'].


# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1. 
# Make a copy of the list of pizzas, and call it friend_pizzas . Then, do the following:
pizzas = ["BBQ Chicken pizza", "Margherita pizza", "Pepperoni pizza"]
friend_pizzas = pizzas[:]

# • Add a new pizza to the original list.
pizzas.append("Cheesy pizza")
# • Add a different pizza to the list friend_pizzas.
friend_pizzas.append('Spicy pizza')
# • Prove that you have two separate lists. Print the message, My favorite pizzas are: , and then use a for loop to print the first list.
print(f"My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza) 
# Print the message, My friend’s favorite pizzas are: , and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
print(f"My friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)