# Day_10: August/06/2020
# In the name 0f Allah..
# Me: Alifa Ara Heya
# From: Book : Python Crash Course
# Chapter 3: Introducing lists

# Exercise: 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? 
# and Make a list that includes at least three people you’d like to invite to dinner. 
# Then use your list to print a message to each person, inviting them to dinner.

Guest_list = ["Mike", 'Alex', "Robert", "Bob"]
print(f"Hello {Guest_list[0]}! You are cordially invited to have dinner with us.")
print("Hello {}! Could you have dinner with us tomorrow? We will be glad." .format(Guest_list[1]))
print("Hello " + Guest_list[2] + "! Will you join us tomorrow for a nice dinner?")
print("Hello %s! It will be a pleasure if you come to our home for a warm dinner." %(Guest_list[3]))


# Exercise: 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# • Start with your program from Exercise 3-4 . Add a print statement at the end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still in your list.
print(f"{Guest_list[1]} can't make the dinner.")
Guest_list[1] = "Jessica"
print(f"Hi {Guest_list[1]}, can you please make some time for a dinner with our family?")
print(f"Hello {Guest_list[0]}! You are cordially invited to have dinner with us.")
print("Hello " + Guest_list[2] + "! Will you join us tomorrow for a nice dinner?")
print("Hello %s! It will be a pleasure if you come to our home for a warm dinner." %(Guest_list[3]))


# Exercise: 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5 . Add a print statement to the end of your program informing people that you found a bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.
print(Guest_list)                      # ['Mike', 'Jessica', 'Robert', 'Bob']
print("We found a bigger dinner table. We can invite more people.")
Guest_list.insert(0, "Rose")
Guest_list.insert(3, "Lily")
Guest_list.append("Jack")
print(Guest_list)                      # ['Rose', 'Mike', 'Jessica', 'Lily', 'Robert', 'Bob', 'Jack']
print(f"Hello {Guest_list[0]}! You are cordially invited to have dinner with us.")
print("Hello {}! Could you have dinner with us tomorrow? We will be glad." .format(Guest_list[1]))
print("Hello " + Guest_list[2] + "! Will you join us tomorrow for a nice dinner?")
print("Hello %s! It will be a pleasure if you come to our home for a warm dinner." %(Guest_list[3]))
print(f"Dear {Guest_list[4]}, we have organized a dinner night. Please join us.")
print(f"Dear {Guest_list[5]}, we have organized a dinner night. Please join us.")
print(f"Dear {Guest_list[6]}, we have organized a dinner night. Please join us.")



# Exercise: 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6 . Add a new line that prints a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
print("I am so sorry guys. My dinner table won't arrive in time. So I can't invite more than two people. We are extremely sorry.")
removed_guest1 = Guest_list.pop()
print(f"Hello {removed_guest1}! We are so sorry that due to some unavoidable circumstances we can't invite you tomorrow.")
removed_guest2 = Guest_list.pop()
print(f"Hello {removed_guest2}! We are so sorry that due to some unavoidable circumstances we can't invite you tomorrow.")
removed_guest3 = Guest_list.pop()
print(f"Hello {removed_guest3}! We are so sorry that due to some unavoidable circumstances we can't invite you tomorrow.")
removed_guest4 = Guest_list.pop()
print(f"Hello {removed_guest4}! We are so sorry that due to some unavoidable circumstances we can't invite you tomorrow.")
removed_guest5 = Guest_list.pop()
print(f"Hello {removed_guest5}! We are so sorry that due to some unavoidable circumstances we can't invite you tomorrow.")
print(Guest_list)
print(f"Dear {Guest_list[0]}! You are still invited. Please join us for dinner tomorrow.")
print(f"Dear {Guest_list[1]}! You are still invited. Please join us for dinner tomorrow.")


# Exercise: Use del to remove the last two names from your list, so you have an empty list. 
# Print your list to make sure you actually have an empty list at the end of your program.
del Guest_list[0]
print(Guest_list)      # ['Mike']
del Guest_list[0]
print(Guest_list)      # []