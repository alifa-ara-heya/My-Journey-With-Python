# 2/ September / 2020
# Python for everybody
# chapter: 9 (Dictionary)

empty_dict = dict()
print(empty_dict)          # {}

empty_dict['one'] = 'who'
print(empty_dict)          # {'one': 'who'}

person = {'name': 'Ohi', 'age': 12, 'gender': 'boy'}
print('ohi' in person.values())   # False
print('Ohi' in person.values())   # True
print('Ohi' in person.keys())     # false
print('Name' in person.keys())    # false
print('name' in person.keys())    # true


# Dictionary as a set of counters:
# Suppose you are given a string and you want to count how many times each letter appears. One way to do this:
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
    
print(d)     # {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}


person = {'name': 'Ohi', 'age': 12, 'gender': 'boy'}
print(person.get('age'))        # 12
print(person.get('age', 0))     # 12 ( the 0 is default and optional)

# we can write the counting program more concisely now:
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1
print(d)    # {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}


# Dictionary and files:
fhand = open('./day_29/romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)
    

# Looping and dictionaries.
person = {'name': 'Ohi', 'age': 12, 'gender': 'boy'}
for key in person:
    print(key, person[key])   # name Ohi    age 12    gender boy


lst = list(person.keys())
print(lst)                    # ['name', 'age', 'gender']

lst2 = list(person.values())
print(lst2)                   # ['Ohi', 12, 'boy']

lst.sort()
for key in lst:
    print(key, person[key])  # age 12    gender boy    name Ohi



# Advanced text parsing

import string
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

fopen = open('./day_29/romeo.txt')
count = dict()
for line in fopen:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    
print(count)

