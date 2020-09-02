fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
# output : There were 27 subject lines in ./day_28/mbox-short.txt 
# output : There were 1797 subject lines in ./day_28/mbox.txt

