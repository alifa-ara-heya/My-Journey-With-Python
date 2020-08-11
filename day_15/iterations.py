# Day_15: August/10/2020
# In the name 0f Allah..
# Me: Alifa
# From: Book : Python for everybody
# Chapter:5 (Iterations)

# Here is a simple program that counts down from five and then says “Blastoff!”.
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")

# writing infinite loop effectively:
# suppose you want to take input from the user until they type done. You could write:
while True:
    line = input('> ')
    if line == "done":
        break
    print(line)
print("Done!")


# Here is an example of a loop that copies its input until the user types “done”, but treats lines that start with the hash character as lines not to be printed (kind of like Python comments).
while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print("All Done!")