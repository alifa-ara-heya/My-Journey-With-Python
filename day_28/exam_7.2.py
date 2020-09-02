'''Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.'''


file_name = input("Enter file name: ")
file_open = open(file_name)
count = 0
total = 0
for line in file_open:
    line = line.strip()
    if line.startswith("X-DSPAM-Confidence:"):
        line = line[21: ]
        value = float(line)
        count = count + 1
        total = total + value
        average = total / count
print("Average spam confidence:", average)