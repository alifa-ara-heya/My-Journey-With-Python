# 31- Aug - 2020
# Files 
# (book: Python for everybody! chapter: 7)

fhand = open('./day_28/mbox.txt')
print(fhand)


fhand = open('./day_28/mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)    # Line Count: 1910


fhand = open('./day_28/mbox-short.txt')
inp = fhand.read()
print(len(inp))                # 94626
print(inp[:20])                # From stephen.marquar


fhand = open('./day_28/mbox-short.txt')
print(len(fhand.read()))       # 94626
print(len(fhand.read()))       # 0



# if we wanted to read a file and only print out lines which started with the prefix “From:”, we could use the string method 'startswith' to select only those lines with the desired prefix:
fhand = open('./day_28/mbox-short.txt')
count = 0
for line in fhand:
    if line.startswith('From:'):
        print(line)


# to remove the newlines:
fhand = open('./day_28/mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)

# We can structure the loop to follow the pattern of skipping uninteresting lines as follows: (continue)
fhand = open('./day_28/mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:'):        # skip uninteresting lines:
        continue
    print(line)                             # proess our 'interesting' lines:
    # output is same as the pervious lines of code. In English, the uninteresting lines are those which do not start with “From:”, which we skip using continue. For the “interesting” lines (i.e., those that start with “From:”) we perform the processing on those lines.


# if we want to search the lines containing the string  “@uct.ac.za” :

fhand = open('./day_28/mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find("@uct.ac.za") == -1:   continue
    print(line)

# writing files:
fopen = open('output.txt', 'w')
print(fopen)

line1 = "This here's the wattle,\n"
print(fopen.write(line1))       # 24

fopen.close()


# Debugging to see the tabs, newlines, whitespaces:
s = "1 2\t 3\n 4"
print(s)
# output:
# 1 2      3
# 4             
print(repr(s))          # '1 2\t 3\n 4'