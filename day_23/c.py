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

print()
# break:
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        break             # 0 1 2

print()
# continue:
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        continue          # 0 1 2 3 4

print()
# skipping 2, 5:
count = 0
while True:
    count += 1
    if count == 2:
        continue
    if count == 5:
        break
    print(count)          # 1 3 4

       
print()
count = 0
while count < 5:
    print(count)
    count += 1
    if count == 3:
        continue