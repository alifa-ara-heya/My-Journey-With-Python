#Day_5: August/01/2020
#In the name 0f Allah..
#Me: Alifa Ara Heya
#Book: Automate the boring staff by Python and Asabeneh and Teclado:

print(42 == 42)                        #output: True (checking logical operation)
print(42 > 43)                         #output: False
print(50 > 20)
print(42 == "43")                      #False because the second data type is string
print(42 == 000000042.000000000000)    #True

spam = True
print(type(spam))
print(spam)
print()
print(2 != 3)                          #2 is not equal to 3, so True
print(2 != 2)                          #False

print("spam" == 'spam')                #true
print(True == "True")                  #False
print(True == True)                    #true

eggCount = 42
print(eggCount >= 42)                  #>= greater than or equal to, so true

my_age = 29  
print(my_age <= 50)                    #less than or equal to, so true

print("Cat" == "cat")                  #False
print("cat" == "cat")                  #True
print(len("tomato") == len("potato"))  #True
print('A' < 'a')                       #True (The ASCII code for A is 65, while a is 97)
print("m" > "M")                       #True

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)                          #True
print(a is b)                          #False
print(id(a))                           #14538824
print(id(b))                           #14538888 (different memory location)

a = [1, 2, 3]
b = a
print(id(a))                           #14285896
print(id(b))                           #14285896 (same location)
print(a == b)                          #True
print(a is b)                          #True

#Boolean Operators:
print(True and True)                   #True
print(True or False)                   #True
print(False or True)                   #True
print()

print('"not" operator:')
print(not True)                        #evaluates to opposite value, so False;
print(not not True)                    #True
print(not not not True)                #False
print(not not not not True)            #True
print(not False)                       #True
print(not not False)                   #False

print(10 >= 10)                        #True
print(10 == "10")                      #False
print(10 == '10')                      #False
print(5 + 4 < 3 * 2)                   #False
print((5 + 4) < (3 * 2))               #False
print(10 != '10')                      #True (not equal)
print({1, 2} == {2, 1})                #True  (because set is unordered)
print([1, 2] == [2, 1])                #False (because list is ordered)
print((4 < 5) and (5 < 4))             #False, because none of the values istrue
print(4 < 5 and 5 < 6)                 #True
print(5 > 4 or 6 > 10)                 #True, because one of the values is true
print(2 + 2 == 4 and 2 + 2 == 5)       #False
print(2 + 2 == 4 and not 2 + 2 == 5)   #True
print(2 + 2 == 4 and not 2 + 2 == 5)   #True    
print(2 + 2 == 4 and 2 + 2 == 5 and 2 * 2 == 2 + 2)  #false   and not > and > or
print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)     #true
print(2 + 2 == 4 and not 2 + 2 == 5 and not 2 * 2 == 2 + 2) #false

x = 3
x +=5
print(x)                               #output: 8
print(x == 8 )                         #output: true

x -=6
print(x)                               #output: 2  as,(8-6=2)

#is and in operator:
print(1 is 1)                          #True
print(2 is 1)                          #False
print("A" in "Alifa")                  #True
print("A in Alifa:" , 'A' in 'Alifa')  #A in Alifa: True
print("coding" in "coding for all")    #True
print(4 is 2*2)                        #True


# bool:
print(bool("Hello!"))           # True
print(bool(0))                  # False
print(bool("Caterpillar"))      # True
print(bool(2))                  # True
print(bool(""))                 # False
print(bool(" "))                # True
print(bool(True))               # True
print(bool(False))              # False
print(bool([]))                 # False
print(bool([ ]))                # False
print(bool({ }))                # False
print(bool({" "}))              # True
print(bool([0, 1, 2, 3]))       # True
print(bool(None))               # False

# Only a small number of values in Python are falsy, which are as follows:
# Any numeric representation of zero. This includes the integer 0, the float 0.0, and representations of zero in other numeric types.
# The values False and None. We haven't looked at None yet, but None represents the intentional absence of a value.
# Empty sequences and other collections. This includes empty strings, empty tuples, empty lists, and several types we haven't covered at this stage.

