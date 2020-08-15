# Day_18: August/14/2020
# In the name 0f Allah..
# Me: Alifa
# From: 30 Days of Python by Asabeneh (Day: 9 {conditionals})

# If Condition.
a = 3
if  a> 0:
    print('a is a positive number.')  # a is a positive number.

# if else:
a = 3
if a < 0:
    print('a is a negative number.')
else:
    print("a is a positive number.")  # a is a positive number.

# if elif else:
# We use elif when we have multiple conditions.
a = 0
if a > 0:
    print('a is a positive number.')
elif a < 0:
    print('a is a negative number.')
else:
    print('a is zero.')

# Short Hand.
a = 3
print('A is positive' if a > 0 else print('A is negative'))  # A is positive.

# Nested Conditions:
a = 0
if a > 0:
    if a % 2 == 0:
        print('a is a positive and even integer.')
    else:
        print('a is a positive and odd integer.')
elif a == 0:
    print('a is zero.')
else:
    print('a is a negative number.')

# We can avoid writing nested condition by using logical operator and..
a = 0
if a  > 0 and a % 2 == 0:
    print('a is a positive and even integer.')
elif a > 0 and a % 2 != 0:
    print('a is a positive and odd integer.')
elif a == 0:
    print('a is zero.')
else:
    print('a is a negative number.')

# If and Or Logical Operators.
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
    print('Aceess granted!')
else:
    print('Aceess denied!')