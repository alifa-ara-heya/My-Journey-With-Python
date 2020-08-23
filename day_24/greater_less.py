# day 24
# 23- August- 2020
# sohoj vashay python

a = int(input("enter a number: "))
if a < 10:
    if a % 2 == 0:
        print("less, yes")
    else:
        print("less, no")
else:
    if a % 3 == 0:
        print('greater, yes')
    else:
        print('greater, no')