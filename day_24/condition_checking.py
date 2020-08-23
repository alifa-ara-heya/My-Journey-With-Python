# day 24
# 23- August- 2020
# sohoj vashay python

a = 5
if a:
    print(True)
else:
    print(False)           # True

a = 0
if a:
    print(True)
else:
    print(False)           # False


a = None
if a:
    print(True)
else:
    print(False)          # False


a = not None
if a:
    print(True)
else:
    print(False)          # True


a = [1, 2,3]
b = a
print(b == a)             # True
print(b is a)             # True

b = a[:]
print(b == a)             # True
print(b is a)             # False


print(4 is 2 * 2)         # True
print(4 == 2 * 2)         # True

print(1000 == 10 ** 3)    # True
print(1000 is 10 ** 3)    # True