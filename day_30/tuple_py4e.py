t = ('a', 'b', 'c', 'd')
t1 = ('a',)

t2 = tuple()
print(t2)         # ()

t4 = tuple('important')
print(t4)         # ('i', 'm', 'p', 'o', 'r', 't', 'a', 'n', 't')

print(t4[1])      # m
print(t4[1 : 3])  # ('m', 'p')

# You can’t modify the elements of a tuple, but you can replace one tuple with another:

t = ('A',) + t[1:]
print(t)          # ('A', 'b', 'c', 'd')


# Comparing tuples:
print((0, 1, 2) < (0, 3, 4))         # True
print((0, 1, 200000) < (0, 3, 4))    # True


# suppose you have a list of words and you want to sort them from longest to shortest:
txt = 'but soft what light in yonder window breaks'
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

# print(t)    output: [(3, 'but'), (4, 'soft'), (4, 'what'), (5, 'light'), (2, 'in'), (6, 'yonder'), (6, 'window'), (6, 'breaks')]

t.sort(reverse = True)

# print(t)    output: [(6, 'yonder'), (6, 'window'), (6, 'breaks'), (5, 'light'), (4, 'what'), (4, 'soft'), (3, 'but'), (2, 'in')]

only_word = list()
for length, word in t:
    only_word.append(word)

print(only_word)       # ['yonder', 'window', 'breaks', 'light', 'what', 'soft', 'but', 'in']


# Tuple assignment:
m = ['have', 'fun']
x, y = m
print(x)               # have
print(y)               # fun
# or,
m = ['have', 'fun']
x = m[0]
y = m[1]
print(x)              # have
print(y)              # fun
# or,
m = ['have', 'fun']
(x, y) = m
print(x)              # have
print(y)              # fun


# A particularly clever application of tuple assignment allows us to swap the values of two variables in a single statement:
#a, b = b, a

#a, b = 1, 2, 3

# to split an email address into a user name and a domain, you could write:

address = 'monty@python.org'
username, domain = address.split('@')
print(address.split())    # ['monty@python.org']
print(address.split('@')) # ['monty', 'python.org']
print(username)           # monty
print(domain)             # python.org


# Dictionaries and tuples:    Dictionaries have a method called items that returns a list of tuples, where each tuple is a key-value pair:
d = {'a' : 10, 'b' : 1, 'c' : 22}
t = list(d.items())
print(t)                  # [('a', 10), ('b', 1), ('c', 22)]
print(d.items())          # dict_items([('a', 10), ('b', 1), ('c', 22)])


# Multiple assignment with dictionaries.
for key, val in list(d.items()):
    print(val, key)       # 10  a    1  b    22  c


d = {'a' : 10, 'b' : 1, 'c' : 22}
l = list()
for key, value in d.items():
    l.append( (value, key) ) 
print(l)    # [(10, 'a'), (1, 'b'), (22, 'c')]

l.sort(reverse = True)
print(l)    # [(22, 'c'), (10, 'a'), (1, 'b')]


# The most common words:
# Coming back to our running example of the text from Romeo and Juliet Act 2, Scene 2, we can augment our program to use this technique to print the ten most common words in the text as follows:
import string
fhand = open('./day_30/romeo-full.txt')
count = dict()
for line in fhand:
    line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1

# sort the dictionary by value:
lst = list()
for key, val in list(count.items()):
    lst.append((val, key))

lst.sort(reverse = True)

for key, val in lst[:10]:
    print(key, val)

''' output:
60 i
42 and
34 to
34 the
32 thou
31 romeo
30 juliet
29 that
29 my
24 a '''


# Using tuples as keys in dictionaries:
# Assuming that we have defined the variables last, first, and number, we could write a dictionary assignment statement as follows:
last = 'Piku'
first = 'Tiku'
number = 3618
# directory[last, first] = number

# for last, first in directory:
    # print(first, last, directory[last,first])

# This loop traverses the keys in directory, which are tuples. It assigns the elements of each tuple to last and first, then prints the name and corresponding telephone number.