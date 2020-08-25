# day_23
# Asabeneh: 30 days of python
# day_10 (while and for loops)

# counting from 0 to 4:
count = 0
while count < 4:
    print(count)
    count += 1            # 0 1 2 3 4  (5 isn't printed here.)


print()                   # giving this break for the terminal to be readable.

# else:
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print(count)          # 0 1 2 3 4 5
# 5 is printed here. The above loop condition will be false when count is 5 and the loop stops, and execution starts the else statement. As a result 5 will be printed.


# break:
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break             # 0 1 2


# continue:
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        continue          # 0 1 2 3 4


# skipping 2, 5:
count = 0
while True:
    count += 1
    if count == 2:
        continue
    if count == 5:
        break
    print(count)          # 1 3 4

       
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        continue         # 0 1 2 3 4

# loops in tuples:
numbers = (0, 1, 2, 3, 4, 5)
for num in numbers:
    print(num)           # 0 1 2 3 4 5

# loops in dictionaries:
info = {
    'name' : 'Piki',
    'class' : 5,
    'country': 'wonderland'
}
for key in info:
    print(key)          # name class country

for value in info:
    print(value)        # name class country ( I have named the variable 'value' because actually it can be anything, but it will always print just the keys.)

for key, value in info.items():
    print(key, value)  # name Piki    class 5   country wonderland

# loops in sets:
name = {'kiwi', 'banana', 'lichi', 'kiwi'}
for fruit in name:
    print(fruit)      # lichi banana kiwi

# break for:
numbers = (0, 1, 2, 3, 4, 5)
for num in numbers:
    print(num)
    if num == 3:
        break         # 0 1 2 3


numbers = (0, 1, 2, 3, 4, 5)
for num in numbers:
    if num == 3:
        break
    print(num)        # 0 1 2


# continue for:
numbers = (0, 1, 2, 3, 4, 5)
for num in numbers:
    print(num)
    if num == 3:
        continue      # 0 1 2 3 4 5

numbers = (0, 1, 2, 3, 4, 5)
for num in numbers:
    if num == 3:
        continue
    print(num)        # 0 1 2 4 5 (skipping 3)
    


numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')

# output:
# 0
# Next number should be  1
# 1
# Next number should be  2
# 2
# Next number should be  3
# 3
# 4
# Next number should be  5
# 5
# loop's end
# outside the loop

# range:
lst = list(range(11))
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

st = set(range(11))
print(st)           # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

tpl = tuple(range(11))
print(tpl)          # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

st2 = set(range(1, 11))
print(st2)          # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst2 = list(range(11, 2))
print(lst2)         # []

lst3 = list(range(1, 11, 2))
print(lst3)         # [1, 3, 5, 7, 9]

lst4 = list(range(0, 11, 2))
print(lst4)         # [0, 2, 4, 6, 8, 10]


# nested for loop:
info = {
    'name' : 'Piki',
    'class' : 5,
    'country': 'wonderland',
    'skills' : ['running', 'jumping', 'diving', 'swimming']
}
for key in info:
    if key == 'skills':
        for skill in info['skills']:
            print(skill)     # running  jumping  diving  swimming

# For else:
for num in range(11):
    print(num)
else:
    print("The loop stops at, ", num) 
# output: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)   The loop stops at,  10


# In python when statement is required (after semicolon), but we don't like to execute any code there, we can write the word pass to avoid errors. Also we can use it as a placeholder, for future statements.
for num in range(6):
    pass        # output nothing

#
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1


words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
parts = pieces[3].split('-')
print(pieces)           # ['His', 'e-mail', 'is', 'q-lar@freecodecamp.org']
print(parts)            # ['q', 'lar@freecodecamp.org']


#
counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('mrugesh' , 42))  # 42