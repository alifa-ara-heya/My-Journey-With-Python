# day 24
# 23- August- 2020
# sohoj vashay python

for num in range(0, 11):
    print(num)      # 0 1 2 3 4 5 6 7 8 9 10

# or,
num = 0
while num <= 10:
    print(num)
    num = num + 1   # 0 1 2 3 4 5 6 7 8 9 10

num = 0
while num <= 10:
    num = num + 1
    print(num)     # 1 2 3 4 5 6 7 8 9 10 11

# summing 1 to 100:
total = 0
for num in range(1, 101):
    total =  num + total
print(total)       # 5050

# or,
num = 1
total = 0
while num <= 100:
    total = total + num
    num =  num + 1
print(total)              # 5050

# or,
n = 100
total = n * (n + 1) / 2
print(total)              # 5050.0


for num in range(5):
    print(num)            # 0 1 2 3 4

for num in range(0, 5):
    print(num)            # 0 1 2 3 4

print(list(range(5, 11))) # [5, 6, 7, 8, 9, 10]

print(str(range(5, 11)))  # range(5, 11)

# break:
for num in range(1, 11):
    print(num)            # 1 2 3 4 5 6 7 8 9 10

for num in range(1, 11):
    if num == 5:
        break
    print(num)            # 1 2 3 4


# continue:
for num in range(1, 11):
    if num == 5:
        continue
    print(num)            # 1 2 3 4 6 7 8 9 10


# pass:
for num in range(1, 11):
    if num == 5:
        pass
    print(num)            # 1 2 3 4 5 6 7 8 9 10


# else: when the condition of while becomes false, the else block starts executing.
num = 0
while num <= 10:
    print(num)
    num = num + 1
else:
    print("The loop is over.")   # 0 1 2 3 4 5 6 7 8 9 10 The loop is over.

print()
# else in for:
for n in range(0, 11):
    print(n)
else:
    print("The loop is over.")   # 0 1 2 3 4 5 6 7 8 9 10 The loop is over.