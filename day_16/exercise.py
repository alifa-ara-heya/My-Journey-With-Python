# Day_16: August/12/2020
# In the name 0f Allah..
# Me: Alifa
# Book : Python Crash Course
# chapter - 5 (If statements)

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")    # True
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')      # False

# exercise: 5-3. Alien colors 1 : Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green' , 'yellow' , or 'red'. 
# • Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
alien_color = 'green'
if alien_color is "green":
    print('You have earned 5 points.')

# • Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)
alien_color = 'red'
if alien_color is "green":
    print('You have earned 5 points.')

# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3 , and write an if - else chain.
# • If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
# • Write one version of this program that runs the if block and another that runs the else block.
alien_color = 'green'
if alien_color is 'green':
    print("You have earned 5 points.")
else:
    print("You earned 10 points.")
# running the else block:
alien_color = 'yellow'
if alien_color == 'green':
    print("You have earned 5 points.")
else:
    print("You have earned 10 points. ")


# 5-5. Alien Colors #3: Turn your if - else chain from Exercise 5-4 into an if - elif-else chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed for the appropriate color alien.

# 1st version: for green
alien_color = 'green'
if alien_color == 'green':
    print('You earned 5 points.')
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

# 2nd version: for yellow
alien_color = 'yellow'
if alien_color == 'green':
    print('You earned 5 points.')
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")

# 3rd version: for red
alien_color = 'red'
if alien_color == 'green':
    print('You earned 5 points.')
elif alien_color == 'yellow':
    print("You earned 10 points.")
else:
    print("You earned 15 points.")


# 5-6. Stages of Life: Write an if - elif - else chain that determines a person’s stage of life. Set a value for the variable age , and then:
# • If the person is less than 2 years old, print a message that the person is a baby.
# • If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
# • If the person is at least 4 years old but less than 13, print a message that the person is a kid.
# • If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
# • If the person is at least 20 years old but less than 65, print a message that the person is an adult.
# • If the person is age 65 or older, print a message that the person is an elder.

age = 17
if age < 2:
    print('You are a baby.')
elif age < 4:
    print('You are a toddler.')
elif age < 13:
    print('You are a kid.')
elif age < 20:
    print('You are a teenager.')
elif age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")


# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.
favourite_fruits = ['apple', 'banana', 'lichi']
print('apple' in favourite_fruits)   # True

# • Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!
if 'apple' in favourite_fruits:
    print("You really like apples!")
if 'banana' in favourite_fruits:
    print('You really like bananas!')
if 'kiwi' in favourite_fruits:
    print('You really like kiwi!')
if 'lichi' in favourite_fruits:
    print('You really like lichi!')
if 'jackfruit' in favourite_fruits:
    print('You really like jackfruit!')


# 5-8. Hello Admin: Make a list of five or more usernames, including the name 'admin' . Imagine you are writing code that will print a greeting to each user after they log in to a website. Loop through the list, and print a greeting to each user:
# • If the username is 'admin' , print a special greeting, such as Hello admin, would you like to see a status report?
# • Otherwise, print a generic greeting, such as Hello Eric, thank you for logging in again.

usernames = ['admin', 'sahara', 'david', 'josephine']
for username in usernames:
    if username == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print("Hello " + username.title() + ', Welcome!')


# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct message is printed.

usernames.clear()
print(usernames)      # []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:        
            print("Hello " + username + ", thank you for logging in again!")
else:
    print("We need to find some users.")


# 5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users .
# • Make another list of five usernames called new_users . Make sure one or two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted.
current_users = ['eric', 'David', 'mary','hasan', 'fahima']
current_users_lower = [user.lower() for user in current_users]
new_users =['abdullah', 'david', 'hossain', 'hasan', 'Fahima']
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Sorry " + new_user + "! Please, enter a new username.")
    else:
        print("Great " + new_user + "! the username is availale.")


# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such as 1st or 2nd . Most ordinal numbers end in th , except 1, 2, and 3.
# • Store the numbers 1 through 9 in a list.
# • Loop through the list.
# • Use an if - elif - else chain inside the loop to print the proper ordinal ending for each number. Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th" , and each result should be on a separate line.
numbers = list(range(10))
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print('3rd')
    else:
        print(str(number) +'th')

print()
# or,
numbers = list(range(10))
for number in numbers:
    if number == 1:
        print("1st")
    if number == 2:
        print("2nd")
    if number == 3:
        print('3rd')
    if number > 3:
        print(str(number) +'th')