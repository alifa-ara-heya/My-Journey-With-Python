''' 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by time of the day for each of the messages. You can pull the time out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each time, print out the counts, sorted by time as shown below. '''

fname = open('./day_28/mbox-short.txt')
lst = list()
counts = dict()
for line in fname:
    line = line.strip()
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hour = time[:2]
        lst.append(hour)

for h in lst:
    if h not in counts:
        counts[h] = 1
    else:
        counts[h] = counts[h] + 1
# print(counts)        # {'09': 2, '18': 1, '16': 4, '15': 2, '14': 1, '11': 6, '10': 3, '07': 1, '06': 1, '04': 3, '19': 1, '17': 2}         

# sorting the dictionary by value:
lst = list()
for key, val in list(counts.items()):
    lst.append((key, val))

# print(lst)           # [('09', 2), ('18', 1), ('16', 4), ('15', 2), ('14', 1), ('11', 6), ('10', 3), ('07', 1), ('06', 1), ('04', 3), ('19', 1), ('17', 2)]

lst.sort()
# print(lst)            # [('04', 3), ('06', 1), ('07', 1), ('09', 2), ('10', 3), ('11', 6), ('14', 1), ('15', 2), ('16', 4), ('17', 2), ('18', 1), ('19', 1)]

for key, val in lst:
    print(key, val)