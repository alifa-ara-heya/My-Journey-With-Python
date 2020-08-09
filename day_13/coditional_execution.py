# Day_13: August/09/2020
# In the name 0f Allah..
# Me: Alifa
# From: Book : Python for everybody
# chapter: 3
# Conditional operator:
print("x" == "y")        # False
n = 18
print(n % 2 == 0 or n % 3 == 0)  # True (the number is divisible by both 2 and 3)

x = 4
y = 5
print(x > y)             # False
print(not x > y)         # True


print(17 and True)       # True

x = 4
if x > 0:
    print("x is positive.")     # x is positive.

if x < 0:
    pass                 # need to handle negative values.
# Occasionally, it is useful to have a body with no statements (usually as a place holder for code you haven’t written yet). 
# In that case, you can use the pass statement, which does nothing.

x = 3
if x < 10:
    print('small')


# Alternative execution:
if x % 2 == 0:
    print("x is even.")
else:
    print("x is odd.")         # x is odd.


# Chained conditionals:
x = 9
y = 8
if x < y:
    print("x is less than y.")
elif x > y:
    print("x is greater than y.")
else:
    print("x is equal to y.")


# Nested conditionals:
# One conditional can also be nested within another. We could have written the three-branch example like this:
if x == y:
    print('x and y are equal.')
else:
    if x < y:
        print("x is less than y.")
    else:
        print("x is greater than y.")

# Nested if statements:
# it is good idea to avoid nested conditionals if I can.
if 0 < x:
    if x < 10:
        print("x is a positive single digit number.")

# or,
if 0 < x and x < 10:
    print("x is a positive single digit number.")


# Debugging: Be aware of indentation error.
x = 5
 #y = 2
#print(y)   # Traceback because of indentation error.


# loop:
for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2.')
    print("done with i =", i, ".")
print('All done.')