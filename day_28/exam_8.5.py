'''8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:

"From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end. Hint: make sure not to include the lines that start with 'From:'. You can download the sample data at http://www.py4e.com/code3/mbox-short.txt'''


fh = open('./day_28/mbox-short.txt')
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith("From "):                                   
        first_index = line.find(" ")
        last_index = line.find(" ", 6)
        line = line[first_index + 1: last_index]
        line = line.rstrip()
        print(line)
        count = count + 1
print("There were", count, "lines in the file with From as the first word")

# but, I haven't used split() here though the output is right, I have to follow the instructions.


# the following method is best I think. Thanks to the instructor.
fh = open('./day_28/mbox-short.txt')
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith("From "):  
        line = line.split()
        print(line[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")