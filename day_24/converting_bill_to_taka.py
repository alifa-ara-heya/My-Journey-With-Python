# day 24
# 23- August- 2020
# sohoj vashay python


bill = int(input("Please, enter your lunch bill: "))

a = bill

no_of_note = bill // 1000
print(no_of_note, '1000 taka note(s)')
if no_of_note > 0:       # if at least 1 note of 1000 taka is needed:
    rest = no_of_note % 1000
    a = rest
else:
    bill = a

no_of_note = bill // 500
print(no_of_note, '500 taka note(s)')
if no_of_note > 0:
    rest = no_of_note % 500
    a = rest
else:
    bill = a

no_of_note = bill // 100
print(no_of_note, '100 taka note(s)')
if no_of_note > 0:
    rest = no_of_note % 100
    a = rest
else:
    bill = a

no_of_note = bill // 50
print(no_of_note, '50 taka note(s)')
if no_of_note > 0:
    rest = no_of_note % 50
    a = rest
else:
    bill = a

no_of_note = bill // 20
print(no_of_note, '20 taka note(s)')
if no_of_note > 0:
    rest = no_of_note % 20
    a = rest
else:
    bill = a

no_of_note = bill // 10
print(no_of_note, '10 taka note(s)')
if no_of_note > 0:
    rest = no_of_note % 10
    a = rest
else:
    bill = a

no_of_note = bill // 5
print(no_of_note, '5 taka note(s)')
if no_of_note > 0:
    rest = no_of_note % 5
    a = rest
else:
    bill = a

no_of_note = bill // 2
print(no_of_note, '2 taka note(s)')
if no_of_note > 0:
    rest = no_of_note % 2
    a = rest
else:
    bill = a
no_of_note = bill // 1
print(no_of_note, '1 taka note(s)')