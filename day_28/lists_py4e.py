# day - 28
# August - 31- 2020
# python for everybody (chapter : 8)

numbers = [17, 5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)          # [34, 10]

print(numbers * 3)      # [34, 10, 34, 10, 34, 10]


t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:2] = ['x', 'y']
print(t)                # ['a', 'x', 'y', 'c', 'd', 'e', 'f']

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1 : 3] = ['x', 'y']
print(t)                # ['a', 'x', 'y', 'd', 'e', 'f']


s = 'pining for the fjords'
t = s.split()
print(t)                # ['pining', 'for', 'the', 'fjords']

t = ['pining', 'for', 'the', 'fjords']
delimiter = " "
print(delimiter.join(t)) # pining for the fjords

# using files: slice the days from the following line.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
file_handle = open(".\day_28\mbox-short.txt")
for line in file_handle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        print(words[2])

#
a = 'banana'
b = 'banana'
print(a is b)             # True
# but,
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)             # False

a = b
print(a == b)             # True

b[0] = 17
print(a)                  # [17, 2, 3]



def delete_head(t):
    del t[0]


letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)           # ['b', 'c']


'''imp: the append method modifies a list, but the + operator creates a new list:'''



line = 'I am stupid.'
print(line.find(" "))      # 1
print(line.find(" ", 2))   # 4