fname = "./day_28/romeo.txt"
fh = open(fname)
lst = list()
for line in fh:
    #line.split(" ")
    delimiter = " "
    line.split(delimiter)
    lst.append(line)
    lst = line.split(delimiter)
    #line.replace("\n", "")
    #lst.append(line)
print(lst[7])
